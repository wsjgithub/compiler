# Shengjiao Wang, Raymond Lee
# 1.2


import sys
from test.scannerTest import scannerRun

def run():
    arguments = sys.argv
    if len(arguments) < 3:
        print('Input or output files were not specified.')
    else:
        # scannerTest(arguments[1], arguments[2])
        inputFilePath = arguments[1]
        outputFilePath = arguments[2]
        try:
            inputFile = open(inputFilePath)
            outputFile = open(outputFilePath,'w')
        except FileNotFoundError as e:
            print(e)
            return
        while True:
            line = inputFile.readline()
            if line:
               scanned = scannerRun(line)
               outputFile.write(scanned)
            else:
                break
        inputFile.close()
        outputFile.close()





run()