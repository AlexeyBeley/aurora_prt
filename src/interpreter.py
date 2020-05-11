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
        self.interpreted_file_name = None

    def run_interpreter(self, dst_file_name="interpreted_tmp.py"):
        self.interpreted_file_name = os.path.join(os.path.abspath(os.path.dirname(__file__)), "generated_files", dst_file_name)

        self.generate_file()
        self.run_generated_file()

    def generate_file(self):
        lst_tokenized_lines = self.tokenizer.tokenize()

        lst_flow, lst_labels = self.parser.parse_tokens(lst_tokenized_lines)

        str_generated = self.generator.generate(lst_flow, lst_labels)
        with open(self.interpreted_file_name, "w") as f:
            f.write(str_generated)

    def run_generated_file(self):
        module_name = os.path.basename(self.interpreted_file_name)
        module_name = "generated_files." + module_name.strip(".py")
        mod = __import__(module_name, fromlist=[''])
        mod.run(self.env)

