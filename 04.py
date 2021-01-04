#Day 04

with open('./04.txt') as myinput:
    limits = myinput.read()

lower_limit, upper_limit = map(int, limits.split('-'))

candidates_1 = set()
candidates_2 = set()
for i in range(lower_limit, upper_limit):
    n = str(i)
    if n[0] <= n[1] <= n[2] <= n[3] <= n[4] <= n[5]:
        for current_digit, next_digit in zip(n, n[1:]):
            if current_digit == next_digit:
                candidates_1.add(n)
                if n.count(current_digit) == 2:
                    candidates_2.add(n)

#Part 1

print(len(candidates_1))

#Part 2

print(len(candidates_2))
