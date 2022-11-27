with open('input.txt') as f:
    lines = f.read().splitlines()
print(lines)
pin = [
    [-1,-1,1,-1,-1],
    [-1,2,3,4,-1],
    [5,6,7,8,9],
    [-1,"A","B","C",-1],
    [-1,-1,"D",-1,-1],
]
pos=[0,2]
code = ""
for line in lines:
    for char in line:
        if char == "U" and pos[0]>0:
            if pin[pos[0]-1][pos[1]]!=-1:
                pos[0] -=1
        elif char == "D" and pos[0]<4:
            if pin[pos[0]+1][pos[1]]!=-1:
                pos[0] +=1
        elif char == "L" and pos[1]>0:
            if pin[pos[0]][pos[1]-1]!=-1:
                pos[1] -=1
        elif char == "R" and pos[1]<4:
            if pin[pos[0]][pos[1]+1]!=-1:
                pos[1] +=1
    code += str(pin[pos[0]][pos[1]])
print("part 2:",code)