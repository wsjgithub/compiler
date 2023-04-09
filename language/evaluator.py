class Evaluator:
    def __init__(self, ast):
        self.root = ast
    
    def evaluate(self):
        stack = Stack()
        self.root.preorder()
        self.root and self.preorder(self.root, stack)
        print('evaluate')
        stack.print()
        return stack

    def preorder(self, root, stack):
        stack.append(root)
        root.left and self.preorder(root.left, stack)
        root.middle and self.preorder(root.middle, stack)
        root.right and self.preorder(root.right, stack)


class Stack:
    def __init__(self):
        self.stack = []

    def append(self, el):
        calculable = True
        el = (el.value, el.type)
        self.stack.append(el)
        while self.stack and calculable:
            lastThree = self.stack[-3:]
            if self.isCalculable(lastThree):
                del self.stack[-3:]
                result = Calculator.calBinary(*[node[0] for node in lastThree])
                self.stack.append((result, "NUMBER"))
            else:
                calculable = False


    def isCalculable(self, lastThree):
        return len(lastThree) == 3 and lastThree[0][1] == "SYMBOL" and lastThree[1][1] == "NUMBER" and lastThree[2][1] == "NUMBER"

    def print(self):
        for item in self.stack:
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
            

