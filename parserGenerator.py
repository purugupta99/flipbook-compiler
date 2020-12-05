from rply import ParserGenerator
from astNode import *

class Parser():
    def __init__(self):
        '''
            Initialise the Parser Generator
        '''

        # Add tokens to be accepted by the parser 
        self.parser = ParserGenerator(
            ['EXEC', 'LOOP', 'INIT', 'SCALE', 'SHIFT', 'IMAGE_FILE', \
            'INTEGER', 'DECIMAL', 'LPAREN', 'RPAREN', 'COMMA']
        )

    def parse(self):
        '''
            Defines production rules accepted by the parser
        '''

        @self.parser.production('expression : EXEC LPAREN loop init_image scale shift image_file RPAREN')
        def expression(expr):
            return Statement(expr[2], expr[3], expr[4], expr[5], expr[6])

        @self.parser.production('loop : LOOP LPAREN INTEGER COMMA INTEGER RPAREN')
        def expression(expr):
            return Loop(Integer(expr[2].value).eval(), Integer(expr[4].value).eval())

        @self.parser.production('init_image : INIT LPAREN INTEGER COMMA INTEGER COMMA INTEGER COMMA INTEGER RPAREN')
        def expression(expr):
            return InitImage(Integer(expr[2].value).eval(), Integer(expr[4].value).eval(), Integer(expr[6].value).eval(), Integer(expr[8].value).eval())

        @self.parser.production('scale : SCALE LPAREN DECIMAL RPAREN')
        def expression(expr):
            return Scale(Decimal(expr[2].value).eval())

        @self.parser.production('shift : SHIFT LPAREN INTEGER COMMA INTEGER RPAREN')
        def expression(expr):
            return Shift(Integer(expr[2].value).eval(), Integer(expr[4].value).eval())

        @self.parser.production('image_file : IMAGE_FILE')
        def expression(expr):
            return ImageFile(expr[0].value)

        @self.parser.error
        def error_handle(token):
            raise ValueError(token)

    def make_parser(self):
        '''
            Returns the generated parser
        '''
        return self.parser.build()