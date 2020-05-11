def run(env):
    env.set_label('END', 1)
    line = 0
    while True:
        if line == 0:
            line = env.get_line_by_label('END')
        elif line == 1:
            line += 1
        else:
            return
