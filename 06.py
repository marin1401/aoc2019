#Day 6

with open('./06.txt') as myinput:
    inputlines = myinput.readlines()

#Part 1    
def count_orbits(obj, counter_a, counter_b):
    counter_a += 1
    counter_b.append(counter_a)
    for line in inputlines:
        if obj == line[:3]:
            count_orbits(line[4:7], counter_a, counter_b)

counter_a = -1
counter_b = []
count_orbits('COM', counter_a, counter_b)
print(sum(counter_b))

#Part 2
def orbital_transfers_req(obj, orbit_map):
    for line in inputlines:
        if obj == line[4:7]:
            orbit_map.add(line[:3])
            orbital_transfers_req(line[:3], orbit_map)

orbit_map_san = set()
orbital_transfers_req('SAN', orbit_map_san)

orbit_map_you = set()
orbital_transfers_req('YOU', orbit_map_you)

print(len(orbit_map_san.symmetric_difference(orbit_map_you)))