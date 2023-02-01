x = 1
y = 1
print(x,y)

delta = [(-1,0),(1,0),(0,-1),(0,1)]

for dx,dy in delta:
    print(x + dx, y + dy)
