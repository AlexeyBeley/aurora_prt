import unittest
import logging
import sys
import os

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
TEST_CASES_DIR = "test_cases"


#@unittest.skip("todo:")
class TestAlplInterpreter(unittest.TestCase):
    #@unittest.skip("todo:")
    def test_init(self):
        for src_filename in os.listdir(TEST_CASES_DIR):
            Tokenizer(os.path.join(TEST_CASES_DIR, src_filename))

    # @unittest.skip("todo:")
    def test_tokenize(self):
        for src_filename in os.listdir(TEST_CASES_DIR):
            logger.debug("tokenizing {}".format(src_filename))
            Tokenizer(os.path.join(TEST_CASES_DIR, src_filename)).tokenize()

    # @unittest.skip("todo:")
    def test_parser(self):
        for src_filename in os.listdir(TEST_CASES_DIR):
            logger.debug("tokenizing {}".format(src_filename))
            lst_lines = Tokenizer(os.path.join(TEST_CASES_DIR, src_filename)).tokenize()
            Parser().parse_tokens(lst_lines)

    # @unittest.skip("todo:")
    def test_interpreter(self):
        for src_filename in os.listdir(TEST_CASES_DIR):
            logger.debug("interpreting {}".format(src_filename))
            Interprerter(os.path.join(TEST_CASES_DIR, src_filename)).run_interpreter()