from aoc.intcomp import IntComp
from collections import defaultdict
from PIL import Image

x, y = 40, 40
xmin, xmax, ymin, ymax = 30, 30, 30, 30
direction = 'U'
panel = defaultdict(int)
panel[(40, 40)] = 1


def main():
    computer = IntComp("day11_input.txt", debug=False)
    computer.run_program([0])
    output = []
    while computer.state == 'RUN':
        output.clear()
        output = computer.get_output()[:]
        computer.clear_output()
        new_input = [process_output(output)]
        computer.run_program(new_input)

    print(len(panel))

    dim = (xmax+10, ymax+10)

    img = Image.new("RGB", dim, color="Blue")
    imap = img.load()

    for pixel in panel:
        if panel[pixel]:
            colour = (255, 255, 255)
        else:
            colour = (0, 0, 0)

        imap[pixel[1], pixel[0]] = colour
    img.show()


def process_output(output):
    global direction, x, y, xmin, xmax, ymin, ymax

    if output[0] == 0:
        panel[(x, y)] = 0  # Black
    else:
        panel[(x, y)] = 1  # White

    if output[1] == 0:
        if direction == 'U':
            direction = 'L'
            y -= 1
        elif direction == 'D':
            direction = 'R'
            y += 1
        elif direction == 'L':
            direction = 'D'
            x -= 1
        elif direction == 'R':
            direction = 'U'
            x += 1
    elif output[1] == 1:
        if direction == 'U':
            direction = 'R'
            y += 1
        elif direction == 'D':
            direction = 'L'
            y -= 1
        elif direction == 'L':
            direction = 'U'
            x += 1
        elif direction == 'R':
            direction = 'D'
            x -= 1

        if x > xmax:
            xmax = x
        if x < xmin:
            xmin = x
        if y > ymax:
            ymax = y
        if y < ymin:
            ymin = y

    return panel[(x, y)]


if __name__ == "__main__":
    main()
