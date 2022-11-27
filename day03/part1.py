with open('input.txt') as f:
    lines = f.read().splitlines()
numbers = [[int(n) for n in x.split()] for x in lines]
ans = 0
for triangle in numbers:
    a, b, c = sorted(triangle)
    if a+b>c:
        ans+=1
print("part 1:",ans)        
