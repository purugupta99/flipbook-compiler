from lexerGenerator import Lexer
from parserGenerator import Parser
from pdfMaker import PDFMaker

import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

pdfMaker = PDFMaker()

with open(input_file) as f:
    lines = f.read().splitlines()

    for line in lines:
        lexer = Lexer().make_lexer()
        tokens = lexer.lex(line)

        parserObj = Parser()
        parserObj.parse()

        parser = parserObj.make_parser()
        node = parser.parse(tokens)

        pdfMaker.add_statement(node)