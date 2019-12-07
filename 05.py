#Day 2

with open('./05.txt') as myinput:
    inputlines = myinput.read().split(',')
inputlines = [int(line) for line in inputlines]

def program(original_input, inputval):
    a = original_input.copy()
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
                a[a[1+i+j]] = inputval
                j += 1
            elif a[i+j] == 4:
                out.append(a[a[1+i+j]])
                j += 1
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
                out.append(a[a[1+i+j]])
                j += 1
            else:
                break
        elif len(str(a[i+j])) == 4:
            if str(a[i+j])[-1] == '1':
                if str(a[i+j])[-4] == '1':
                    if str(a[i+j])[-3] == '1':
                        a[a[3+i+j]] = a[1+i+j]+a[2+i+j]
                    else:
                        a[a[3+i+j]] = a[a[1+i+j]]+a[2+i+j]
                    j += 3
            elif str(a[i+j])[-1] == '2':
                if str(a[i+j])[-4] == '1':
                    if str(a[i+j])[-3] == '1':
                        a[a[3+i+j]] = a[1+i+j]*a[2+i+j]
                    else:
                        a[a[3+i+j]] = a[a[1+i+j]]*a[2+i+j]
                    j += 3 
            else:
                break
        else:
            break
    return out

#Part 1
print(program(inputlines, 1)[-1])

#Part 2
