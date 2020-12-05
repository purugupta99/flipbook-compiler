from PyPDF2 import PdfFileMerger
from fpdf import FPDF

import os

class PDFMaker():

    def __init__(self):
        '''
            Initialize PDF Maker Class
        '''
        self.statements = []
        self.instructions = {}
        self.maxPage = 0
        self.imageDir = "./images/"
        
    def add_statement(self, statementNode):
        '''
            Add statement nodes to statement list
        '''
        self.statements.append(statementNode)

    def print_instructions(self):
        '''
            Print pdf generation instructions for debug
        '''
        for i in range(1, self.maxPage+1):
            print("\nPage Num: " + str(i))
            for instruction in self.instructions[i]:
                print(instruction)

    def generate_instructions(self):
        '''
            Generate pdf generation instructions for each page
        '''
        for statement in self.statements:
            valList = statement.eval()

            startIdx, endIdx = valList[0]
            x, y, szX, szY = valList[1]
            scaleVal = valList[2]
            shiftX, shiftY = valList[3]
            imageFile = valList[4]

            self.maxPage = max(self.maxPage, endIdx)

            for i in range(startIdx, endIdx+1):
                instruction = [x, y, szX, szY, imageFile]

                if i not in self.instructions:
                    self.instructions[i] = []

                self.instructions[i].append(instruction)

                x += shiftX
                y += shiftY
                szX = szX * scaleVal
                szY = szY * scaleVal

    def generate_PDF(self, filename):
        '''
            Generate PDF from the instructions created
        '''
        pdfMerger = PdfFileMerger()
        
        for i in range(1, self.maxPage+1):
            pdfObj = FPDF()
            pdfObj.add_page()

            for instruction in self.instructions[i]:
                x, y, szX, szY, imageFile = instruction
                pdfObj.image(self.imageDir + imageFile, x=x, y=y, w=szX, h=szY, type='', link='')

            pdfObj.output(filename, 'F')
            pdfMerger.append(filename)

            os.remove(filename)

        with open(filename, 'wb') as f:
            pdfMerger.write(f)