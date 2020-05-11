import pdb

class Tokenizer:
    def __init__(self, file_name):
        self.tokens_map = {"LET": self._let,
                      "IF": self._if,
                      "JUMP": self._jump,
                      "CALL": self._call,
                      "RERTURN": self._return,
                      "PRINT": self._print,
                      }

        with open(file_name) as f:
            self.lines = f.readlines()

    def tokenize(self):
        return [self.tokenize_line(line) for line in self.lines]

    def tokenize_line(self, str_line):
        for token_key, token_func in self.tokens_map:
            if str_line.startswith(token_key):
                return token_func(str_line)

        raise RuntimeError("Wrong token")

    def _let(self, str_line):
        pdb.set_trace()

    def _if(self, str_line):
        pdb.set_trace()

    def _jump(self, str_line):
        pdb.set_trace()

    def _call(self, str_line):
        pdb.set_trace()

    def _return(self, str_line):
        pdb.set_trace()

    def _print(self, str_line):
        pdb.set_trace()