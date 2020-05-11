import pdb

class Generator(object):
    def generate(self, lst_parsed_line):
        lst_new = []
        for_spaces = "    "
        indent = 1
        lst_new.append("def run(env):")
        lst_new.append("{}line = 0".format(for_spaces * indent))
        lst_new.append("{}while True:".format(for_spaces * indent))

        for str_line in lst_parsed_line:
            lst_new.append("{}{}".format(for_spaces * (indent+1), str_line))

        str_ret = "\n".join(lst_new)

        return str_ret
