from aoc.intcomp import IntComp

computer = IntComp("day13_program.txt")
computer.run_program()
output = computer.get_output()

tiles = {}

i = 0
while i < len(output):
    pos = (output[i], output[i+1])
    tile_id = output[i+2]
    tiles[pos] = tile_id
    i += 3

block_tiles = sum(value == 2 for value in tiles.values())

print("Block tiles:", block_tiles)
