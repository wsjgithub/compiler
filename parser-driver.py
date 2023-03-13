# Shengjiao Wang, Raymond Lee
# 1.2


import sys
from test.parserTest import parserRun
from test.scannerTest import scannerRun
def run():
    arguments = sys.argv
    inputFilePath = 'input.txt'
    outputFilePath = 'output.txt'
    if len(arguments) < 3:
        print('Input or output files were not specified. Using input.txt, output.txt as intput and output file paths.')
    else:
        inputFilePath = arguments[1]
        outputFilePath = arguments[2]
    try:
        inputFile = open(inputFilePath)
        outputFile = open(outputFilePath,'w')
    except FileNotFoundError as e:
        print(e)
        return
    tokens = []
    outputFile.write('Tokens: \n')
    while True:
        line = inputFile.readline()
        if line:
            scannedTokens, scannedOutput = scannerRun(line)
            tokens += scannedTokens
            outputFile.write(scannedOutput)
        else:
            break
    parsed = '\nAST: \n' + parserRun(tokens) + '\n'
    outputFile.write(parsed)
    inputFile.close()
    outputFile.close()





run()