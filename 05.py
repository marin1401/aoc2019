#Day 2

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
