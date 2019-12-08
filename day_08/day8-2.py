from PIL import Image, ImageColor

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

dim = (25, 6)

img = Image.new("RGB", dim, color="Blue")
map = img.load()

for layer in image:
    pc = 0
    for row in range(img.size[1]):
        for col in range(img.size[0]):
            if map[col, row] == (0, 0, 255):
                if layer[pc] == '0':
                    map[col, row] = (0, 0, 0)
                elif layer[pc] == '1':
                    map[col, row] = (255, 255, 255)
            pc += 1

img.show()