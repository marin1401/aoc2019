#Day 08

with open('./08.txt') as myinput:
    image_layers = myinput.read()

image_width = 25
image_height = 6
image_size = image_width * image_height

#Part 1

layer, layers, zeros = [], [], []
counter = 0
for digit in image_layers:
    layer.append(digit)
    counter += 1
    if counter % image_size == 0:
        layers.append(layer)
        zeros.append(layer.count('0'))
        layer = []

layer_with_fewest_zeros = layers[zeros.index(min(zeros))]

print(layer_with_fewest_zeros.count('1') * layer_with_fewest_zeros.count('2'))

#Part 2

message = layers[-1]
for layer in reversed(layers):
    for digit in range(image_size):
        if layer[digit] != '2':
            message[digit] = layer[digit]
message = ''.join(message)
for line in range(0, image_size, image_width):
    print(message[line:line+image_width].replace('0', ' '))
