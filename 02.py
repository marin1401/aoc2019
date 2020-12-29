#Day 2

with open('./02.txt') as myinput:
    inputlines = myinput.read().split(',')

inputlines = [int(line) for line in inputlines]

def Intcode(original_input, x, y):
    a = original_input.copy()
    a[1] = x
    a[2] = y
    for i in range(0, len(a), 4):
        if a[i] == 1:
            a[a[3+i]] = a[a[1+i]] + a[a[2+i]]
        elif a[i] == 2:
            a[a[3+i]] = a[a[1+i]] * a[a[2+i]]
    return a[0]

#Part 1

print(Intcode(inputlines, 12, 2))

#Part 2

def get_output(output, inputlines):
    for noun in range(100):
        for verb in range(100):
            result = Intcode(inputlines, noun, verb)
            if result == output:
                return 100 * noun + verb

print(get_output(19690720, inputlines))
