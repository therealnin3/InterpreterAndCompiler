from Lexer import Lexer
from Parser import Parser


def main():

    # OPEN FILE
    with open('Input.tt', 'r') as file:
        content = file.read()

    # CREATE LEXER
    lexer = Lexer(content)

    # CREATE PARSER
    parser = Parser(lexer)

    print("> Tiny Compiler.")
    parser.program()
    print("> Parse completed.")


main()
