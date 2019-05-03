tableData = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']]


k=0


for i in range(len(tableData)):
	for j in range(len(tableData[i])):
		if k < len(tableData[i][j]):
			  k=len(tableData[i][j])
			  

for i in range(len(tableData)):
	for j in range(len(tableData[i])):
		tableDataContent=tableData[i][j]
		print(tableDataContent.rjust(k,' '),end=' ')
	print()
