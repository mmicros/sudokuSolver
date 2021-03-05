#import numpy as np

grid = [[0,3,0,0,0,0,0,4,7],
	[9,0,0,7,0,2,0,8,0],
	[0,7,6,3,0,0,0,1,0],
	[0,8,0,9,0,0,1,0,0],
	[0,0,0,0,4,6,5,0,8],
	[0,6,9,0,2,0,0,0,0],
	[3,0,7,0,9,0,0,0,6],
	[8,0,4,0,0,7,0,0,0],
	[0,0,0,8,0,5,4,0,1]]

# check if we are allowed to enter integer 'n' 
# to position (x,y)
def valid(x,y,n):
	global grid
	#check row for conflicts
	for i in range(9):
		if grid[x][i]==n:
			return False
	#check column for conflicts
	for i in range(9):
		if grid[i][y]==n:
			return False
	#check square for conflicts
	sx = (x//3)*3 #first row of square
	sy = (y//3)*3 #first col of square
	for i in range(3):
		for j in range(3):
			if grid[sx+i][sy+j]==n:
				return False
	return True

x = int(input("enter x:"))
y = int(input("enter y:"))
n = int(input("enter n:"))
answer = valid(x,y,n)
print(f"you guess was {answer}")

