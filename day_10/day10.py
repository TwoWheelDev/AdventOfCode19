with open("day10_input.txt", "r") as f:
    lines = f.readlines()


def generate_map(inp):
    y = 0
    ast_locs = []

    for line in lines:
        for x in range(len(line)):
            if line[x] == "#":
                ast_locs.append((x, y))
        y += 1

    return ast_locs

asteroids = generate_map(lines)
print("Asteroids", asteroids)
print("Number of asteroids", len(asteroids))
