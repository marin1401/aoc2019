#Day 5

with open('./05.txt') as myinput:
    inputlines = myinput.read().split(',')
inputlines = [int(line) for line in inputlines]

def program(original_input, input_value):
    a = original_input.copy()
    b = input_value
    out = []
    j = 0
    for i in range(0, len(a)):
        if len(str(a[i+j])) == 1:
            if a[i+j] == 1:
                a[a[3+i+j]] = a[a[1+i+j]]+a[a[2+i+j]]
                j += 3
            elif a[i+j] == 2:
                a[a[3+i+j]] = a[a[1+i+j]]*a[a[2+i+j]]
                j += 3
            elif a[i+j] == 3:
                a[a[1+i+j]] = b
                j += 1
            elif a[i+j] == 4:
                out.append(a[a[1+i+j]])
                j += 1
            elif a[i+j] == 5:
                if a[a[1+i+j]] != 0:
                    j = a[a[2+i+j]]-i-1
                else:
                    j += 2
            elif a[i+j] == 6:
                if a[a[1+i+j]] == 0:
                    j = a[a[2+i+j]]-i-1
                else:
                    j += 2
            elif a[i+j] == 7:
                if a[a[1+i+j]] < a[a[2+i+j]]:
                    a[a[3+i+j]] = 1
                else:
                    a[a[3+i+j]] = 0
                j += 3
            elif a[i+j] == 8:
                if a[a[1+i+j]] == a[a[2+i+j]]:
                    a[a[3+i+j]] = 1
                else:
                    a[a[3+i+j]] = 0
                j += 3
            else:
                break
        elif len(str(a[i+j])) == 3:
            if str(a[i+j])[-1] == '1':
                a[a[3+i+j]] = a[1+i+j]+a[a[2+i+j]]
                j += 3
            elif str(a[i+j])[-1] == '2':
                a[a[3+i+j]] = a[1+i+j]*a[a[2+i+j]]
                j += 3
            elif str(a[i+j])[-1] == '4':
                out.append(a[1+i+j])
                j += 1
            elif str(a[i+j])[-1] == '5':
                if a[1+i+j] != 0:
                    j = a[a[2+i+j]]-i-1
                else:
                    j += 2
            elif str(a[i+j])[-1] == '6':
                if a[1+i+j] == 0:
                    j = a[a[2+i+j]]-i-1
                else:
                    j += 2
            elif str(a[i+j])[-1] == '7':
                if a[1+i+j] < a[a[2+i+j]]:
                    a[a[3+i+j]] = 1
                else:
                    a[a[3+i+j]] = 0
                j += 3
            elif str(a[i+j])[-1] == '8':
                if a[1+i+j] == a[a[2+i+j]]:
                    a[a[3+i+j]] = 1
                else:
                    a[a[3+i+j]] = 0
                j += 3
            else:
                break
        elif len(str(a[i+j])) == 4:
            if str(a[i+j])[-1] == '1':
                    if str(a[i+j])[-3] == '1':
                        a[a[3+i+j]] = a[1+i+j]+a[2+i+j]
                    else:
                        a[a[3+i+j]] = a[a[1+i+j]]+a[2+i+j]
                    j += 3
            elif str(a[i+j])[-1] == '2':
                    if str(a[i+j])[-3] == '1':
                        a[a[3+i+j]] = a[1+i+j]*a[2+i+j]
                    else:
                        a[a[3+i+j]] = a[a[1+i+j]]*a[2+i+j]
                    j += 3 
            elif str(a[i+j])[-1] == '5':
                    if str(a[i+j])[-3] == '1':
                        if a[1+i+j] != 0:
                            j = a[2+i+j]-i-1
                        else:
                            j += 2
                    else:
                        if a[a[1+i+j]] != 0:
                            j = a[2+i+j]-i-1
                        else:
                            j += 2
            elif str(a[i+j])[-1] == '6':
                    if str(a[i+j])[-3] == '1':
                        if a[1+i+j] == 0:
                            j = a[2+i+j]-i-1
                        else:
                            j += 2
                    else:
                        if a[a[1+i+j]] == 0:
                            j = a[2+i+j]-i-1
                        else:
                            j += 2
            elif str(a[i+j])[-1] == '7':
                    if str(a[i+j])[-3] == '1':
                        if a[1+i+j] < a[2+i+j]:
                            a[a[3+i+j]] = 1
                        else:
                            a[a[3+i+j]] = 0
                    else:
                        if a[a[1+i+j]] < a[2+i+j]:
                            a[a[3+i+j]] = 1
                        else:
                            a[a[3+i+j]] = 0
                    j += 3
            elif str(a[i+j])[-1] == '8':
                    if str(a[i+j])[-3] == '1':
                        if a[1+i+j] == a[2+i+j]:
                            a[a[3+i+j]] = 1
                        else:
                            a[a[3+i+j]] = 0
                    else:
                        if a[a[1+i+j]] == a[2+i+j]:
                            a[a[3+i+j]] = 1
                        else:
                            a[a[3+i+j]] = 0
                    j += 3
            else:
                break
        else:
            break
    return out[-1]

#Part 1
print(program(inputlines, 1))

#Part 2
print(program(inputlines, 5))

#Day 5

with open('./05.txt') as myinput:
    inputlines = myinput.read().split(',')

intcode_program = [int(line) for line in inputlines]

def computer(intcode_program, input_value):
    ip = intcode_program.copy()
    out = []
    i = 0
    while ip[i] != 99:
        opcode = '0000' + str(ip[i])
        if opcode[-1] == '1' or opcode[-1] == '2':
            if opcode[-3] == '1':
                fp = ip[1+i]
            else:
                fp = ip[ip[1+i]]
            if opcode[-4] == '1':
                sp = ip[2+i]
            else:
                sp = ip[ip[2+i]]
            if opcode[-5] == '1':
                if opcode[-1] == '1':
                    ip[3+i] = fp + sp
                elif opcode[-1] == '2':
                    ip[3+i] = fp * sp
            else:
                if opcode[-1] == '1':
                    ip[ip[3+i]] = fp + sp
                elif opcode[-1] == '2':
                    ip[ip[3+i]] = fp * sp
            i += 4
        elif opcode[-1] == '3':
            ip[ip[1+i]] = input_value
            i += 2
        elif opcode[-1] == '4':
            out.append(ip[ip[1+i]])
            i += 2
    return out[-1]

print(computer(intcode_program, 1))
