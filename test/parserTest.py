from language.parser import Parser


def parserRun(tokens, expression = False, returnAST = False):
    print('parsing ')
    output = ''
    ast = None
    try:
        if expression:
            ast = Parser(tokens).parseExpression()  
        else:
            ast  = Parser(tokens).parse()
        output  += ast.preorderOutput()
    except Exception as e:
        raise Exception(output + str(e) + '\n')
    output += '\n'
    if returnAST:
        return output, ast
    return output


