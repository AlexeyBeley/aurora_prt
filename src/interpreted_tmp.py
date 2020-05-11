def run(env):
    line = 0
    while True:
        if line == 0:
            env.set_register('R0', 1)
            line += 1
        if line == 1:
            env.set_register('R1', env.get_register('R0'))
            line += 1
        if line == 2:
            env.set_register('R2', env.get_register('R1') + 1)
            line += 1
        if line == 3:
            env.set_register('R3', 1 + env.get_register('R2'))
            line += 1
        if line == 4:
            env.set_register('R4', env.get_register('R2') * env.get_register('R1'))
            line += 1
        else:
            return
