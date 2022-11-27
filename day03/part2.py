with open('input.txt') as f:
    lines = f.read().splitlines()
numbers = [[int(n) for n in x.split()] for x in lines]
ans = 0

def Is_triangle(sides):
    a, b, c = sorted(sides)
    return a + b > c

for i in range(3):
    for j in range(0,len(numbers),3):
        if Is_triangle([numbers[j][i],numbers[j+1][i],numbers[j+2][i]]):
            ans+=1
print("part 2:",ans)        
