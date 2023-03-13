from language.scanner import Scanner
from language.utils import serializeToken

# def scannerTest(inputFilePath, outputFilePath):  
#     try:
#         inputFile = open(inputFilePath)
#         outputFile = open(outputFilePath,'w')
#     except FileNotFoundError as e:
#         print(e)
#         return
#     while True:
#         line = inputFile.readline()
#         if line:
#             print('scanning ',line)
#             scanner = Scanner()
#             try:
#                 tokens = scanner.scan(line)
#                 outputFile.write("LINE: " + line+'\n')
#                 for token in tokens:
#                     outputFile.write(serializeToken(token)+'\n')
#                 outputFile.write('\n')
#             except Exception as e:
#                 print("Error: ", e)
#         else:
#             break
#     inputFile.close()
#     outputFile.close()
#     print('Scanning finished')

# def scannerRun(line):
#     print('scanning ',line)
#     scanner = Scanner()
#     try:
#         tokens = scanner.scan(line)
#         output = ''
#         output += ("LINE: " + line+'\n')
#         for token in tokens:
#             output += (serializeToken(token)+'\n')
#         output += '\n'
#         return output
#     except Exception as e:
#         print("Error: ", e)



def scannerRun(line):
    print('scanning ',line)
    scanner = Scanner()
    try:
        tokens = scanner.scan(line)
        output = ''
        for token in tokens:
            output += (serializeToken(token)+'\n')
        return (tokens, output)
    except Exception as e:
        print("Error: ", e)