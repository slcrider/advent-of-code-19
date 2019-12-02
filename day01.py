from math import floor

def fuel_for_module(mass: int):
    """
    Returns the fuel necessary for the module
    """
    return floor(mass / 3) - 2


def fuel_for_module_and_fuel(mass: int):
    """
    Returns the fuel necessary for the module (based on mass) and its necessary fuel
    """
    fuel = fuel_for_module(mass)
    if fuel > 0:
        return fuel + fuel_for_module_and_fuel(fuel)
    return 0


if __name__ == '__main__':
    with open('day01.txt') as input:
        module_masses = [int(line.strip()) for line in input]
    print(f'Answer 1: {sum(fuel_for_module(module_mass) for module_mass in module_masses)}')
    print(f'Answer 2: {sum(fuel_for_module_and_fuel(module_mass) for module_mass in module_masses)}')
