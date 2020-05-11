
from tokenizer import Tokenizer
from parser import Parser
from generator import Generator


class Interprerter(object):
    def __init__(self, file_path):
        self.tokenizer = Tokenizer(file_path)
        self.parser = Parser()
        self.generator = Generator()
        self.interpreted_file_name = "interpreted_tmp.py"

    def run_interpreter(self):
        lst_tokenized_lines = self.tokenizer.tokenize()

        lst_parsed = self.parser.parse_tokens(lst_tokenized_lines)

        str_generated = self.generator.generate(lst_parsed)

        with open(self.interpreted_file_name, "w") as f:
            f.write(str_generated)

        from interpreted_tmp import run
        run()




