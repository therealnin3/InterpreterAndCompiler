from Token import Token, TokenType


class Lexer:
    def __init__(self, source):
        self.source = source + '\n'
        self.curChar = ''
        self.curPos = -1
        self.nextChar()

    # Process next char
    def nextChar(self):
        self.curPos += 1
        if (self.curPos >= len(self.source)):
            self.curChar = '\0'  # EOF
        else:
            self.curChar = self.source[self.curPos]

    # Return lookahead
    def peek(self):
        if (self.curPos + 1 >= len(self.source)):
            return '\0'
        else:
            return self.source[self.curPos + 1]

    # Invalid token, Error

    def abort(self, message):
        pass

    # Skip whitespaces, except newlines
    def skipWhitespace(self):
        pass

    # Skip comments
    def skipComment(self):
        pass

    # Return next token
    def getToken(self):
        if self.curChar == '+':
            token = Token(self.curChar, TokenType.PLUS)
        elif self.curChar == '-':
            token = Token(self.curChar, TokenType.MINUS)
        elif self.curChar == '*':
            token = Token(self.curChar, TokenType.ASTERISK)
        elif self.curChar == '/':
            token = Token(self.curChar, TokenType.SLASH)
        elif self.curChar == '\n':
            token = Token(self.curChar, TokenType.NEWLINE)
        elif self.curChar == '\0':
            token = Token('', TokenType.EOF)
        else:
            # Unknown token!
            pass

        self.nextChar()
        return token
