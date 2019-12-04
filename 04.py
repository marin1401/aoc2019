#Day 04

lower_limit = 246540
upper_limit = 787419

#Part 1
numbers = lower_limit-1
candidates = set()
for i in range(lower_limit, upper_limit):
    numbers += 1
    numbers_str = str(numbers)
    if numbers_str[0]<=numbers_str[1]<=numbers_str[2]<= \
       numbers_str[3]<=numbers_str[4]<=numbers_str[5]:
           for j in range(5):
               if numbers_str[j]==numbers_str[j+1]:
                   candidates.add(numbers)
print(len(candidates))