from rply import LexerGenerator

class Lexer():
    def __init__(self):
        '''
            Initialise Lexer Generator
        '''
        self.lexer = LexerGenerator()

    def _init_tokens(self):
        '''
            Define various tokens supported by the flip language
            Tokens follow camel case
        '''

        # Executes statement
        self.lexer.add('EXEC', r'exec')

        # Loop over pages
        self.lexer.add('LOOP', r'for')

        # Initial position and size
        self.lexer.add('INIT', r'initImage')

        # Scale image
        self.lexer.add('SCALE', r'scale')

        # Shift image
        self.lexer.add('SHIFT', r'shift')

        # Input image file - <filename> + '.' + <extension>
        self.lexer.add('IMAGE_FILE', r'[^\s]+(\.(?i)(jpg|jpeg|png|bmp))')

        # Decimal
        self.lexer.add('DECIMAL', r'\d+[.]\d+')

        # Integer
        self.lexer.add('INTEGER', r'\d+')

        # Left Parenthesis
        self.lexer.add('LPAREN', r'\(')

        # Right Parenthesis
        self.lexer.add('RPAREN', r'\)')

        # Comma
        self.lexer.add('COMMA', r'\,')

        # Ignore spaces
        self.lexer.ignore('\s+')

    def make_lexer(self):
        '''
            Returns the generated lexer
        '''
        self._init_tokens()
        return self.lexer.build()