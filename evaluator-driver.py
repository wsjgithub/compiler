from test.evaluatorTest import evaluatorRun
from file.file import readWrite
from test.parserTest import parserRun
from test.scannerTest import scannerRun



def run(inputFile):
    line = inputFile.read()
    print('line', line)
    #input = '3 * (5 + 10 / 3 - 1)'
    #evaluatorRun(input)
    output = ''
    # try:
    #     lineOutput, lineTokens= scannerRun(line)
    #     output += lineOutput + '\n'
    #     parsedOutput, ast = parserRun(lineTokens, False, True)
    #     output += 'AST: \n' + parsedOutput + '\n'
    #     output += evaluatorRun(ast)
    # except Exception as e:
    #     print(e)
    #     output += "\n" + str(e)
    lineOutput, lineTokens= scannerRun(line)
    output += lineOutput + '\n'
    parsedOutput, ast = parserRun(lineTokens, False, True)
    output += 'AST: \n' + parsedOutput + '\n'
    output += evaluatorRun(ast)
    return output


readWrite(run)