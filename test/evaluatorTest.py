
from language.evaluator import Evaluator
def evaluatorRun(ast):
    print('evaluating')
    output = 'Output: '
    result = Evaluator(ast).evaluate()
    if result:
        output += str(result[0])
    # try:
    #     result = Evaluator(ast).evaluate()
    #     if result:
    #         output += str(result[0])
    # except Exception as e:
    #     output += 'Error: ' + str(e)
    return output





