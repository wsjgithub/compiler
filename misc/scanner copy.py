import re

class Scanner:
    def __init__(self):
        self.MARKS = {
            'identifier': 'IDENTIFIER',
            'number': 'NUMBER',
            'symbol':'SYMBOL'
        }
        self.symbols = ("+", "-", "*", "/", "(", ")",":")
        self.tokenTypes = ['identifier', 'number'] # exclude symbol
        self.patterns = {
            "identifier":"([a-z]|[A-Z])([a-z]|[A-Z]|[0-9])*",
            "number": '[0-9]+',
            "symbol": self._generateSymbolsPattern(self.symbols),
            "validChar": '[a-z]|[A-Z]|[0-9]|' + self._generateSymbolsPattern(self.symbols)
        }
        self.validCharPattern = '[a-z]|[A-Z]|[0-9]|\+|\-|\*|\/|\(|\)'
        self.whitespace = '\s'
        self.tokens = []
        self.currentToken = ''

    def scan(self, input):
        for ch in input:
            if self._isWhitespace(ch):
                self._parseToken()
                
            elif self._isSymbol(ch):
                self._parseToken()
                self.currentToken = ch
                self._parseSymbol()

            elif self._isValidChar(ch):
                self.currentToken += ch

            else:
                # continue
                raise Exception('Invalid character. Scanning aborted.')
        try:
            self._parseToken()
        except Exception as e:
            raise e
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
            if matched:
                longestMatchedToken = matched.group() if len(longestMatchedToken) < len(matched.group()) else longestMatchedToken
                longestMatchedTokenType = self.MARKS[type]
        if longestMatchedToken and longestMatchedTokenType:
            self.tokens.append((longestMatchedToken, longestMatchedTokenType))
            self.currentToken = self.currentToken[len(longestMatchedToken):]
            self._parseToken()
        else:
            raise Exception("Token doesn't match any pattern. Scanning aborted.")
        self.currentToken = ''

    def _isWhitespace(self, char):
        return re.fullmatch(self.whitespace, char)
    
    def _isSymbol(self, char):
        return re.fullmatch(self.patterns['symbol'], char)

    def _isValidChar(self, char):
        return re.fullmatch(self.validCharPattern,char)

    def _generateSymbolsPattern(self, symbols):
        return ''.join(["\\"+s+'|' for s in symbols])[:-1]







