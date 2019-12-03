#Day 03

with open('./03.txt') as myinput:
    wirepaths = myinput.read().split('\n')
wirepath1 = wirepaths[0].split(',')
wirepath2 = wirepaths[1].split(',')

def wireprog(wirepath, x, y):
    for i in range(len(wirepath)):
        