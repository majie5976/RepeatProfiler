#! /usr/bin/env python
import sys
import collections
import re

# Set input file name
# (program must be run from within the directory
# that contains this data file)
# InFileName = "testout.txt"

OutFileName = "pileup_counted.txt"  # pileup_counted.txt
countedFile = sys.argv[2] + ".csv"
The_refrence_size = int(sys.argv[3])
countedFile_multi = "multi_poly/" + sys.argv[2] + ".txt"
# Open input file for reading, 'r' is "read mode"
# InFile = open(InFileName, 'r')

with open(OutFileName, "w") as OutFile:
    # DepthList = [ ]

    Dict = {}  # defines an empty dictionary

    # "1_pileup.out"
    with open(sys.argv[1], 'r') as InFile:
        for Line in InFile:

            # if LineNumber >= 0: #for infile with a header, change to '> 0'
            Strip = Line.strip('\n')  # removes line ending characters
            ElementList = Strip.split(
                '\t')  # splits line into elements defined by tabs and adds each element to list ElementList

            while True:  # this loop uses regex to strip out indel information from the mpileup input file which will throw off base counts
                match = re.search(r"[+-](\d+)", ElementList[
                    4])  # makes a list of all instances of the first element of indel notation (+/- and 1 or more digits)

                if match is None:
                    break
                ElementList[4] = ElementList[4][:match.start()] + ElementList[4][match.end() + int(match.group(
                    1)):]  # replaces the first and second component of indel information (+/- and 1 or more digits and the bases that follow the digits)

            # print(ElementList[4])

            DictPosition = int(ElementList[
                                   1])  # makes the list of keys for the dictionary using the second element in ElementList (position)
            DictBases = ElementList[
                4].upper()  # defines uppercase string of bases in fifth element in ElementList in preparation to make dictionary
            DictDepth = ElementList[3]  # defines fourth element (depth) as a value in the dictionary
            Dict[DictPosition] = (DictBases,
                                  DictDepth)  # this makes the dictionary with DictPosition as the key and DictBases and DictDepth as the values

    # print(Dict)
    HeaderInfo = 'Position\tCountMatch\tCountA\tCountT\tCountG\tCountC\t' + 'Depth'
    OutFile.write(HeaderInfo + "\n")
    Fixing = 1
    for Position in sorted(
            Dict.keys()):  # loops through keys (position) in dictionary and counts the number of each base in the 0th element stored as a value in the dictionary. * count in coverage, ',' and '.' are the characters that indicate the base matches the reference sequence.
        print(" pos:" + str(Fixing) + "    " + str(Position))

        while Fixing != Position:
            OutputString = "%s  %d  %d  %d  %d  %d  %s" % (str(Fixing), 0, 0, 0, 0, 0, "0")

            OutFile.write(OutputString + "\n")
            Fixing = Fixing + 1

        Fixing = Fixing + 1

        NumA = Dict[Position][0].count('A')
        NumT = Dict[Position][0].count('T')
        NumG = Dict[Position][0].count('G')
        NumC = Dict[Position][0].count('C')
        # NumE = Dict[Position][0].count('*')
        NumF = Dict[Position][0].count(',') + Dict[Position][0].count('.') + Dict[Position][0].count('*')

        # print("%s	%d   %d  %d  %d  %d	%s" % (Position, NumA, NumF, NumT, NumG, NumC, Dict[Position][1]))

        # unlike the print command, write requires manual new line command, this prints one element to file in a single column
        OutputString = "%s  %d  %d  %d  %d  %d  %s" % (Position, NumF, NumA, NumT, NumG, NumC, Dict[Position][1])
        OutFile.write(OutputString + "\n")
    print('so long')
    while Fixing != The_refrence_size:
        print("in whileloop")
        OutputString = "%s  %d  %d  %d  %d  %d  %s" % (str(Fixing), 0, 0, 0, 0, 0, "0")
        OutFile.write(OutputString + "\n")
        Fixing = Fixing + 1
    # OutFile.close()

