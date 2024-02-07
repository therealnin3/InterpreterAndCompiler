from curses.ascii import isdigit
from pickle import NONE
import sys
from unittest import skip
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
        sys.exit("Lexing error. " + message)

    # Skip whitespaces, except newlines
    def skipWhitespace(self):
        while (self.curChar == ' ' or self.curChar == '\t' or self.curChar == '\r'):
            self.nextChar()

    # Skip comments
    def skipComment(self):
        if self.curChar == '#':
            while self.curChar != '\n':
                self.nextChar()

    # Return next token
    def getToken(self):

        self.skipWhitespace()
        self.skipComment()
        token = None

        # PLUS +
        if self.curChar == '+':
            token = Token(self.curChar, TokenType.PLUS)

        # MINUS -
        elif self.curChar == '-':
            token = Token(self.curChar, TokenType.MINUS)

        # ASTERISK *
        elif self.curChar == '*':
            token = Token(self.curChar, TokenType.ASTERISK)

        # SLASH /
        elif self.curChar == '/':
            token = Token(self.curChar, TokenType.SLASH)

        # EQ = OR EQEQ ==
        elif self.curChar == '=':
            # EQEQ ==
            if self.peek() == '=':
                lastChar = self.curChar
                self.nextChar()
                token = Token(lastChar + self.curChar, TokenType.EQEQ)
            # EQ =
            else:
                token = Token(self.curChar, TokenType.EQ)

        # GT > OR GTEQ >=
        elif self.curChar == '>':
            # GTEQ >=
            if self.peek() == '=':
                lastChar = self.curChar
                self.nextChar()
                token = Token(lastChar + self.curChar, TokenType.GTEQ)
            # GT >
            else:
                token = Token(self.curChar, TokenType.GT)

        # LT < OR LTEQ <=
        elif self.curChar == '<':
            # LTEQ >=
            if self.peek() == '=':
                lastChar = self.curChar
                self.nextChar()
                token = Token(lastChar + self.curChar, TokenType.LTEQ)
            # LT >
            else:
                token = Token(self.curChar, TokenType.LT)

        # NOTEQ !
        elif self.curChar == '!':
            if self.peek() == '=':
                lastChar = self.curChar
                self.nextChar()
                token = Token(lastChar + self.curChar, TokenType.NOTEQ)
            else:
                return self.abort("Expected !=, got !" + self.peek())

        # STRING "{string}"
        elif self.curChar == '\"':
            self.nextChar()
            startPos = self.curPos

            while self.curChar != '\"':
                if self.curChar == '\r' or self.curChar == '\n' or self.curChar == '\t' or self.curChar == '\\' or self.curChar == '%':
                    self.abort("Illegal character in string.")
                self.nextChar()

            text = self.source[startPos:self.curPos]  # End is not included!
            token = Token(text, TokenType.STRING)

        # NUMBER {int}.{int}
        elif self.curChar.isdigit():

            startPos = self.curPos

            while self.curChar.isdigit():
                self.nextChar()
            if self.curChar == '.':
                if not self.peek().isdigit:
                    self.abort("Illegal character in number.")
                else:
                    self.nextChar()
                    while self.curChar.isdigit():
                        self.nextChar()

            digit = self.source[startPos:self.curPos]
            token = Token(digit, TokenType.NUMBER)

        # NEW LINE \n
        elif self.curChar == '\n':
            token = Token(self.curChar, TokenType.NEWLINE)

        # EOF \0
        elif self.curChar == '\0':
            token = Token('', TokenType.EOF)

        # UNKNOWN TOKEN
        else:
            self.abort("Unknown token: " + self.curChar)

        self.nextChar()
        return token
