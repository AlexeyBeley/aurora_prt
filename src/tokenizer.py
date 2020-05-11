import pdb
from enum import Enum


class TokenizerError(Exception):
    pass


class Tokenizer:
    def __init__(self, file_name):

        self.tokens_map = {"LET ": self._let,
                          "IF ": self._if,
                          "JUMP ": self._jump,
                          "CALL ": self._call,
                          "RETURN": self._return,
                          "PRINT ": self._print}

        with open(file_name) as f:
            self.lines = f.readlines()

    class TokenType(Enum):
        LET = 1
        IF = 2
        JUMP = 3
        CALL = 4
        RETURN = 5
        PRINT = 6
        LABEL = 7

    def tokenize(self):
        lst_ret = []
        for line in self.lines:
            tokens = self.tokenize_line(line)
            if tokens is None:
                continue
            lst_ret.append(tokens)
        return lst_ret

    def tokenize_line(self, str_line):
        str_line = str_line.strip("\n")
        str_line = str_line.strip(" ")
        if not str_line:
            return None

        for token_key, token_func in self.tokens_map.items():
            if str_line.startswith(token_key):
                return token_func(str_line)

        return self._label(str_line)

    def int_or_reg(self, val):
        if val.startswith("R"):
            int(val[1:])
        else:
            val = int(val)
        return val

    def _let(self, str_line):
        lst_ret = str_line.split(" ")
        if lst_ret[2] != ":=":
            raise TokenizerError("LET is broken {}".format(str_line))

        lst_ret[3] = self.int_or_reg(lst_ret[3])

        if len(lst_ret) > 4:
            lst_ret[5] = self.int_or_reg(lst_ret[5])

        return self.TokenType.LET, lst_ret[1:]

    def _if(self, str_line):
        lst_ret = str_line.split(" ")
        return self.TokenType.IF, lst_ret[1:]

    def _jump(self, str_line):
        lst_ret = str_line.split(" ")
        return self.TokenType.JUMP, lst_ret[1:]

    def _call(self, str_line):
        lst_ret = str_line.split(" ")
        return self.TokenType.CALL, lst_ret[1:]

    def _return(self, str_line):
        if str_line != "RETURN":
            return self._label(str_line)

        return self.TokenType.RETURN, None

    def _print(self, str_line):
        lst_ret = str_line.split(" ")
        return self.TokenType.PRINT, lst_ret[1:]

    def _label(self, str_line):
        if " " in str_line:
            raise TokenizerError("Label is not alphanumeric {}".format(str_line))
        if not str_line.endswith(":"):
            raise TokenizerError("Label has no `:` {}".format(str_line))

        return self.TokenType.LABEL, [str_line[:-1]]
