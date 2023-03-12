from .asTree import Node
from .utils import raiseException
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.cursor = 0

    def parse(self):
        try:
            return self.expression()
        except Exception as e:
            curr = self.currentToken()
            raiseException('Error parsing token: ' + (str(curr) if curr else 'end of tokens') + "; " + str(e))
    
    def expression(self):
        left = self.term()
        curr = self.currentToken()
        while curr and curr[0] == '+': 
            self.consume()
            right = self.term()
            if not right:
                raiseException("Expression: nothing is on the right side of +")
            left = Node(*curr, left, right)  
            curr = self.currentToken() 
        if curr:
            raiseException('Expression: there are unparsed tokens starting from: '+ str(curr))
        return left
        
    def currentToken(self):
        if self.cursor < len(self.tokens):
            return self.tokens[self.cursor]
    
    def term(self):
        left = self.factor()
        curr = self.currentToken()
        while curr and curr[0] == '-':
            self.consume()
            right = self.factor()
            if not right:
                raiseException("Term: nothing is on the right side of -")
            left = Node(*curr, left, right)
            curr = self.currentToken()
        return left
    
    def factor(self):
        left = self.piece()
        curr = self.currentToken()
        while curr and curr[0] == '/':
            self.consume()
            right = self.piece()
            if not right:
                raiseException("Term: nothing is on the right side of /")
            left = Node(*curr, left, right)
            curr = self.currentToken()
        return left
    
    def piece(self):
        left = self.element()
        curr = self.currentToken()
        while curr and curr[0] == '*':
            self.consume()
            right = self.element()
            if not right:
                raiseException("piece: nothing is on the right side of *")
            left = Node(*curr, left, right)
            curr = self.currentToken()
        return left
    
    def element(self):
        curr = self.currentToken()
        if curr:
            if curr[1] == 'ERROR':
                raiseException("Element: An error token was found. ")
            if curr[0] == "(":
                self.consume()
                node = self.expression()
                if not node:
                    raiseException("Element: Nothing follows (.")
                curr = self.currentToken()
                if curr and curr[0] == ')':
                    self.consume()
                    return node
                else:
                    raiseException("Element: Right parenthesis was not found.")
            elif curr[1] in ("NUMBER", "IDENTIFIER"):
                self.consume()
                return Node(*curr)
            else:
                raiseException("Element: Token is not valid.")
    
    def consume(self):
        self.cursor += 1

if __name__ == 'main':
    Parser([('Error', 'ERROR')]).parse()