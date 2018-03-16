from functools import reduce
import sys

def list_prod(nums):
    return reduce(lambda x,y: x * y, nums)

grid = []
for grid_i in range(20):
   grid_t = [int(grid_temp) for grid_temp in input().strip().split(' ')]
   grid.append(grid_t)

largest = 0

for i in range(17):
    for j in range(20):
        
        down = list_prod([grid[i+x][j] for x in range(0,4)])
        right = 0
        down_and_right = 0
        down_and_left = 0
        
        if j < 17:
            right = list_prod(grid[i][j:j+4])
            down_and_right = list_prod([grid[i+x][j+x] for x in range(0,4)])
        
        if j > 2:
            down_and_left = list_prod([grid[i+x][j-x] for x in range(0,4)])
        
        #if 2 < j < 17:
            #right = list_prod(grid[i][j:j+4])
            #down_and_right = list_prod([grid[i+x][j+x] for x in range(0,4)])
            #down_and_left = list_prod([grid[i+x][j-x] for x in range(0,4)])
        
        #print(i,j,right)
        coordinate_max = max([down, right, down_and_right, down_and_left])   
        if coordinate_max > largest:
            largest = coordinate_max

for i in range(17,20):
    for j in range(17):
        right = list_prod(grid[i][j:j+4])
        if right > largest:
            largest = right
        
    
print(largest)