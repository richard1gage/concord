#   concord4.py
#   Richard Gage

import sys, re, fileinput
from pprint import pprint  #for debugging
from operator import itemgetter, attrgetter

class concord:

    def __init__(self, input=None, output=None):
        self.input = input  #holds input file if given
        self.output = output  #holds output file if given
        self.lines_list = []
        self.exclusion_string = ""
        self.output_list = []

        if(self.input != None):
            results = self.full_concordance()
            self.__write_to_file(results)

    def __write_to_file(self, results):
        with open(self.output, 'w') as f:
            f.write('\n'.join(results))
            f.write('\n')
        f.close()

    def full_concordance(self):
        '''
        main function in concord class which runs all other functions within the class.
        '''
        self.__get_lines_from_input()
        self.__determine_exclusion_words()
        self.__list_builder()
        self.__index_word_capitalizer()       
        self.output_list = sorted(self.output_list, key = itemgetter(0,2))
        self.__line_whitespace_formatter()

        newlines = [line[1] for line in self.output_list]  #creating a list for final output
        return newlines

    def __get_lines_from_input(self):
        if(self.input != None):  #for when driver-new.py is used
            file= open(self.input, "r")
            self.lines_list = [line.strip() for line in file if line != '\n' ]
            file.close()
        else:  #for when driver-original.py is used
            self.lines_list = [line.strip() for line in fileinput.input() if line != '\n']
    	
        if(self.lines_list[0] == '1'):  #test for correct input test file
            print("Input is version 1, concord4.py expected version 2")
            sys.exit(0)

    def __determine_exclusion_words(self):
        exclusion_start_index = (self.lines_list.index("''''") + 1)
        exclusion_stop_index = self.lines_list.index('""""')
        exclusion_word_range = range(exclusion_start_index, exclusion_stop_index)

        exclusion_list = [self.lines_list[i].lower() for i in exclusion_word_range]
        self.exclusion_string = " ".join(exclusion_list)
        self.lines_list = self.lines_list[exclusion_stop_index+1:]

    def __list_builder(self):
        '''
        Checks every word in each line-for-indexing to see whether it is in the exclusion list,
        if the word isn't excluded, then a list of the following form: [the word, the line it is from, line number index]
        is appended to the self.output_list.
        '''
        index_for_sorting = 1
        for line in self.lines_list:
            line_words = re.split(r'\s', line)
            for word in line_words:
                if(re.search(r"\b" + word.lower() + r"\b", self.exclusion_string) == None):
                    self.output_list.append([word, line, index_for_sorting])
                    index_for_sorting += 1

    def __index_word_capitalizer(self): 
        '''
        Goes through each line, capitalizing the index word in each line.
        '''
        for line in self.output_list:        
            line[1] = re.sub(r"\b" + line[0]+ r"\b", line[0].upper(), line[1])
            line[0] = line[0].upper()  #done for later sorting by index word

    def __line_whitespace_formatter(self):
        '''
        Formats each full line in lines_list, left aligning index words at the 30th column of output.
        Words to the left of the index word do not appear if they go further left than col 10.
        Words to the right of the index word do not appear if they go further right than col 60.
        '''
        for line in self.output_list:
            regex = re.search(r"\b"+line[0]+r"\b", line[1])
            word_index = regex.start()
            while(word_index > 20):
                line[1] = re.sub('^\S+\s+', '', line[1])  #removes first word from line[1]
                word_index = line[1].find(line[0])
            line[1] = line[1].rjust(29+len(line[1][word_index:]), " ")

            while(len(line[1])> 60):  #keep removing words from the end until line doesn't pass col 60
                regex2 = re.search('\S+$', line[1])
                line[1] = line[1][:regex2.start()-1]