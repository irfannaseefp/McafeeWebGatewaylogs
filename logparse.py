#!/usr/bin/env python

"""
USAGE:

logparse.py log_file output_file

This script takes apache log file of the below format and ouput a csv file

[20/Nov/2019:00:01:32 +0530] "USERNAME" SOURCEIP 407 "GET http://www.msftncsi.com/ncsi.txt HTTP/1.1" "Business" "Minimal Risk" "" 4226 150 "Microsoft NCSI" "" "81" "" 221.135.111.120

"""

import sys
import csv



def parse(logfile,outfile):
    outcsv = csv.writer(outfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for line in logfile:
        split_line = line.split()
        outcsv.writerow([split_line[2],split_line[3],split_line[5],split_line[6]])



if __name__ == "__main__":
    if not len(sys.argv) > 1:
        print (__doc__)
        sys.exit(1)

    inputfilename  = sys.argv[1]
    outputfilename = sys.argv[2]

    try:
        inputfile = open(inputfilename, 'r')
        outputfile = open(outputfilename,'w')
    except IOError:
        print ("You must specify a valid file to parse")
        print (__doc__)
        sys.exit(1)

    parse(inputfile,outputfile)
    
    inputfile.close()
    outputfile.close()
