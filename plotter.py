from board import mn_board as board

#getting input

r = 61
c = 61
origin = [r/2+1, c/2+1]

#getting the equation



def plot(graph, equation, start = -15, end = 15):

	equation = equation.replace('^', '**').lower()

	pairs = []
	#goin thru range
	for x in range(start, end+1):
		pairs.append([x, eval(equation.replace('x', str(x)))])


	#print pairs
	ytent = (r-1)/2
	xtent = (c-1)/2
	


	for each in pairs:
		if -1*xtent <= each[0] and each[0] <= xtent and -1*ytent <= each[1] and each[1] <= ytent:
			try:
				graph.put_at(origin[0] - each[1], origin[1] + each[0], 'X')
			except Exception:
				pass

	print 'Ordered pairs: \n'
	for each in pairs:
		print each,
	print '\n'
	graph.print_board()



while True:

	graph = board(r, c, ' ')
	for each in range(c):
		graph.put_at(r/2 + 1, each, '-')
	for each in range(r):
		graph.put_at(each, c/2 + 1, '|')
	graph.put_at(r/2 + 1, c/2 + 1, '+')


	equation = raw_input('Enter the equation in x: \ny = ')

	start = int(raw_input('Start at: '))
	end = int(raw_input('End at: '))
	plot(graph, equation, start, end)

	wait = raw_input()