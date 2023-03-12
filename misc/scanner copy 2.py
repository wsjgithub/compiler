import re

class Scanner:
    def __init__(self):
        self.MARKS = {
            'identifier': 'IDENTIFIER',
            'number': 'NUMBER',
            'symbol':'SYMBOL',
            'keyword':'KEYWORD'
        }
        self.symbols = ("+", "-", "*", "/", "(", ")",":=", ";")
        self.keywords = ("if", "then", "else", "endif", "while", "do", "endwhile", "skip")
        self.tokenTypes = ['keyword', 'identifier', 'number', 'symbol',] # exclude symbol
        self.patterns = {
            "identifier":"([a-z]|[A-Z])([a-z]|[A-Z]|[0-9])*",
            "number": '[0-9]+',
            "symbol": self._generateSymbolsPattern(self.symbols),
            "validChar": '[a-z]|[A-Z]|[0-9]|' + self._generateSymbolsPattern(self.symbols),
            "keyword":self._generateKeywordPattern(self.keywords)
        }
        self.validCharPattern = '[a-z]|[A-Z]|[0-9]|\+|\-|\*|\/|\(|\)|\:|\=|\;'
        self.whitespace = '\s'
        self.tokens = []
        self.currentToken = ''

    def scan(self, input):
        for ch in input:
            if self._isWhitespace(ch):
                self._parseToken()
            else:
                self.currentToken += ch
            # integrate symbol into parseToken
            # elif self._isSymbol(ch):
            #     self._parseToken()
            #     self.currentToken = ch
            #     self._parseSymbol()

            # elif self._isValidChar(ch):
            #     self.currentToken += ch

            # else:
            #     print('Invalid character.')
            #     self._parseToken()
                # raise Exception('Invalid character.')
        self._parseToken()
        return self.tokens

    def _parseSymbol(self):
        # additional logic for :=, : alone is not valid.
        self.tokens.append((self.currentToken, self.MARKS['symbol']))
        self.currentToken = ''   

    def _parseToken(self):
        if not self.currentToken: return 
        longestMatchedToken = ''
        longestMatchedTokenType = ''
        for type in self.tokenTypes:
            matched = re.match(self.patterns[type], self.currentToken)
            if matched and len(longestMatchedToken) < len(matched.group()):
                longestMatchedToken = matched.group() 
                longestMatchedTokenType = self.MARKS[type]
        if longestMatchedToken and longestMatchedTokenType:
            self.tokens.append((longestMatchedToken, longestMatchedTokenType))
            self.currentToken = self.currentToken[len(longestMatchedToken):]
            self._parseToken()
        else:
            print("Token doesn't match any pattern. Skipped.", self.currentToken)
        self.currentToken = ''

    def _isWhitespace(self, char):
        return re.fullmatch(self.whitespace, char)
    
    def _isSymbol(self, char):
        return re.fullmatch(self.patterns['symbol'], char)

    def _isValidChar(self, char):
        return re.fullmatch(self.validCharPattern,char)

    def _generateSymbolsPattern(self, symbols):
        return ''.join(["\\"+s+'|' for s in symbols])[:-1]
    
    def _generateKeywordPattern(self, keywords):
        return '|'.join([k for k in keywords])




#tokens = Scanner().scan('324+ then*while: (ooif+ ; 23r3')


#tokens = Scanner().scan('if')
#print(tokens)

# p = 'if|then|else|endif|while|do|endwhile|skip'
# print(re.match(p, 'if').group())