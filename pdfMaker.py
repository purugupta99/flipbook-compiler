from PyPDF2 import PdfFileMerger
from fpdf import FPDF
import fitz # PyMuPDF
import io
from PIL import Image
import time

import os

class PDFMaker():

    def __init__(self, filename):
        '''
            Initialize PDF Maker Class
        '''
        self.statements = []
        self.instructions = {}
        self.maxPage = 0
        self.imageDir = "./images/"
        self.filename = filename
        
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

    def generate_PDF(self):
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

            pdfObj.output(self.filename, 'F')
            pdfMerger.append(self.filename)

            os.remove(self.filename)

        with open(self.filename, 'wb') as f:
            pdfMerger.write(f)

    def extract_images(self):
        pdf_file = fitz.open(self.filename)

        for page_index in range(len(pdf_file)):
            # get the page itself
            page = pdf_file[page_index]
            image_list = page.getImageList()
            # printing number of images found in this page
            if image_list:
                print(f"[+] Found a total of {len(image_list)} images in page {page_index}")
            else:
                print("[!] No images found on page", page_index)
            for image_index, img in enumerate(page.getImageList(), start=1):
                # get the XREF of the image
                xref = img[0]
                # extract the image bytes
                base_image = pdf_file.extractImage(xref)
                image_bytes = base_image["image"]
                # get the image extension
                image_ext = base_image["ext"]
                # load it to PIL
                image = Image.open(io.BytesIO(image_bytes))
                # save it to local disk
                image.save(open(f"image{page_index+1}_{image_index}.{image_ext}", "wb"))