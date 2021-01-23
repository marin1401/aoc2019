#Day 6

with open('./06.txt') as myinput:
    inputlines = myinput.readlines()

orbits = [line.strip().split(')') for line in inputlines]

#Part 1

def count_orbits(current_object, counter, counters):
    counter += 1
    counters.append(counter)
    for object_1, object_2 in orbits:
        if current_object == object_1:
            count_orbits(object_2, counter, counters)

counters = []
count_orbits('COM', -1, counters)

print(sum(counters))

#Part 2

def required_orbital_transfers(current_object, orbit_map):
    for object_1, object_2 in orbits:
        if current_object == object_2:
            orbit_map.add(object_1)
            required_orbital_transfers(object_1, orbit_map)

orbit_map_san = set()
required_orbital_transfers('SAN', orbit_map_san)

orbit_map_you = set()
required_orbital_transfers('YOU', orbit_map_you)

print(len(orbit_map_san.symmetric_difference(orbit_map_you)))
