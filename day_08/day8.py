with open('day8_input.txt', 'r') as f:
    recv = f.read()
image = []
image_dim = 25*6
num_layers = int(len(recv) / image_dim)

while recv:
    image.append(recv[:image_dim])
    recv = recv[image_dim:]

zero_count = [x.count('0') for x in image]
minzero = zero_count.index(min(zero_count))

print(image[minzero].count('1') * image[minzero].count('2'))
