import sys

def readWrite(operation):
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
    output = operation(inputFile)
    outputFile.write(output)  
    inputFile.close()
    outputFile.close()