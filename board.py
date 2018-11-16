class mn_board(object):
	def __init__(self, r, c, lachar):
		self.r = r
		self.c = c
		self.lachar = str(lachar).upper()
		self.el_board = []
		for x in range(self.r):
			self.el_board.append([self.lachar]*self.c)
	#prints the board/matrix
	def print_board(self):
		for each in self.el_board:
			print ' '.join(each)
	#puts z at row x and column y
	def put_at(self, x, y, z):
		x = int(x)
		y = int(y)
		self.el_board[x-1][y-1] = z