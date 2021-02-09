#Day 7

import itertools

with open('./07.txt') as myinput:
    inputlines = myinput.read().split(',')

intcode_program = [int(line) for line in inputlines]

def overwrite_ip(ip, opcode, parameter, position, value):
    if opcode[position] == '1':
        ip[parameter] = value
    else:
        ip[ip[parameter]] = value

def computer(intcode_program, instruction, i):
    ip = intcode_program.copy()
    out = []
    first_pass = True
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
            if first_pass:
                overwrite_ip(ip, opcode, i+1, -3, instruction)
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
            overwrite_ip(ip, opcode, i+3, -5, 1 if fp < sp else 0)
            i += 4
        elif op == '08':
            overwrite_ip(ip, opcode, i+3, -5, 1 if fp == sp else 0)
            i += 4
    if out:
        return out[-1], i, ip.copy()
    else:
        return instruction, i, ip.copy()

#Part 1

all_phase_settings = list(itertools.permutations((0, 1, 2, 3, 4)))

thruster_signals = set()

for phase_settings in all_phase_settings:
    output = 0
    for phase_setting in phase_settings:
        *_, i, ip_bak = computer(intcode_program, phase_setting, 0)
        output, *_ = computer(ip_bak, output, i)
    thruster_signals.add(output)

print(max(thruster_signals))

#Part 2

all_phase_settings = list(itertools.permutations((5, 6, 7, 8, 9)))

thruster_signals = set()

i_ = [None for _ in range(5)]
ip_ = i_.copy()
output_ = i_.copy()

for phase_settings in all_phase_settings:
    for amp in range(5):
        *_, i_[amp], ip_[amp] = computer(intcode_program, phase_settings[amp], 0)
    output_[4] = 0
    while ip_[4][i_[4]] != 99:
        for amp in range(5):
            prev_amp = 4 if amp == 0 else amp - 1
            output_[amp], i_[amp], ip_[amp] = computer(ip_[amp], output_[prev_amp], i_[amp])
    thruster_signals.add(output_[4])

print(max(thruster_signals))