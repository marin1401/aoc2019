#Day 09

with open('./09.txt') as myinput:
    input_lines = myinput.read().split(',')

intcode_program = [int(line) for line in input_lines]
outside_ip = {}

def value(ip, idx):
    if len(ip) < idx:
        return outside_ip[idx] if idx in outside_ip.keys() else 0
    else:
        return ip[idx]

def overwrite_ip(ip, opcode, parameter, position, rb, value):
    idx = ip[parameter] if opcode[position] == '0' else ip[parameter] + rb
    if opcode[position] == '1':
        ip[parameter] = value
    else:
        if len(ip) < idx:
            write_outside_ip(outside_ip, idx, value)
        else:
            ip[idx] = value

def write_outside_ip(outside_ip, idx, value):
    outside_ip[idx] = value

def computer(intcode_program, instruction, i):
    ip = intcode_program.copy()
    out = []
    first_pass = True
    rb = 0
    while ip[i] != 99:
        opcode = '0000' + str(ip[i])
        op = opcode[-2:]
        if op not in ['03']:
            idx = ip[i+1] + rb if opcode[-3] == '2' else ip[i+1]
            fp = idx if opcode[-3] == '1' else value(ip, idx)
            if op not in ['04']:
                idx = ip[i+2] + rb if opcode[-4] == '2' else ip[i+2]
                sp = idx if opcode[-4] == '1' else value(ip, idx)
        if op == '01':
            overwrite_ip(ip, opcode, i+3, -5, rb, fp + sp)
            i += 4
        elif op == '02':
            overwrite_ip(ip, opcode, i+3, -5, rb, fp * sp)
            i += 4
        elif op == '03':
            if first_pass:
                overwrite_ip(ip, opcode, i+1, -3, rb, instruction)
                first_pass = False
                i += 2
            else:
                break
        elif op == '04':
            out.append(fp)
            i += 2
        elif op == '05':
            i = sp if fp else i+3
        elif op == '06':
            i = sp if not fp else i+3
        elif op == '07':
            overwrite_ip(ip, opcode, i+3, -5, rb, 1 if fp < sp else 0)
            i += 4
        elif op == '08':
            overwrite_ip(ip, opcode, i+3, -5, rb, 1 if fp == sp else 0)
            i += 4
        elif op == '09':
            rb += fp
            i += 2
    if out:
        return out[-1], i, ip.copy()
    else:
        return instruction, i, ip.copy()

#Part 1

print(computer(intcode_program, 1, 0)[0])

#Part 2

print(computer(intcode_program, 2, 0)[0])