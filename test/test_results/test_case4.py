def run(env):
    line = 0
    while True:
        if line == 0:
            env.set_register('R0', 1)
            line += 1
        elif line == 1:
            env.set_register('R1', env.get_register('R0'))
            line += 1
        elif line == 2:
            env.set_register('R2', env.get_register('R1') + 1)
            line += 1
        elif line == 3:
            env.set_register('R3', 1 + env.get_register('R2'))
            line += 1
        elif line == 4:
            env.set_register('R4', env.get_register('R2') * env.get_register('R1'))
            line += 1
        else:
            return
