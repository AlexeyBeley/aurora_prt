
class Environment(object):
    def __init__(self):
        self.registers = [None for _ in range(10)]
        self.labels = {}

    def reg_id_from_reg_name(self, name):
        return int(name[1:])

    def set_register(self, reg_name, value):
        self.registers[self.reg_id_from_reg_name(reg_name)] = value
        return True

    def get_register(self, reg_name):
        return self.registers[self.reg_id_from_reg_name(reg_name)]

    def set_label(self, label_name, value):
        self.labels[label_name] = value
        return True

    def get_line_by_label(self, label_name):
        return self.labels[label_name]
