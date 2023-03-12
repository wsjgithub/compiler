from .asTree import Node
from .utils import serializeToken
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.cursor = 0

    def parse(self):
        try:
            return self.expression()
        except Exception as e:
            print('parse exception', e)
            curr = self.currentToken()
            raise Exception('Error parsing token: ' + (str(curr) if curr else 'end of tokens'))
    
    def expression(self):
        left = self.term()
        curr = self.currentToken()
        while curr and curr[0] == '+': 
            self.consume()
            right = self.term()
            if not right:
                err = "Expression: nothing is on the right side of +"
                print(err)
                raise Exception ("err")
            left = Node(*curr, left, right)  
            curr = self.currentToken() 
        if curr:
            err = 'Expression: there are unparsed tokens starting from: '
            print(err, curr)  
            raise Exception(err, str(curr))
        return left
        
    def currentToken(self):
        if self.cursor < len(self.tokens):
            return self.tokens[self.cursor]
    
    def term(self):
        left = self.factor()
        curr = self.currentToken()
        while curr and curr[0] == '-':
            self.consume()
            left = Node(*curr, left, self.factor())
            curr = self.currentToken()
        return left
    
    def factor(self):
        left = self.piece()
        curr = self.currentToken()
        while curr and curr[0] == '/':
            self.consume()
            left = Node(*curr, left, self.piece())
            curr = self.currentToken()
        return left
    
    def piece(self):
        left = self.element()
        curr = self.currentToken()
        while curr and curr[0] == '*':
            self.consume()
            left = Node(*curr, left, self.element())
            curr = self.currentToken()
        return left
    
    def element(self):
        curr = self.currentToken()
        if curr:
            if curr[1] == 'ERROR':
                raise Exception("An error token was found. ")
            if curr[0] == "(":
                self.consume()
                node = self.expression()
                if not node:
                    print("Nothing follows (.")
                    raise Exception("Nothing follows (.")
                curr = self.currentToken()
                if curr and curr[0] == ')':
                    self.consume()
                    return node
                else:
                    print("Right parenthesis not found.")
                    raise Exception("Right parenthesis not found.")
            elif curr[1] in ("NUMBER", "IDENTIFIER"):
                self.consume()
                return Node(*curr)
            else:
                print("Error while parsing element.")
                raise Exception('Error while parsing element.')
    
    def consume(self):
        self.cursor += 1


