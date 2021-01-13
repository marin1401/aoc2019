#Day 5

with open('./05.txt') as myinput:
    inputlines = myinput.read().split(',')

intcode_program = [int(line) for line in inputlines]

def overwrite_ip(ip, opcode, parameter, position, value):
    if opcode[position] == '1':
        ip[parameter] = value
    else:
        ip[ip[parameter]] = value

def computer(intcode_program, input_value):
    ip = intcode_program.copy()
    out = []
    i = 0
    while ip[i] != 99:
        opcode = '0000' + str(ip[i])
        op = opcode[-2:]
        if op not in ['03']:
            if opcode[-3] == '1':
                fp = ip[1+i]
            else:
                fp = ip[ip[1+i]]
            if op not in ['04']:
                if opcode[-4] == '1':
                    sp = ip[2+i]
                else:
                    sp = ip[ip[2+i]]
        if op == '01':
            overwrite_ip(ip, opcode, i+3, -5, fp + sp)
            i += 4
        elif op == '02':
            overwrite_ip(ip, opcode, i+3, -5, fp * sp)
            i += 4
        elif op == '03':
            overwrite_ip(ip, opcode, i+1, -3, input_value)
            i += 2
        elif op == '04':
            out.append(fp)
            i += 2
        elif op == '05':
            i = sp if fp else i+3
        elif op == '06':
            i = sp if not fp else i+3
        elif op == '07':
            overwrite_ip(ip, opcode, i+3, -5, 1 if fp < sp else 0)
            i += 4
        elif op == '08':
            overwrite_ip(ip, opcode, i+3, -5, 1 if fp == sp else 0)
            i += 4
    return out[-1]

#Part 1

print(computer(intcode_program, 1))

#Part 2

print(computer(intcode_program, 5))
