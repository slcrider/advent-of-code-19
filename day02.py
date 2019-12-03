def run_int_code(intcode, noun, verb):
    pos = 0
    intcode[1] = noun
    intcode[2] = verb
    while True:
        if intcode[pos] == 1:
            intcode[intcode[pos + 3]] = intcode[intcode[pos + 2]] + intcode[intcode[pos + 1]]
        elif intcode[pos] == 2:
            intcode[intcode[pos + 3]] = intcode[intcode[pos + 2]] * intcode[intcode[pos + 1]]
        elif intcode[pos] == 99:
            return intcode[0]
        else:
            return -1
        pos += 4

if __name__ == '__main__':
    with open('day02.txt') as f:
        intcode = [int(code) for code in f.read().strip().split(',')]
    print(f'Answer 1: {run_int_code(intcode.copy(), 12, 2)}')
    print(f'Answer 1: {[100 * noun + verb for verb in range(100) for noun in range(100) if run_int_code(intcode.copy(), noun, verb) == 19690720][0]}')
