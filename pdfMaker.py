from PyPDF2 import PdfFileMerger
from fpdf import FPDF

class PDFMaker():

    def __init__(self):
        self.statements = []
        
    def add_statement(self, statementNode):
        self.statements.append(statementNode)