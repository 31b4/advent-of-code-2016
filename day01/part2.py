with open('input.txt') as f:
    line = list(f.read().split(", "))

def Part2(line):
    d = [0,0,0,0]#N,E,S,W
    had_been=[]
    direction = 0
    for x in line:
        if x[0] == "R":
            direction = (direction+1)%4
        else:
            direction = (direction-1)%4
        for i in range(1, int(x[1:])+1):
            d[direction] += 1
            if not [d[0]-d[2],d[1]-d[3]] in had_been:
                had_been.append([d[0]-d[2],d[1]-d[3]])
            else:
                return(abs(d[0]-d[2])+abs(d[1]-d[3]))
print("part 2: ",Part2(line))