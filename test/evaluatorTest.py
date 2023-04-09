from language.scanner import Scanner
from language.parser import Parser
from language.evaluator import Evaluator
def evaluatorRun(line):
    print('evaluator test')
    tokens = Scanner().scan(line)
    print(tokens)
    ast = Parser(tokens).parseExpression()
    Evaluator(ast).evaluate()



