__authors__ = ['Andrew Taylor']

class TextWriter():

	font_5x7 = {
	" ": (0x00, 0x00, 0x00, 0x00, 0x00),
	"\"": (0x00, 0x07, 0x00, 0x07, 0x00), # "
	"#": (0x14, 0x7F, 0x14, 0x7F, 0x14), # #
	"$": (0x24, 0x2A, 0x7F, 0x2A, 0x12), # $
	"%": (0x23, 0x13, 0x08, 0x64, 0x62), # %
	"&": (	0x36, 0x49, 0x55, 0x22, 0x50), # &
	"'": (0x00, 0x05, 0x03, 0x00, 0x00), # '
	"(": (0x00, 0x1C, 0x22, 0x41, 0x00), # (
	")": (0x00, 0x41, 0x22, 0x1C, 0x00), # )
	"*": (0x08, 0x2A, 0x1C, 0x2A, 0x08), # *
	"+": (0x08, 0x08, 0x3E, 0x08, 0x08), # +
	",": (0x00, 0x50, 0x30, 0x00, 0x00), # ,
	"-": (0x08, 0x08, 0x08, 0x08, 0x08), # -
	".": (0x00, 0x60, 0x60, 0x00, 0x00), # .
	"/": (0x20, 0x10, 0x08, 0x04, 0x02), # /
	"0": (0x3E, 0x51, 0x49, 0x45, 0x3E), # 0
	"1": (0x00, 0x42, 0x7F, 0x40, 0x00), # 1
	"2": (0x42, 0x61, 0x51, 0x49, 0x46), # 2
	"3": (0x21, 0x41, 0x45, 0x4B, 0x31), # 3
	"4": (0x18, 0x14, 0x12, 0x7F, 0x10), # 4
	"5": (0x27, 0x45, 0x45, 0x45, 0x39), # 5
	"6": (0x3C, 0x4A, 0x49, 0x49, 0x30), # 6
	"7": (0x01, 0x71, 0x09, 0x05, 0x03), # 7
	"8": (0x36, 0x49, 0x49, 0x49, 0x36), # 8
	"9": (0x06, 0x49, 0x49, 0x29, 0x1E), # 9
	":": (0x00, 0x36, 0x36, 0x00, 0x00), # :
	";": (0x00, 0x56, 0x36, 0x00, 0x00), # ;
	"<": (0x00, 0x08, 0x14, 0x22, 0x41), # <
	"=": (0x14, 0x14, 0x14, 0x14, 0x14), # =
	">": (0x41, 0x22, 0x14, 0x08, 0x00), # >
	"?": (0x02, 0x01, 0x51, 0x09, 0x06), # ?
	"@": (0x32, 0x49, 0x79, 0x41, 0x3E), # @
	"A": (0x7E, 0x11, 0x11, 0x11, 0x7E), # A
	"B": (0x7F, 0x49, 0x49, 0x49, 0x36), # B
	"C": (0x3E, 0x41, 0x41, 0x41, 0x22), # C
	"D": (0x7F, 0x41, 0x41, 0x22, 0x1C), # D
	"E": (0x7F, 0x49, 0x49, 0x49, 0x41), # E
	"F": (0x7F, 0x09, 0x09, 0x01, 0x01), # F
	"G": (0x3E, 0x41, 0x41, 0x51, 0x32), # G
	"H": (0x7F, 0x08, 0x08, 0x08, 0x7F), # H
	"I": (0x00, 0x41, 0x7F, 0x41, 0x00), # I
	"J": (0x20, 0x40, 0x41, 0x3F, 0x01), # J
	"K": (0x7F, 0x08, 0x14, 0x22, 0x41), # K
	"L": (0x7F, 0x40, 0x40, 0x40, 0x40), # L
	"M": (0x7F, 0x02, 0x04, 0x02, 0x7F), # M
	"N": (0x7F, 0x04, 0x08, 0x10, 0x7F), # N
	"O": (0x3E, 0x41, 0x41, 0x41, 0x3E), # O
	"P": (0x7F, 0x09, 0x09, 0x09, 0x06), # P
	"Q": (0x3E, 0x41, 0x51, 0x21, 0x5E), # Q
	"R": (0x7F, 0x09, 0x19, 0x29, 0x46), # R
	"S": (0x46, 0x49, 0x49, 0x49, 0x31), # S
	"T": (0x01, 0x01, 0x7F, 0x01, 0x01), # T
	"U": (0x3F, 0x40, 0x40, 0x40, 0x3F), # U
	"V": (0x1F, 0x20, 0x40, 0x20, 0x1F), # V
	"W": (0x7F, 0x20, 0x18, 0x20, 0x7F), # W
	"X": (0x63, 0x14, 0x08, 0x14, 0x63), # X
	"Y": (0x03, 0x04, 0x78, 0x04, 0x03), # Y
	"Z": (0x61, 0x51, 0x49, 0x45, 0x43), # Z
	"[": (0x00, 0x00, 0x7F, 0x41, 0x41), # [
	"\\": (0x02, 0x04, 0x08, 0x10, 0x20), # "\"
	"]": (0x41, 0x41, 0x7F, 0x00, 0x00), # ]
	"^": (0x04, 0x02, 0x01, 0x02, 0x04), # ^
	"_": (0x40, 0x40, 0x40, 0x40, 0x40), # _
	"`": (0x00, 0x01, 0x02, 0x04, 0x00), # `
	"a": (0x20, 0x54, 0x54, 0x54, 0x78), # a
	"b": (0x7F, 0x48, 0x44, 0x44, 0x38), # b
	"c": (0x38, 0x44, 0x44, 0x44, 0x20), # c
	"d": (0x38, 0x44, 0x44, 0x48, 0x7F), # d
	"e": (0x38, 0x54, 0x54, 0x54, 0x18), # e
	"f": (0x08, 0x7E, 0x09, 0x01, 0x02), # f
	"g": (0x08, 0x14, 0x54, 0x54, 0x3C), # g
	"h": (0x7F, 0x08, 0x04, 0x04, 0x78), # h
	"i": (0x00, 0x44, 0x7D, 0x40, 0x00), # i
	"j": (0x20, 0x40, 0x44, 0x3D, 0x00), # j
	"k": (0x00, 0x7F, 0x10, 0x28, 0x44), # k
	"l": (0x00, 0x41, 0x7F, 0x40, 0x00), # l
	"m": (0x7C, 0x04, 0x18, 0x04, 0x78), # m
	"n": (0x7C, 0x08, 0x04, 0x04, 0x78), # n
	"o": (0x38, 0x44, 0x44, 0x44, 0x38), # o
	"p": (0x7C, 0x14, 0x14, 0x14, 0x08), # p
	"q": (0x08, 0x14, 0x14, 0x18, 0x7C), # q
	"r": (0x7C, 0x08, 0x04, 0x04, 0x08), # r
	"s": (0x48, 0x54, 0x54, 0x54, 0x20), # s
	"t": (0x04, 0x3F, 0x44, 0x40, 0x20), # t
	"u": (0x3C, 0x40, 0x40, 0x20, 0x7C), # u
	"v": (0x1C, 0x20, 0x40, 0x20, 0x1C), # v
	"w": (0x3C, 0x40, 0x30, 0x40, 0x3C), # w
	"x": (0x44, 0x28, 0x10, 0x28, 0x44), # x
	"y": (0x0C, 0x50, 0x50, 0x50, 0x3C), # y
	"z": (0x44, 0x64, 0x54, 0x4C, 0x44), # z
	"{": (0x00, 0x08, 0x36, 0x41, 0x00), # {
	"|": (0x00, 0x00, 0x7F, 0x00, 0x00), # |
	"}": (0x00, 0x41, 0x36, 0x08, 0x00), # }
	}

	def __init__(self):
		pass

	def draw_text(self, surface, text, colour, x_pos, y_pos):
		"""
		Draws text in the specified place, in the appropriate colour
		"""
		text_buffer = self.make_text(text)

		width = len(text_buffer)
		height = 0
		if (width > 0):
			height = len(text_buffer[0])

		# If surface is None, then we just return the size of the text, and
		#  not actually draw it
		if (surface != None):
			for x in range(0, len(text_buffer)):
				for y in range(0, len(text_buffer[x])):
					if (text_buffer[x][y] == 1):
						surface.draw_tuple_pixel(x+x_pos,y+y_pos, colour)

		return (width, height)

	def make_text(self, string):
		"""
		Construct a buffer that contains which pixels to draw (=1) to make text
		"""
		pixel_height = 7
		pixel_width = 5
	
		font_characters = []
	
		# Gap between each character
		space_padding = 1

		output_buffer = [[0 for y in range(0,pixel_height)] for x in range(0,(pixel_width+space_padding)*len(string))]

		#if (len(output_buffer) > 0):
		#	print "Output buffer size is %d x %d" % (len(output_buffer), len(output_buffer[0]))

		# For each character in the string, grab the array of pixels from the 
		#  5x7 font collection, and then insert the data into the output array
		character_number = 0
		for character in string:
			character_definition = self.font_5x7[character]
			font_characters.append(character_definition)
			if (character_definition != None):
				for x in range(0, len(character_definition)):
					for y in range(0, pixel_height):
						pixel_value = (character_definition[x] >> y) & 0x01
						output_buffer[character_number*(pixel_width+space_padding)+x][y] = pixel_value
			character_number += 1

		return output_buffer
