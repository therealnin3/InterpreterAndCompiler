import sys
from textwrap import indent

from Token import Token, TokenType


class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.curToken = None
        self.peekToken = None
        self.nextToken()
        self.nextToken()
        pass

    def nextToken(self):
        self.curToken = self.peekToken
        self.peekToken = self.lexer.getToken()

    def checkToken(self, kind):
        return self.curToken.kind == kind

    def checkPeek(self, kind):
        return self.peekToken.kind == kind

    def abort(self, message):
        sys.exit("Error. " + message)

    def match(self, kind):
        if not self.checkToken(kind):
            self.abort("Expected " + kind.name +
                       ", got " + self.curToken.kind.name)
        self.nextToken()

    # GRAMMER
    # program ::= {statement}
    def program(self):
        print("PROGRAM")

        while self.checkToken(TokenType.NEWLINE):
            self.nextToken()

        while not self.checkToken(TokenType.EOF):
            self.statement()

    # nl ::= '\n'+
    def n1(self):
        print("NEWLINE")
        self.match(TokenType.NEWLINE)
        while self.checkToken(TokenType.NEWLINE):
            self.nextToken()

    # TODO:
    def expression(self):
        print("expression")
        pass

    # TODO:
    def comparison(self):
        print("comparison")
        pass

    # statement ::= "PRINT" (expression | string) nl
    # | "IF" comparison "THEN" nl {statement} "ENDIF" nl
    # | "WHILE" comparison "REPEAT" nl {statement} "ENDWHILE" nl
    # | "LABEL" ident nl
    # | "GOTO" ident nl
    # | "LET" ident "=" expression nl
    # | "INPUT" ident nl
    def statement(self):

        # "PRINT" (expression | string) nl
        if self.checkToken(TokenType.PRINT):
            print("STATEMENT-PRINT")
            self.nextToken()

            if self.checkToken(TokenType.STRING):
                self.nextToken()
                # TODO: string??
            else:
                self.expression()

        # "IF" comparison "THEN" nl {statement} "ENDIF" nl
        elif self.checkToken(TokenType.IF):
            print("STATEMENT-IF")
            self.nextToken()

            self.comparison()

            self.match(TokenType.THEN)
            self.n1()

            while not self.checkToken(TokenType.ENDIF):
                self.statement()

            self.match(TokenType.ENDIF)

        # "WHILE" comparison "REPEAT" nl {statement} "ENDWHILE" nl
        elif self.checkToken(TokenType.WHILE):
            print("STATEMENT-WHILE")
            self.nextToken()

            self.comparison()

            self.match(TokenType.REPEAT)
            self.n1()

            while not self.checkToken(TokenType.ENDWHILE):
                self.statement()

            self.match(TokenType.ENDWHILE)

        # "LABEL" ident nl
        elif self.checkToken(TokenType.LABEL):
            print("STATEMENT-LABEL")
            self.nextToken()
            self.match(TokenType.IDENT)
            pass

        # "GOTO" ident nl
        elif self.checkToken(TokenType.GOTO):
            print("STATEMENT-GOTO")
            self.nextToken()
            self.match(TokenType.IDENT)
            pass

        # "LET" ident "=" expression nl
        elif self.checkToken(TokenType.LET):
            print("STATEMENT-LET")
            self.nextToken()
            self.match(TokenType.IDENT)
            self.match(TokenType.EQ)
            self.expression()
            pass

        # "INPUT" ident nl
        elif self.checkToken(TokenType.INPUT):
            print("STATEMENT-INPUT")
            self.nextToken()
            self.match(TokenType.IDENT)
            pass
        else:
            self.abort("Invalid statement at " + self.curToken.text +
                       " (" + self.curToken.kind.name + ")")

        self.n1()
