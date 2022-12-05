file = open('input.txt', 'r')
calories = []
new_list = []
total = 0
for line in file:
	if line != '\n':
		calories.append(int(line))
	else:
		calories.append(0)
calories.append(0)
for i in calories:
	if i != 0:
		total+=i
	else:
		new_list.append(total)
		total = 0
new_list.sort(reverse=True)
topthree = 0
for i in range(3):
	topthree+=new_list[i]
print(topthree)