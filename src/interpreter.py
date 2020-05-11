import os
import pdb
from tokenizer import Tokenizer
from parser import Parser
from generator import Generator
from environment import Environment


class Interprerter(object):
    def __init__(self, file_path):
        self.tokenizer = Tokenizer(file_path)
        self.parser = Parser()
        self.generator = Generator()
        self.env = Environment()

        self.interpreted_file_name = os.path.join(os.path.abspath(os.path.dirname(__file__)), "interpreted_tmp.py")

    def run_interpreter(self):
        self.generate_file()
        self.run_generated_file()

    def generate_file(self):
        lst_tokenized_lines = self.tokenizer.tokenize()

        lst_flow, lst_labels = self.parser.parse_tokens(lst_tokenized_lines)

        str_generated = self.generator.generate(lst_flow, lst_labels)

        with open(self.interpreted_file_name, "w") as f:
            f.write(str_generated)

    def run_generated_file(self):
        pdb.set_trace()
        from interpreted_tmp import run
        run(self.env)
