with open('input.txt') as f:
    line = list(f.read().split(", "))

d = [0,0,0,0]#N,E,S,W

direction = 0
for x in line:
    if x[0] == "R":
        direction = (direction+1)%4
    else:
        direction = (direction-1)%4
    d[direction] += int(x[1:])
print("part 1: ",abs(d[0]-d[2])+abs(d[1]-d[3]))    
