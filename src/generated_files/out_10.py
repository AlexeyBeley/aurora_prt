def run(env):
    env.set_label('LOOPONR5', 3)
    env.set_label('PRINTR5', 10)
    env.set_label('PRINTR4', 13)
    env.set_label('DECR5', 16)
    env.set_label('INCR4', 19)
    env.set_label('END', 22)
    line = 0
    while True:
        if line == 0:
            env.set_register('R5', 10)
            line += 1
        elif line == 1:
            env.set_register('R0', 0)
            line += 1
        elif line == 2:
            env.set_register('R4', 2)
            line += 1
        elif line == 3:
            line += 1
        elif line == 4:
            if env.get_register('R5') == env.get_register('R0'):
                line = env.get_line_by_label('END')
            else:
                line += 1
        elif line == 5:
            env.push_call_return_line(line + 1)
            line = env.get_line_by_label('PRINTR5')
        elif line == 6:
            env.push_call_return_line(line + 1)
            line = env.get_line_by_label('INCR4')
        elif line == 7:
            env.push_call_return_line(line + 1)
            line = env.get_line_by_label('DECR5')
        elif line == 8:
            env.push_call_return_line(line + 1)
            line = env.get_line_by_label('PRINTR4')
        elif line == 9:
            line = env.get_line_by_label('LOOPONR5')
        elif line == 10:
            line += 1
        elif line == 11:
            print(env.get_register('R5'))
            line += 1
        elif line == 12:
            line = env.pop_call_return_line()
        elif line == 13:
            line += 1
        elif line == 14:
            print(env.get_register('R4'))
            line += 1
        elif line == 15:
            line = env.pop_call_return_line()
        elif line == 16:
            line += 1
        elif line == 17:
            env.set_register('R5', env.get_register('R5') - 1)
            line += 1
        elif line == 18:
            line = env.pop_call_return_line()
        elif line == 19:
            line += 1
        elif line == 20:
            env.set_register('R4', env.get_register('R4') * 2)
            line += 1
        elif line == 21:
            line = env.pop_call_return_line()
        elif line == 22:
            line += 1
        else:
            return
