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
print(max(new_list))