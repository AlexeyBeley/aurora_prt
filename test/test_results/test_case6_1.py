def run(env):
    env.set_label('R0GREATER', 4)
    line = 0
    while True:
        if line == 0:
            env.set_register('R0', 2)
            line += 1
        elif line == 1:
            env.set_register('R1', 1)
            line += 1
        elif line == 2:
            if env.get_register('R0') == env.get_register('R1'):
                line = env.get_line_by_label('R0GREATER')
            else:
                line += 1
        elif line == 3:
            print(env.get_register('R1'))
            line += 1
        elif line == 4:
            line += 1
        elif line == 5:
            print(env.get_register('R0'))
            line += 1
        else:
            return
