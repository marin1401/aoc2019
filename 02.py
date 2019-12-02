#Day 2

with open('./02.txt') as myinput:
    inputlines = myinput.read().split(',')
inputlines = [int(line) for line in inputlines]

def program(original_input, x, y):
    a = original_input.copy()
    a[1] = x
    a[2] = y
    for i in range(0, len(a), 4):
        if a[i] == 1:
            a[a[3+i]] = a[a[1+i]]+a[a[2+i]]
        elif a[i] == 2:
            a[a[3+i]] = a[a[1+i]]*a[a[2+i]]
        else:
            break
    return a[0]

#Part 1
print(program(inputlines, 12, 2))

#Part 2
for x in range(100):
    for y in range(100):
        result = program(inputlines, x, y)
        if result == 19690720:
            print(100*x+y)
            break