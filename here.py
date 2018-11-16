from board import mn_board as board

#getting input

r = 61
c = 61
origin = [r/2+1, c/2+1]

#getting the equation


def getcon(equation):
	config = []#main thing
	const = 0
	signs = []

	if equation[0] not in ['+', '-']: equation = '+'+equation

	for each in equation:
		if each in ['+', '-']: signs.append(each)

	equation = ' '.join(equation.split('+'))
	equation = ' '.join(equation.split('-'))
	equation = equation.split(' ')



	#clean up
	for each in equation:
		if not each: equation.remove(each)

	for each in range(len(equation)):
		if 'x' in equation[each]:
			sign = signs[each]
			coeff = equation[each].split('x')[0]
			power = equation[each].split('x')[1][1:]
			config.append([sign, coeff, power])
		else:
			const = int(signs[each] + equation[each])
	print config
	return [config, const]


#print getcon(equation)


def plot(graph, equation, start = -15, end = 15):

	equation = getcon(equation)
	config = equation[0]
	const = equation[1]
	#y = const

	pairs = []
	#goin thru range
	for x in range(start, end+1):
		y = 'no'
		xhere = 0
		#goin thru each term
		for each in config:
			sign = 1
			coeff=0
			power=0
			if each[0] == '-': sign = -1
			if each[1]:
				coeff = float(each[1])
			else:
				coeff = 1

			if each[2]:
				power = float(each[2])
			else:
				power = 1
			if not(x < 0 and isinstance(power, float)):
				y = const
				xhere = coeff*(x**power)*sign
				y += xhere
		pairs.append([x, y])
	print pairs
	ytent = (r-1)/2
	xtent = (c-1)/2
	
	print xtent, ytent


	for each in pairs:
		if -1*xtent <= each[0] and each[0] <= xtent and -1*ytent <= each[1] and each[1] <= ytent:
			try:
				graph.put_at(origin[0] - each[1], origin[1] + each[0], 'X')
			except Exception:
				pass

	graph.print_board()


h = True
while h:

	graph = board(r, c, ' ')
	for each in range(c):
		graph.put_at(r/2 + 1, each, '-')
	for each in range(r):
		graph.put_at(each, c/2 + 1, '|')
	graph.put_at(r/2 + 1, c/2 + 1, '+')


	equation = raw_input('Enter the equation in x: \ny = ')

	plot(graph, equation)
	h = False