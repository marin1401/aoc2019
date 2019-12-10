#Day 08

with open('./08.txt') as myinput:
    imagelayers = myinput.read()

imagewidth = 25
imageheight = 6
imagesize = imagewidth*imageheight

#Part 1
layer_list = []
layers_list = []
counter = 0
number_of_zeros = []
for digit in range(len(imagelayers)):
    counter += 1
    layer_list.append(imagelayers[digit])
    if counter % imagesize == 0:
        layers_list.append(layer_list)
        number_of_zeros.append(layer_list.count('0'))
        layer_list = []
layer_num_with_fewest_zeros = number_of_zeros.index(min(number_of_zeros))
layer_with_fewest_zeros = layers_list[layer_num_with_fewest_zeros]
print(layer_with_fewest_zeros.count('1')* \
      layer_with_fewest_zeros.count('2'))

#Part 2
message = layers_list[len(layers_list)-1]
for each_layer in reversed(layers_list):
    for each_digit in range(len(each_layer)):
        if each_layer[each_digit] != '2':
            message[each_digit] = each_layer[each_digit]
message_joined = ''.join(message)
for line in range(0, len(message_joined), imagewidth):
    print(message_joined[line:line+imagewidth].replace('0', ' '))



            