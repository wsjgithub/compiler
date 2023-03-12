# Shengjiao Wang, Raymond Lee
# 1.2

import re
from .constants import MARKS, SYMBOLS, KEYWORDS

class Scanner:
    def __init__(self):
        self.MARKS = MARKS
        self.symbols = SYMBOLS
        self.keywords = KEYWORDS
        self.tokenTypes = ['keyword', 'identifier', 'number', 'symbol',] 
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
        self._parseToken()
        return self.tokens

    def _parseSymbol(self): # not used
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
            self.tokens.append((self.currentToken, self.MARKS['error'])) # error token type
        self.currentToken = ''

    def _isWhitespace(self, char):
        return re.fullmatch(self.whitespace, char)
    
    def _isSymbol(self, char):
        return re.fullmatch(self.patterns['symbol'], char)

    def _isValidChar(self, char): # not used
        return re.fullmatch(self.validCharPattern,char)

    def _generateSymbolsPattern(self, symbols):
        return ''.join(["\\"+s+'|' for s in symbols])[:-1]
    
    def _generateKeywordPattern(self, keywords):
        return '|'.join([k for k in keywords])




# tokens = Scanner().scan('324+ then*while: (ooif+ ; 23r3')
# print(tokens)

#tokens = Scanner().scan('if')
#print(tokens)

# p = 'if|then|else|endif|while|do|endwhile|skip'
# print(re.match(p, 'if').group())