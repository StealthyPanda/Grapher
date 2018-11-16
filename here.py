from board import mn_board as board

#getting input
"""r = int(raw_input('Enter rows: '))
c = int(raw_input('Enter cols: '))"""
r = 51
c = 51
origin = [r/2+1, c/2+1]


#init stuff
graph = board(r, c, ' ')
for each in range(c):
	graph.put_at(r/2 + 1, each, '-')
for each in range(r):
	graph.put_at(each, c/2 + 1, '|')
graph.put_at(r/2 + 1, c/2 + 1, '+')

#getting the equation

equation = raw_input('Enter the equation in x: \n')

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

	return [config, const]


print getcon(equation)


def plot(equation, start = -10, end = 10):

	equation = getcon(equation)
	config = equation[0]
	const = equation[1]
	#y = const

	pairs = []
	#goin thru range
	for x in range(start, end+1):
		y = const
		#goin thru each term
		for each in config:
			sign = 1
			coeff=0
			power=0
			if sign == '-': sign = -1
			if each[1]:
				coeff = int(each[1])
			else:
				coeff = 1

			if each[2]:
				power = int(each[2])
			else:
				power = 1

			xhere = coeff*(x**power)*sign
			y += xhere
		pairs.append([x, y])

	for each in pairs:
		graph.put_at(origin[1]-each[0], origin[0]+each[1], 'X')

	graph.print_board()


plot(equation)






#printing the graph
#graph.print_board()

