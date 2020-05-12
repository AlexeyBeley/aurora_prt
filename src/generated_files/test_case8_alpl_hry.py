def run(env):
    env.set_label('LOOP', 2)
    env.set_label('END', 6)
    line = 0
    while True:
        if line == 0:
            env.set_register('R0', 0)
            line += 1
        elif line == 1:
            env.set_register('R1', 10)
            line += 1
        elif line == 2:
            line += 1
        elif line == 3:
            if env.get_register('R0') == env.get_register('R1'):
                line = env.get_line_by_label('END')
            else:
                line += 1
        elif line == 4:
            env.set_register('R0', env.get_register('R0') + 1)
            line += 1
        elif line == 5:
            line = env.get_line_by_label('LOOP')
        elif line == 6:
            line += 1
        else:
            return
