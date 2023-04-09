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
    line = inputFile.readline()
    output = 'Tokens: \n'
    tokens = []
    while line:
        lineOutput, lineTokens= scannerRun(line)
        output += lineOutput + '\n'
        tokens += lineTokens
        line = inputFile.read()
    output += 'AST: \n' + parserRun(tokens) + '\n'
    outputFile.write(output)  
    inputFile.close()
    outputFile.close()





run()