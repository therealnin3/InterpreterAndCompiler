from Lexer import Lexer
from Token import TokenType


def main():

    with open('Input.txt', 'r') as file:
        content = file.read()

    # CREATE LEXER
    lexer = Lexer(content)

    # LOOP THROUGH FILE
    token = lexer.getToken()
    while (token != TokenType.EOF):
        print(token.tokenKind)
        lexer.getToken()


main()
