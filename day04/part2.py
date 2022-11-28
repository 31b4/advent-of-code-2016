from string import ascii_letters
with open('input.txt') as f:
    l = f.read().splitlines()


keys = [x.split('[') for x in l]
for i in range(len(keys)):
    keys[i][1] = keys[i][1][:-1]
    keys[i].append(keys[i][0][len(keys[i][0])-3:])
    keys[i][0] = keys[i][0][:len(keys[i][0])-4]
    
for x in keys:
    if (''.join([ascii_letters[(ascii_letters.index(c)+int(x[2]))%len(ascii_letters)] if c in ascii_letters else c for c in x[0]])).lower() == "northpole-object-storage":
        print("part 2:",x[2])
        break 