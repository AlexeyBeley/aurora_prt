def run(env):
    line = 0
    while True:
        if line == 0:
            env.set_register('R0', 1 * 2)
            line += 1
        else:
            return
