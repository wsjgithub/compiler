from language.parser import Parser


def parserRun(tokens):
    print('parsing ')
    try:
        output = ''
        try:
            output  += Parser(tokens).parse().preorderOutput()
        except Exception as e:
            return output + str(e) + '\n'
        output += '\n'
        return output
    except Exception as e:
        print("Error: ", e)