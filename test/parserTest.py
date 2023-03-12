from language.parser import Parser
from language.scanner import Scanner
from language.utils import serializeToken

def parserRun(line):
    print('parsing ',line)
    scanner = Scanner()
    try:
        tokens = scanner.scan(line)
        output = ''
        output += ("LINE: " + line+'\n')
        try:
            output  += Parser(tokens).parse().preorderOutput()
        except Exception as e:
            print('catch', e)
            return output + str(e)
        output += '\n'
        return output
    except Exception as e:
        print("Error: ", e)