#Day 03

with open('./03.txt') as myinput:
    wirepaths = myinput.read().split('\n')

wirepath_1 = wirepaths[0].split(',')
wirepath_2 = wirepaths[1].split(',')

def get_coords(wirepath):
    x, y = 0, 0
    coords = [(x, y)]
    for path in wirepath:
        if path[0] == 'R':
            x += int(path[1:])
            coords.append((x, y))
        elif path[0] == 'L':
            x -= int(path[1:])
            coords.append((x, y))
        elif path[0] == 'U':
            y += int(path[1:])
            coords.append((x, y))
        elif path[0] == 'D':
            y -= int(path[1:])
            coords.append((x, y))
    return coords

def in_range(num, r1, r2):
    return num in range(min(r1, r2), max(r1, r2))

w1c = get_coords(wirepath_1)
w2c = get_coords(wirepath_2)
intersections = set()
intersections_after_indices_in_paths, remaining_steps = [], []
for i in range(len(w1c) - 1):
    for j in range(1, len(w2c) - 1):
        if w1c[i][0] == w1c[i+1][0] and w2c[j][1] == w2c[j+1][1]:
            if in_range(w2c[j][1], w1c[i][1], w1c[i+1][1]) and in_range(w1c[i][0], w2c[j][0], w2c[j+1][0]):
                intersections.add((w1c[i][0], w2c[j][1]))
                intersections_after_indices_in_paths.append((i, j))
                remaining_steps.append((abs(w1c[i][1] - w2c[j][1]) + abs(w1c[i][0] - w2c[j][0])))
        elif w1c[i][1] == w1c[i+1][1] and w2c[j][0] == w2c[j+1][0]:
            if in_range(w2c[j][0], w1c[i][0], w1c[i+1][0]) and in_range(w1c[i][1], w2c[j][1], w2c[j+1][1]):
                intersections.add((w2c[j][0], w1c[i][1]))
                intersections_after_indices_in_paths.append((i, j))
                remaining_steps.append((abs(w1c[i][0] - w2c[j][0]) + abs(w1c[i][1] - w2c[j][1])))

#Part 1

distances = set()
for intersection in intersections:
    distances.add(abs(intersection[0]) + abs(intersection[1]))

print(min(distances))

#Part 2

steps = set()
for i in range(len(intersections_after_indices_in_paths)):
    wirestep_1, wirestep_2 = 0, 0
    for j in range(intersections_after_indices_in_paths[i][0]):
        wirestep_1 += int(wirepath_1[j][1:])
    for j in range(intersections_after_indices_in_paths[i][1]):
        wirestep_2 += int(wirepath_2[j][1:])
    steps.add(wirestep_1 + wirestep_2 + remaining_steps[i])

print(min(steps))
