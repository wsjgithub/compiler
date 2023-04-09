from .asTree import Node
from .utils import raiseException
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.cursor = 0

    def parse(self):
        try:
            curr = self.currentToken()
            node = self.statement()
        except Exception as e:
            raiseException('Error parsing token: ' + (str(curr) if curr else 'end of tokens') + "; " + str(e))
        curr = self.currentToken()
        if curr:
            raiseException('Error parsing token: ' + (str(curr) if curr else 'end of tokens') + "; " + 'There are unparsed tokens.')
        return node
    
    def parseExpression(self):
        node = self.expression()
        return node
    
    def binaryOperator(self, nextOpt, sign):
        left = getattr(self, nextOpt)()
        curr = self.currentToken()
        while curr and curr[0] == sign:
            self.consume()
            right = getattr(self, nextOpt)()
            if not right:
                raiseException("Expression: nothing is on the right side of " + sign)
            left = Node(*curr, left, right)
            curr = self.currentToken() 
        return left
    
    def statement(self):
        return self.binaryOperator('baseStatement', ';')
    
    def baseStatement(self):
        node = self.assignment()
        if not node:
            node = self.ifStatement()
        if not node:
            node = self.whileStatement()
        if not node:
            curr = self.currentToken()
            if curr and curr[1] == 'KEYWORD' and curr[0] == 'skip':
                node = Node(*curr)
                self.consume()
            else:
                raiseException("baseStatement: invalid base statement.")
        return node
    
    def assignment(self):
        curr = self.currentToken()
        if curr and curr[1] == 'IDENTIFIER':
            left = Node(*self.currentToken())
            self.consume()
            if self.currentToken()[0] == ':=':
                sign = self.currentToken()
                self.consume()
                right = self.expression()
                if right:
                    return Node(*sign, left, right)
                else:
                    raiseException('Assignment: there is nothing on the right side of :=')
            else:
                raiseException('Assignment: Failed to match :=')

    def whileStatement(self):
        curr = self.currentToken()
        if curr and curr[1] == 'KEYWORD' and curr[0] == 'while':
            self.consume()
            left = self.expression()
            if not left:
                raiseException("whileStatement: while expression is missing.")
            curr = self.currentToken()
            if curr and curr[1] == 'KEYWORD' and curr[0] == 'do':
                self.consume()
                middle = self.statement()
                if not middle:
                    raiseException("whileStatement: do statement is missing.")
                curr = self.currentToken()
                print('while', curr)
                if curr and curr[1] == 'KEYWORD' and curr[0] == 'endwhile':
                    self.consume()
                    node = Node('while','KEYWORD', left, middle)
                    return node
                else:
                    raiseException("whileStatement: keyword endwhile is missing.")
            else:
                raiseException("ifStatement: keyword do is missing.")
        
    def ifStatement(self):
        curr = self.currentToken()
        if curr and curr[1] == 'KEYWORD' and curr[0] == 'if':
            self.consume()
            left = self.expression()
            if not left:
                raiseException("ifStatement: if expression is missing.")
            curr = self.currentToken()
            if curr and curr[1] == 'KEYWORD' and curr[0] == 'then':
                self.consume()
                middle = self.statement()
                if not middle:
                    raiseException("ifStatement: then statement is missing.")
                curr = self.currentToken()
                if curr and curr[1] == 'KEYWORD' and curr[0] == 'else':
                    self.consume()
                    right = self.statement()
                    if not right:
                        raiseException("ifStatement: else statement is missing.")
                    curr = self.currentToken()
                    if curr and curr[1] == 'KEYWORD' and curr[0] == 'endif':
                        self.consume()
                        node = Node('if','KEYWORD', left, middle, right)
                        return node
                    else:
                        raiseException("ifStatement: keyword endif is missing.")
                else:
                    raiseException("ifStatement: keyword else is missing.")
            else:
                raiseException("ifStatement: keyword then is missing.")
        
    def expression(self):
        return self.binaryOperator('term', '+')
    
    def term(self):
        return self.binaryOperator('factor','-')
    
    def factor(self):
        return self.binaryOperator('piece', '/')
    
    def piece(self):
        return self.binaryOperator('element', '*')
    
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
    
    def currentToken(self):
        if self.cursor < len(self.tokens):
            return self.tokens[self.cursor]