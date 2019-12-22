from itertools import combinations
# <x=3, y=15, z=8>
# <x=5, y=-1, z=-2>
# <x=-10, y=8, z=2>
# <x=8, y=4, z=-5>

moons = [{"pos": {"x": 3, "y": 15, "z": 8}, "vel": {"x": 0, "y": 0, "z": 0}},
         {"pos": {"x": 5, "y": -1, "z": -2}, "vel": {"x": 0, "y": 0, "z": 0}},
         {"pos": {"x": -10, "y": 8, "z": 2}, "vel": {"x": 0, "y": 0, "z": 0}},
         {"pos": {"x": 8, "y": 4, "z": -5}, "vel": {"x": 0, "y": 0, "z": 0}}]
moon_pairs = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]


def timestep():
    apply_gravity()
    apply_velocity()


def apply_gravity():
    global moons
    for pair in moon_pairs:
        for axis in ("x", "y", "z"):
            if moons[pair[0]]["pos"][axis] == moons[pair[1]]["pos"][axis]:
                pass
            elif moons[pair[0]]["pos"][axis] < moons[pair[1]]["pos"][axis]:
                moons[pair[0]]["vel"][axis] += 1
                moons[pair[1]]["vel"][axis] -= 1
            elif moons[pair[0]]["pos"][axis] > moons[pair[1]]["pos"][axis]:
                moons[pair[0]]["vel"][axis] -= 1
                moons[pair[1]]["vel"][axis] += 1


def apply_velocity():
    global moons
    for moon in moons:
        for axis in ("x", "y", "z"):
            moon["pos"][axis] += moon["vel"][axis]


def calc_moon_energy():
    energy = []
    for moon in moons:
        pot = sum(abs(j) for j in moon['pos'].values())
        kin = sum(abs(k) for k in moon['vel'].values())
        energy.append(pot * kin)

    return sum(energy)


for x in range(1000):
    timestep()
tot_energy = calc_moon_energy()

print("Total energy:", tot_energy)
