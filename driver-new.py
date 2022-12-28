#!/usr/bin/env python3


import sys
import argparse
import concord4

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=str, required=True)
    parser.add_argument('--output', type=str, required=True)
    args = parser.parse_args()

    saved_stdout, saved_stderr = sys.stdout, sys.stderr
    sys.stdout, sys.stderr = None, None

    cc = concord4.concord(args.input, args.output)

    sys.stdout, sys.stderr = saved_stdout, saved_stderr






if __name__ == "__main__":
    main()
