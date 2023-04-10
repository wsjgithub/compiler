class Evaluator:
    def __init__(self, ast):
        self.root = ast
    
    def evaluate(self):
        stack = Stack()
        self.root.preorder()
        self.root and self.preorder(self.root, stack)
        print('evaluate')
        stack.print()
        if len(stack) != 1:
            raise Exception("Expression failed to evaluate.")
        return stack[0]

    def preorder(self, root, stack):
        stack.append(root)
        root.left and self.preorder(root.left, stack)
        root.middle and self.preorder(root.middle, stack)
        root.right and self.preorder(root.right, stack)


class Stack(list):
    # def __init__(self):
    #     self.stack = []

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
    # def __len__(self):
    #     return len(self.stack)

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
            

