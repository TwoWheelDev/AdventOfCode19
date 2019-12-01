import math


def calcfuel(mass):
    fuel_required = math.floor(mass / 3) - 2
    return fuel_required


allModules = []

fh = open("day1_input", 'r')
masses = fh.readlines()

for mass in masses:
    allModules.append(calcfuel(int(mass)))

additional_fuel = []
for module_fuel in allModules:
    extra_fuel = 0
    while True:
        fuel_required = calcfuel(module_fuel)
        if fuel_required <= 0:
            fuel_required = 0

        extra_fuel += fuel_required
        module_fuel = fuel_required

        if module_fuel <= 0:
            additional_fuel.append(extra_fuel)
            break

totalFuel = sum(allModules) + sum(additional_fuel)

print("The total fuel required is:", totalFuel)