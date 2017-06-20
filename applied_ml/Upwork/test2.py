'''l = [4, 5, 16]
for i in l:
	y = 16*i*i - 25*i - 275
	print(i, y)'''
print([16*i*i - 25*i - 275 for i in (4, 5, 16)])