with open('input.txt') as f:
    l = f.read().splitlines()

keys = [x.split('[') for x in l]
for i in range(len(keys)):
    keys[i][1] = keys[i][1][:-1]
    keys[i].append(keys[i][0][len(keys[i][0])-3:])
    keys[i][0] = keys[i][0][:len(keys[i][0])-4]
    
sum = 0
for x in keys:
    letters = {}
    for c in x[0]:
        if c != '-':
            if c in letters.keys():
                letters[c] +=1
            else:
                letters[c] = 1
    letters = dict(sorted(letters.items()))
    most_keys = "".join(dict(sorted(letters.items(), key=lambda item: item[1],reverse=True)).keys())
    most_keys = most_keys[:5]
    print(most_keys)
    if most_keys == x[1]:
        sum += int(x[2])
        
print("part 1:",sum)