#Day 01

def fuel_calc(x):
    return int(x)//3-2

#Part 1
with open('./01.txt') as myinput:
    inputlines = myinput.readlines()
    fuel_required = 0
    for line in inputlines:
        fuel_required += fuel_calc(line)
    print (fuel_required)

#Part 2
    total_fuel = 0
    for line in inputlines:
        fuel_required_for_each_module = 0
        fuel_required = fuel_calc(line)
        while fuel_required >= 0:
            fuel_required_for_each_module += fuel_required
            fuel_required = fuel_calc(fuel_required)
        total_fuel += fuel_required_for_each_module
    print (total_fuel)