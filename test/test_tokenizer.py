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
TEST_CASES_DIR = "test_cases"
#@unittest.skip("todo:")
class TestTokenizer(unittest.TestCase):
    #@unittest.skip("todo:")
    def test_init(self):
        for src_filename in os.listdir(TEST_CASES_DIR):
            Tokenizer(os.path.join(TEST_CASES_DIR, src_filename))

    # @unittest.skip("todo:")
    def test_tokenize(self):
        for src_filename in os.listdir(TEST_CASES_DIR):
            logger.debug("tokenizing {}".format(src_filename))
            Tokenizer(os.path.join(TEST_CASES_DIR, src_filename)).tokenize()
