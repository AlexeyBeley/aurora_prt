
class Environment(object):
    def __init__(self):
        self.registers = [None for _ in range(10)]

    def reg_id_from_reg_name(self, name):
        return int(name[1:])

    def set_register(self, reg_name, value):
        self.registers[self.reg_id_from_reg_name(reg_name)] = value
        return True

    def get_register(self, reg_id, value):
        return self.registers[reg_id]
