from .asTree import Node
from .constants import MARKS
import copy
class Evaluator:
    def __init__(self, ast):
        if ast and ast.value != ';':
            self.root = Node(';', MARKS['symbol'], ast)
        else:
            self.root = ast
        self.memory = {}
        self.parent = None
        self.curr = self.root
    
    def evaluate(self):
        while self.root and self.root.left:
            self.evaluateStatement()
            print('evaluate', self.root, self.root.left)
            self.root.preorder()
        print('memoery', self.memory)
        self.root = None
        self.parent = None
        self.curr = None

    def evaluateStatement(self):
        while True:
            if not self.curr:
                raise Exception('Statement is missing.')
            if self.curr.value != ';':
                self.evaluateBaseStatement()
                # if self.parent:
                #     self.parent.left = self.parent.middle
                #     self.parent.middle = None
                break
            if not self.curr.left:
                self.parent.left = self.parent.middle
                self.parent.middle = None
                break
            self.parent = self.curr
            self.curr = self.curr.left 
        self.parent = None
        self.curr = self.root

    def evaluateBaseStatement(self):
        if self.curr.value == ':=':
            self.evaluateAssignment()
        elif self.curr.value == 'if':
            self.evaluateCondition()
        elif self.curr.value == 'while':
            self.evaluateLoop()
        else:
            raise Exception("Not a valid base statement")

    def evaluateAssignment(self):
        value = self.evaluateExpression(self.curr.middle)[0]
        self.memory[self.curr.left.value] = int(value)
        # if self.parent:
        #     self.parent.left = None
        self.adjustTree()

    def evaluateCondition(self):
        pass
    
    def evaluateLoop(self):
        condition = self.curr.left
        operation = copy.deepcopy(self.curr.middle)
        expr = self.evaluateExpression(condition)
        print('expr', expr)
        if expr[0] == 0:
            self.adjustTree()
        else:
            self.parent.left = Node(';', MARKS['symbol'], operation, self.curr)
        self.root.preorder()

    def evaluateExpression(self, root): 
        stack = Stack()
        root and self.preorder(root, stack)
        if len(stack) != 1:
            raise Exception("Expression failed to evaluate.")
        return stack[0]
    
    def adjustTree(self):
        if self.parent:
            self.parent.left = self.parent.middle
            self.parent.middle = None

    def preorder(self, root, stack):
        # need to resolve an identifier with the memory table
        stack.append(self.resolveIdentifier(root))
        root.left and self.preorder(root.left, stack)
        root.middle and self.preorder(root.middle, stack)
        root.right and self.preorder(root.right, stack)

    def resolveIdentifier(self, node):
        if node.type == MARKS['identifier']:
            try:
                return Node(self.memory[node.value], MARKS['number'])
            except KeyError:
                raise Exception('Accessed an uninitialized identifier.')
        else:
            return node

class Stack(list): 
    def append(self, el):
        calculable = True
        el = (el.value, el.type)
        super().append(el)
        while len(self) > 0 and calculable:
            lastThree = self[-3:]
            if self.isCalculable(lastThree):
                del self[-3:]
                result = Calculator.calBinary(*[node[0] for node in lastThree])
                super().append((result, "NUMBER"))
            else:
                calculable = False


    def isCalculable(self, lastThree):
        return len(lastThree) == 3 and lastThree[0][1] == "SYMBOL" and lastThree[1][1] == "NUMBER" and lastThree[2][1] == "NUMBER"

    def print(self):
        for item in self:
            print(item)


class Calculator:
    def calBinary(operator, num1, num2):
        num1, num2 = int(num1), int(num2)
        match operator:
            case "/":
                if num2 == 0:
                    raise Exception('Divisor cannot be zero.')
                return num1 // num2
            case "-":
                return max(num1 - num2, 0)
            case "*":
                return num1 * num2
            case "+":
                return num1 + num2
            case _:
                raise Exception("Unsupported operator is found: " + str(operator))
            

