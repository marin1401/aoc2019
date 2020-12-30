#Day 2

with open('./02.txt') as myinput:
    inputlines = myinput.read().split(',')

intcode_program = [int(line) for line in inputlines]

def computer(intcode_program, noun, verb):
    ip = intcode_program.copy()
    ip[1] = noun
    ip[2] = verb
    for i in range(0, len(ip), 4):
        if ip[i] == 1:
            ip[ip[3+i]] = ip[ip[1+i]] + ip[ip[2+i]]
        elif ip[i] == 2:
            ip[ip[3+i]] = ip[ip[1+i]] * ip[ip[2+i]]
        elif ip[i] == 99:
            return ip[0]

#Part 1

print(computer(intcode_program, 12, 2))

#Part 2

def get_output(intcode_program, output):
    for noun in range(100):
        for verb in range(100):
            result = computer(intcode_program, noun, verb)
            if result == output:
                return 100 * noun + verb

print(get_output(intcode_program, 19690720))
