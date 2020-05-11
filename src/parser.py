import pdb
from tokenizer import Tokenizer

class Parser(object):
    LET = ["env.set_register('{REGISTER_NAME}', {VALUE})",
           "line += 1"
           ]

    GET_REGISTER_VALUE = "env.get_register({REGISTER_ID})"

    FINAL_ELSE = ["else:",
                  "    return\n"
                  ]

    def __init__(self):
        self.line = 0

    def parse_tokens(self, lst_tokens):
        lst_ret = []

        for token_type, token_value in lst_tokens:
            if token_type == Tokenizer.TokenType.LET:
                lst_let = self.init_let(token_value)
                lst_ret += lst_let
            else:
                pdb.set_trace()

        lst_ret += self.FINAL_ELSE
        return lst_ret

    def init_let(self, token_value):
        lst_ret = ["if line == {}:".format(self.line)]
        string_block_let = "\n".join(self.LET)

        if len(token_value) == 3:
            string_block_let = string_block_let.format(REGISTER_NAME=token_value[0], VALUE=token_value[2])
        else:
            pdb.set_trace()
            raise NotImplementedError()

        lst_ret += self.string_block_to_intended_lines(string_block_let)
        self.line += 1
        return lst_ret

    def string_block_to_intended_lines(self, string_block):
        return ["{}{}".format("    ", line) for line in string_block.split("\n")]



