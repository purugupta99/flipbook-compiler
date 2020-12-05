from rply.token import BaseBox

# This module contains the class definitions of different types of AST nodes

class Integer(BaseBox):
    def __init__(self, value):
        self.value = value

    def eval(self):
        return int(self.value)

class Decimal(BaseBox):
    def __init__(self, value):
        self.value = value

    def eval(self):
        return float(self.value)

class ImageFile(BaseBox):
	def __init__(self, imageFile):
		self.imageFile = imageFile

	def eval(self):
		return self.imageFile

class Scale(BaseBox):
	def __init__(self, scaleValue):
		self.scaleValue = scaleValue

	def eval(self):
		return self.scaleValue

class Shift(BaseBox):
	def __init__(self, shiftX, shiftY):
		self.shiftX = shiftX
		self.shiftY = shiftY

	def eval(self):
		return self.shiftX, self.shiftY

class InitImage(BaseBox):
	def __init__(self, initX, initY, initSizeX, initSizeY):
		self.initX = initX
		self.initY = initY
		self.initSizeX = initSizeX
		self.initSizeY = initSizeY

	def eval(self):
		return self.initX, self.initY, self.initSizeX, self.initSizeY

class Loop(BaseBox):
	def __init__(self, startIdx, endIdx):
		self.startIdx = startIdx
		self.endIdx = endIdx

	def eval(self):
		return self.startIdx, self.endIdx

class Statement(BaseBox):
	def __init__(self, loop, init_image, scale, shift, image_file):
		self.loop = loop
		self.init_image = init_image
		self.scale = scale
		self.shift = shift
		self.image_file = image_file

	def eval(self):
		return [self.loop.eval(), self.init_image.eval(), self.scale.eval(), self.shift.eval(), self.image_file.eval()]