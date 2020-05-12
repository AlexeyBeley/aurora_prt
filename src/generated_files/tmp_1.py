def run(env):
    line = 0
    while True:
        if line == 0:
            env.set_register('R0', 1 + 1)
            line += 1
        elif line == 1:
            env.set_register('R1', env.get_register('R0') * env.get_register('R0'))
            line += 1
        elif line == 2:
            print(env.get_register('R0'))
            line += 1
        elif line == 3:
            print(env.get_register('R1'))
            line += 1
        else:
            return
