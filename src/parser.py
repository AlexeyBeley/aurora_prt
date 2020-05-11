import pdb
from tokenizer import Tokenizer

class Parser(object):
    LET_FLOW_STEP = ["env.set_register('{REGISTER_NAME}', {VALUE})",
                     "line += 1"
                     ]

    LABEL_FLOW_STEP = ["line += 1"]

    JUMP_FLOW_STEP = ["line = env.get_line_by_label('{LABEL_NAME}')"]

    GET_REGISTER_VALUE = "env.get_register('{REGISTER_NAME}')"
    SET_LABEL_VALUE = "env.set_label('{LABEL_NAME}', {LINE_NUMBER})"

    FINAL_ELSE = ["else:",
                  "    return\n"
                  ]

    def __init__(self):
        self.line = 0

    def parse_tokens(self, lst_tokens):
        lst_flow = []
        lst_labels = []

        for token_type, token_value in lst_tokens:
            if token_type == Tokenizer.TokenType.LET:
                lst_let = self.init_let(token_value)
                lst_flow += lst_let
            elif token_type == Tokenizer.TokenType.LABEL:
                lst_label_flow, lst_label_set = self.init_label(token_value)
                lst_flow += lst_label_flow
                lst_labels += lst_label_set
            elif token_type == Tokenizer.TokenType.JUMP:
                lst_let = self.init_jump(token_value)
                lst_flow += lst_let
            else:
                pdb.set_trace()

        lst_flow += self.FINAL_ELSE
        return lst_flow, lst_labels

    def init_let(self, token_value):
        lst_ret = ["if line == {}:".format(self.line)]
        string_block_let = "\n".join(self.LET_FLOW_STEP)

        if len(token_value) == 3:
            string_block_let = string_block_let.format(REGISTER_NAME=token_value[0],
                                                       VALUE=self.init_register_or_int_template(token_value[2]))
        else:
            expression = "{} {} {}".format(self.init_register_or_int_template(token_value[2]), token_value[3],
                                           self.init_register_or_int_template(token_value[4]))

            string_block_let = string_block_let.format(REGISTER_NAME=token_value[0],
                                                       VALUE=expression)

        lst_ret += self.string_block_to_intended_lines(string_block_let)
        self.line += 1
        return lst_ret

    def init_label(self, token_value):
        lst_label_flow = ["if line == {}:".format(self.line)]

        lst_label_set = [self.SET_LABEL_VALUE.format(LABEL_NAME=token_value[0], LINE_NUMBER=self.line)]

        string_block_let = "\n".join(self.LABEL_FLOW_STEP)
        lst_label_flow += self.string_block_to_intended_lines(string_block_let)

        self.line += 1

        return lst_label_flow, lst_label_set

    def init_jump(self, token_value):
        lst_flow = ["if line == {}:".format(self.line)]
        string_block_let = "\n".join(self.JUMP_FLOW_STEP)
        string_block_let = string_block_let.format(LABEL_NAME=token_value[0])
        lst_flow += self.string_block_to_intended_lines(string_block_let)

        self.line += 1

        return lst_flow

    def init_register_or_int_template(self, value):
        if isinstance(value, int):
            return str(value)
        else:
            return self.GET_REGISTER_VALUE.format(REGISTER_NAME=value)

    def string_block_to_intended_lines(self, string_block):
        return ["{}{}".format("    ", line) for line in string_block.split("\n")]



