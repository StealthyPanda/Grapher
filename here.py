from board import mn_board as board

#getting input
r = int(raw_input('Enter rows: '))
c = int(raw_input('Enter cols: '))
origin = [r/2+1, c/2+1]


#init stuff
graph = board(r, c, 'O')
for each in range(c):
	graph.put_at(r/2 + 1, each, '-')
for each in range(r):
	graph.put_at(each, c/2 + 1, '|')
graph.put_at(r/2 + 1, c/2 + 1, '+')

#getting the equation

equation = raw_input('Enter the equation in x: \n')
config = []

for each in range(len(equation)):

	sign = '+'
	coeff = 0
	power = 0
		


	if each != 0:

		if not equation[each].isalpha() and equation[each] not in ['+', '-']:
			try:
				equation[each-1]
			except IndexError:
				pass
			else:
				sign = equation[each-1]
			coeff = int(equation[each])
			try:
				equation[each+1]
			except IndexError:
				power = 1
			else:
				if equation[each+1] == '^':
					power = int(equation[each+2])

		config.append([sign, coeff, power])

	else:

		config.append()


print config











#printing the graph
#graph.print_board()

