Description for concord program

concord4.py is a program that focuses on a particular kind of text indexing known as concordance (or "keyword in context"). A text file of the followingform is taken as input into the program. There will be a line with four single quotes ''''. Then there is a list of exclusion words, one word per line, with the exclusion list ended using a line with four double quotes """". The remainder of the file is made up of the lines-for-indexing of which the concordance will be constructed for that file.

Each line in the output contains text based on one line-for-indexing of the input with exactly one non-exclusion word capitalized. Each line in the output is also formatted so that the index words are left-aligned to begin at the 30th column of the output, and words to the left of the index word may appear but only if they do not go further left than column 10. Words to the right of the index word may appear but only if they do not go further right than column 60.

driver-original.py is used on the command line

driver-new.py accepts two file arguments, one for the name of the input file, one for the name of the output file.

The following is an example of an INPUT file, and then the resulting OUTPUT file below.


''''
of
and
the
too
on
who
to
that
""""
that fortune
sense and sensibility
life of robert browning
the man who knew too much
legend of montrose
visit to iceland
orthodoxy
the mountains
on the track
ward of king canute



              life of robert BROWNING
                ward of king CANUTE
                        that FORTUNE
                    visit to ICELAND
                     ward of KING canute
                 the man who KNEW too much
                             LEGEND of montrose
                             LIFE of robert browning
                         the MAN who knew too much
                   legend of MONTROSE
                         the MOUNTAINS
            man who knew too MUCH
                             ORTHODOXY
                     life of ROBERT browning
                             SENSE and sensibility
                   sense and SENSIBILITY
                      on the TRACK
                             VISIT to iceland
                             WARD of king canute

