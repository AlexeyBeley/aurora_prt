import pdb

class Generator(object):
    def generate(self, lst_flow_lines, lst_label_lines):
        lst_new = []
        for_spaces = "    "
        indent = 1
        lst_new.append("def run(env):")
        if len(lst_label_lines) > 0:
            for str_set_label in lst_label_lines:
                lst_new.append("{}{}".format(for_spaces * indent, str_set_label))
            pdb.set_trace()
        lst_new.append("{}line = 0".format(for_spaces * indent))
        lst_new.append("{}while True:".format(for_spaces * indent))

        for str_line in lst_flow_lines:
            lst_new.append("{}{}".format(for_spaces * (indent+1), str_line))

        str_ret = "\n".join(lst_new)

        return str_ret
