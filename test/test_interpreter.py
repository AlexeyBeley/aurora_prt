import unittest
import logging
import sys
import os
from io import StringIO
import pdb

logger = logging.getLogger('tokenizer')
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
logger.addHandler(ch)

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from tokenizer import Tokenizer
from parser import Parser
from interpreter import Interprerter
from environment import Environment
from generator import Generator
TEST_CASES_DIR = "test_cases"


#@unittest.skip("todo:")
class TestALPLInterpreter(unittest.TestCase):
    #@unittest.skip("todo:")
    def test_environment_set(self):
        env = Environment()
        for i in range(10):
            self.assertEqual(env.set_register("R{}".format(i), i), True)

    # @unittest.skip("todo:")
    def test_environment_reg_id_from_reg_name(self):
        env = Environment()
        for i in range(10):
            self.assertEqual(env.reg_id_from_reg_name("R{}".format(i)), i)

    #@unittest.skip("todo:")
    def test_init(self):
        for src_filename in os.listdir(TEST_CASES_DIR):
            Tokenizer(os.path.join(TEST_CASES_DIR, src_filename))

    #@unittest.skip("todo:")
    def test_tokenize(self):
        for src_filename in os.listdir(TEST_CASES_DIR):
            logger.debug("tokenizing {}".format(src_filename))
            Tokenizer(os.path.join(TEST_CASES_DIR, src_filename)).tokenize()

    #@unittest.skip("todo:")
    def test_generator_case0(self):
        src_filename = "test_case0.alpl"
        result_filename = "./test_results/test_case0.py"

        lst_lines = Tokenizer(os.path.join(TEST_CASES_DIR, src_filename)).tokenize()
        lst_flow, lst_labels = Parser().parse_tokens(lst_lines)

        str_ret = Generator().generate(lst_flow, lst_labels)
        with open(result_filename) as f:
            self.assertEqual(str_ret, f.read())

    # @unittest.skip("todo:")
    def test_generator_case1(self):
        src_filename = "test_case1.alpl"
        result_filename = "./test_results/test_case1.py"

        lst_lines = Tokenizer(os.path.join(TEST_CASES_DIR, src_filename)).tokenize()
        lst_flow, lst_labels = Parser().parse_tokens(lst_lines)

        str_ret = Generator().generate(lst_flow, lst_labels)
        with open(result_filename) as f:
            self.assertEqual(str_ret, f.read())

    # @unittest.skip("todo:")
    def test_generator_case2(self):
        src_filename = "test_case2.alpl"
        result_filename = "./test_results/test_case2.py"

        lst_lines = Tokenizer(os.path.join(TEST_CASES_DIR, src_filename)).tokenize()
        lst_flow, lst_labels = Parser().parse_tokens(lst_lines)

        str_ret = Generator().generate(lst_flow, lst_labels)
        with open(result_filename) as f:
            self.assertEqual(str_ret, f.read())

    # @unittest.skip("todo:")
    def test_generator_case3(self):
        src_filename = "test_case3.alpl"
        result_filename = "./test_results/test_case3.py"

        lst_lines = Tokenizer(os.path.join(TEST_CASES_DIR, src_filename)).tokenize()
        lst_flow, lst_labels = Parser().parse_tokens(lst_lines)

        str_ret = Generator().generate(lst_flow, lst_labels)
        with open(result_filename) as f:
            self.assertEqual(str_ret, f.read())

    # @unittest.skip("todo:")
    def test_generator_case4(self):
        src_filename = "test_case4.alpl"
        result_filename = "./test_results/test_case4.py"

        lst_lines = Tokenizer(os.path.join(TEST_CASES_DIR, src_filename)).tokenize()
        lst_flow, lst_labels = Parser().parse_tokens(lst_lines)

        str_ret = Generator().generate(lst_flow, lst_labels)
        with open(result_filename) as f:
            self.assertEqual(str_ret, f.read())
    # @unittest.skip("todo:")

    def test_generator_case5(self):
        src_filename = "test_case5.alpl"
        result_filename = "./test_results/test_case5.py"

        lst_lines = Tokenizer(os.path.join(TEST_CASES_DIR, src_filename)).tokenize()
        lst_flow, lst_labels = Parser().parse_tokens(lst_lines)

        str_ret = Generator().generate(lst_flow, lst_labels)
        with open(result_filename) as f:
            self.assertEqual(str_ret, f.read())

    def test_generator_case6(self):
        src_filename = "test_case6.alpl"
        result_filename = "./test_results/test_case6.py"

        lst_lines = Tokenizer(os.path.join(TEST_CASES_DIR, src_filename)).tokenize()
        lst_flow, lst_labels = Parser().parse_tokens(lst_lines)

        str_ret = Generator().generate(lst_flow, lst_labels)
        with open(result_filename) as f:
            self.assertEqual(str_ret, f.read())

    @unittest.skip("todo:")
    def test_interpreter_case0(self):
        old_stdout = sys.stdout
        sys.stdout = new_stdout = StringIO()

        src_filename = "test_case0.alpl"
        result_stdout_filename = "./test_results/test_case0_stdout"

        src_file_path = os.path.abspath(os.path.join(TEST_CASES_DIR, src_filename))
        Interprerter(src_file_path).run_interpreter()

        sys.stdout = old_stdout
        with open(result_stdout_filename) as f:
            self.assertEqual(new_stdout.getvalue(), f.read())

    @unittest.skip("todo:")
    def test_interpreter_case1(self):
        src_filename = "test_case1.alpl"
        result_stdout_filename = "./test_results/test_case1_stdout"

        old_stdout = sys.stdout
        sys.stdout = new_stdout = StringIO()

        src_file_path = os.path.abspath(os.path.join(TEST_CASES_DIR, src_filename))

        inter = Interprerter(src_file_path)
        inter.run_interpreter()

        sys.stdout = old_stdout
        with open(result_stdout_filename) as f:
            self.assertEqual(new_stdout.getvalue(), f.read())

    @unittest.skip("todo:")
    def test_interpreter_case2(self):
        src_filename = "test_case2.alpl"
        result_stdout_filename = "./test_results/test_case2_stdout"

        old_stdout = sys.stdout
        sys.stdout = new_stdout = StringIO()

        src_file_path = os.path.abspath(os.path.join(TEST_CASES_DIR, src_filename))

        inter = Interprerter(src_file_path)
        inter.run_interpreter()

        sys.stdout = old_stdout
        with open(result_stdout_filename) as f:
            self.assertEqual(new_stdout.getvalue(), f.read())

    @unittest.skip("todo:")
    def test_interpreter_case3(self):
        src_filename = "test_case1.alpl"
        result_stdout_filename = "./test_results/test_case3_stdout"

        old_stdout = sys.stdout
        sys.stdout = new_stdout = StringIO()

        src_file_path = os.path.abspath(os.path.join(TEST_CASES_DIR, src_filename))

        inter = Interprerter(src_file_path)
        inter.run_interpreter()

        sys.stdout = old_stdout
        with open(result_stdout_filename) as f:
            self.assertEqual(new_stdout.getvalue(), f.read())

    @unittest.skip("todo:")
    def test_interpreter_case4(self):
        src_filename = "test_case4.alpl"
        result_stdout_filename = "./test_results/test_case4_stdout"

        old_stdout = sys.stdout
        sys.stdout = new_stdout = StringIO()

        src_file_path = os.path.abspath(os.path.join(TEST_CASES_DIR, src_filename))

        inter = Interprerter(src_file_path)
        inter.run_interpreter()

        sys.stdout = old_stdout
        with open(result_stdout_filename) as f:
            self.assertEqual(new_stdout.getvalue(), f.read())

    # @unittest.skip("todo:")
    def test_interpreter_case5(self):
        src_filename = "test_case5.alpl"
        result_stdout_filename = "./test_results/test_case5_stdout"

        old_stdout = sys.stdout
        sys.stdout = new_stdout = StringIO()

        src_file_path = os.path.abspath(os.path.join(TEST_CASES_DIR, src_filename))

        inter = Interprerter(src_file_path)

        inter.run_interpreter(dst_file_name="tmp_1.py")

        sys.stdout = old_stdout
        with open(result_stdout_filename) as f:
            self.assertEqual(new_stdout.getvalue(), f.read())

    #@unittest.skip("todo:")
    def test_interpreter_case6(self):
        src_filename = "test_case6.alpl"
        result_stdout_filename = "./test_results/test_case6_stdout"

        old_stdout = sys.stdout
        sys.stdout = new_stdout = StringIO()

        src_file_path = os.path.abspath(os.path.join(TEST_CASES_DIR, src_filename))

        inter = Interprerter(src_file_path)

        inter.run_interpreter(dst_file_name="out_6.py")

        sys.stdout = old_stdout
        with open(result_stdout_filename) as f:
            self.assertEqual(new_stdout.getvalue(), f.read())

    @unittest.skip("todo:")
    def test_parser(self):
        for src_filename in os.listdir(TEST_CASES_DIR):
            logger.debug("tokenizing {}".format(src_filename))
            lst_lines = Tokenizer(os.path.join(TEST_CASES_DIR, src_filename)).tokenize()
            Parser().parse_tokens(lst_lines)


    @unittest.skip("todo:")
    def test_interpreter(self):
        for src_filename in os.listdir(TEST_CASES_DIR):
            logger.debug("interpreting {}".format(src_filename))
            Interprerter(os.path.join(TEST_CASES_DIR, src_filename)).run_interpreter()