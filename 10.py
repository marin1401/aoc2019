#Day 10

with open('./10.txt') as my_input:
    space = my_input.read().splitlines()

locations = []
y = 0
for row in space:
    x = 0
    for column in row:
        if column == '#':
            locations.append((x, y))
        x += 1
    y += 1

def direction(dx, dy):
    d = 0
    d = 1 if not dx and dy < 0 else d
    d = 2 if dx > 0 and dy < 0 else d
    d = 3 if not dy and dx > 0 else d
    d = 4 if dx > 0 and dy > 0 else d
    d = 5 if not dx and dy > 0 else d
    d = 6 if dx < 0 and dy > 0 else d
    d = 7 if not dy and dx < 0 else d
    d = 8 if dx < 0 and dy < 0 else d
    return d

#Part 1

intersections = set()
for (x0, y0) in locations:
    slopes = set()
    for (x1, y1) in locations:
        if (x0, y0) == (x1, y1):
            continue
        dx = x1-x0
        dy = y1-y0
        d = direction(dx, dy)
        if dx:
            slopes.add((d, dy/dx))
        else:
            slopes.add(d)
    intersections.add((len(slopes), (x0, y0)))

asteroids, (x0, y0) = max(intersections)

print(asteroids)

#Part 2

slopes = {k: [] for k in range(1, 9)}
for (x1, y1) in locations:
    if (x0, y0) == (x1, y1):
        continue
    dx = x1-x0
    dy = y1-y0
    d = direction(dx, dy)
    slope = dy/dx if dx else None
    slopes[d].append((slope, (x1, y1)))

for k, v in slopes.items():
    if k in (1, 7):
        slopes[k] = sorted(v, reverse=True)
    else:
        slopes[k] = sorted(v)

vaporized = []
while len(vaporized) < 299:
    for d in range(1, 9):
        slope = set()
        for s, (x1, y1) in slopes[d]:
            if s not in slope and (x1, y1) not in vaporized:
                vaporized.append((x1, y1))
                slope.add(s)
                if len(vaporized) == 200:
                    print(x1*100 + y1)