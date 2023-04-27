
from language.evaluator import Evaluator
def evaluatorRun(ast):
    print('evaluating')
    output = 'Output: '
    try:
        result = Evaluator(ast).evaluate()
        if result:
            output += str(result)
    except Exception as e:
        output += 'Error: ' + str(e)
    return output