with open(countedFile, "w") as OutFile:
    # DepthList = [ ]

    Dict = {}  # defines an empty dictionary

    # "1_pileup.out"
    with open(sys.argv[1], 'r') as InFile:
        for Line in InFile:

            # if LineNumber >= 0: #for infile with a header, change to '> 0'
            Strip = Line.strip('\n')  # removes line ending characters
            ElementList = Strip.split(
                '\t')  # splits line into elements defined by tabs and adds each element to list ElementList

            while True:  # this loop uses regex to strip out indel information from the mpileup input file which will throw off base counts
                match = re.search(r"[+-](\d+)", ElementList[
                    4])  # makes a list of all instances of the first element of indel notation (+/- and 1 or more digits)

                if match is None:
                    break
                ElementList[4] = ElementList[4][:match.start()] + ElementList[4][match.end() + int(match.group(
                    1)):]  # replaces the first and second component of indel information (+/- and 1 or more digits and the bases that follow the digits)

            # print(ElementList[4])

            DictPosition = int(ElementList[
                                   1])  # makes the list of keys for the dictionary using the second element in ElementList (position)
            DictBases = ElementList[
                4].upper()  # defines uppercase string of bases in fifth element in ElementList in preparation to make dictionary
            DictDepth = ElementList[3]  # defines fourth element (depth) as a value in the dictionary
            Dict[DictPosition] = (DictBases,
                                  DictDepth)  # this makes the dictionary with DictPosition as the key and DictBases and DictDepth as the values

    # print(Dict)
    HeaderInfo = 'Position,' + sys.argv[2]
    OutFile.write(HeaderInfo + "\n")

    Fixing = 1
    for Position in sorted(
            Dict.keys()):  # loops through keys (position) in dictionary and counts the number of each base in the 0th element stored as a value in the dictionary. * count in coverage, ',' and '.' are the characters that indicate the base matches the reference sequence.
        # print "%s" % (Position)
        # print(" pos:" + str(Fixing) + "    " + str(Position))

        while Fixing != Position:
            OutputString = str(Fixing) + ",0"

            OutFile.write(OutputString + "\n")
            Fixing = Fixing + 1

        Fixing = Fixing + 1

        NumA = Dict[Position][0].count('A')
        NumT = Dict[Position][0].count('T')
        NumG = Dict[Position][0].count('G')
        NumC = Dict[Position][0].count('C')
        NumF = Dict[Position][0].count(',') + Dict[Position][0].count('.') + Dict[Position][0].count('*')
        OutputString = "%s,%s" % (Position, Dict[Position][1])
        OutFile.write(OutputString + "\n")

    while Fixing != The_refrence_size:
        # print("in whileloop")
        OutputString = str(Fixing) + ",0"
        OutFile.write(OutputString + "\n")
        Fixing = Fixing + 1

with open(countedFile_multi, "w") as OutFile:
    # DepthList = [ ]

    Dict = {}  # defines an empty dictionary

    # "1_pileup.out"
    with open(sys.argv[1], 'r') as InFile:
        for Line in InFile:

            # if LineNumber >= 0: #for infile with a header, change to '> 0'
            Strip = Line.strip('\n')  # removes line ending characters
            ElementList = Strip.split(
                '\t')  # splits line into elements defined by tabs and adds each element to list ElementList

            while True:  # this loop uses regex to strip out indel information from the mpileup input file which will throw off base counts
                match = re.search(r"[+-](\d+)", ElementList[
                    4])  # makes a list of all instances of the first element of indel notation (+/- and 1 or more digits)

                if match is None:
                    break
                ElementList[4] = ElementList[4][:match.start()] + ElementList[4][match.end() + int(match.group(
                    1)):]  # replaces the first and second component of indel information (+/- and 1 or more digits and the bases that follow the digits)

            # print(ElementList[4])

            DictPosition = int(ElementList[
                                   1])  # makes the list of keys for the dictionary using the second element in ElementList (position)
            DictBases = ElementList[
                4].upper()  # defines uppercase string of bases in fifth element in ElementList in preparation to make dictionary
            DictDepth = ElementList[3]  # defines fourth element (depth) as a value in the dictionary
            Dict[DictPosition] = (DictBases,
                                  DictDepth)  # this makes the dictionary with DictPosition as the key and DictBases and DictDepth as the values

    # print(Dict)
    HeaderInfo = 'Position\tCountMatch\tCountA\tCountT\tCountG\tCountC\t' + 'Depth'
    OutFile.write(HeaderInfo + "\n")
    Fixing = 1
    for Position in sorted(
            Dict.keys()):  # loops through keys (position) in dictionary and counts the number of each base in the 0th element stored as a value in the dictionary. * count in coverage, ',' and '.' are the characters that indicate the base matches the reference sequence.
        print(" pos:" + str(Fixing) + "    " + str(Position))

        while Fixing != Position:
            OutputString = "%s  %d  %d  %d  %d  %d  %s" % (str(Fixing), 0, 0, 0, 0, 0, "0")

            OutFile.write(OutputString + "\n")
            Fixing = Fixing + 1

        Fixing = Fixing + 1

        NumA = Dict[Position][0].count('A')
        NumT = Dict[Position][0].count('T')
        NumG = Dict[Position][0].count('G')
        NumC = Dict[Position][0].count('C')
        # NumE = Dict[Position][0].count('*')
        NumF = Dict[Position][0].count(',') + Dict[Position][0].count('.') + Dict[Position][0].count('*')

        # print("%s	%d   %d  %d  %d  %d	%s" % (Position, NumA, NumF, NumT, NumG, NumC, Dict[Position][1]))

        # unlike the print command, write requires manual new line command, this prints one element to file in a single column
        OutputString = "%s  %d  %d  %d  %d  %d  %s" % (Position, NumF, NumA, NumT, NumG, NumC, Dict[Position][1])
        OutFile.write(OutputString + "\n")
    print('so long')
    while Fixing != The_refrence_size:
        print("in whileloop")
        OutputString = "%s  %d  %d  %d  %d  %d  %s" % (str(Fixing), 0, 0, 0, 0, 0, "0")
        OutFile.write(OutputString + "\n")
        Fixing = Fixing + 1
    # OutFile.close()

print('end of python script')
