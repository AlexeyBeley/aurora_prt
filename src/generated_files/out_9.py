def run(env):
    env.set_label('PRINTR5', 3)
    env.set_label('END', 6)
    line = 0
    while True:
        if line == 0:
            env.set_register('R5', 2020)
            line += 1
        elif line == 1:
            env.push_call_return_line(line + 1)
            line = env.get_line_by_label('PRINTR5')
        elif line == 2:
            line = env.get_line_by_label('END')
        elif line == 3:
            line += 1
        elif line == 4:
            print(env.get_register('R5'))
            line += 1
        elif line == 5:
            line = env.pop_call_return_line()
        elif line == 6:
            line += 1
        else:
            return
