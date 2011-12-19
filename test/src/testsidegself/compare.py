import os.path
import pdb
import testsidegself.command
import StringIO
import unittest


SRC_PATH = None
DEST_PATH = None
HEAD = """\
from selenium import selenium
import unittest, time, re

class testcase(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*chrome", "http://code.google.com/")
        self.selenium.start()

    def test_testcase(self):
        sel = self.selenium
"""
FOOT = """\

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
"""


def create_expectation(src_path):
    commands = testsidegself.command.extract(src_path)
    exp = StringIO.StringIO()
    exp.write(HEAD)
    for command in commands:
        exp.write('        sel.%s(' % command[0])
        if len(command) > 1:
            args = command[1:]
            exp.write('"')
            exp.write('", "'.join(args))
            exp.write('"')
        exp.write(')\n')
    exp.write(FOOT)
    exp.seek(0)
    return exp.readlines()


class TestResult(unittest.TestCase):

    maxDiff = None

    def test_result(self):
        exp = create_expectation(SRC_PATH)
        got = file(os.path.join(DEST_PATH, 'testcase.py'), 'r').readlines()
        self.assertEqual(exp, got)

def compare_result(src_path, dest_path):
    """Compare the result the converter produced with the expectations."""
    global SRC_PATH, DEST_PATH
    SRC_PATH = src_path
    DEST_PATH = dest_path
    unittest.main(module='testsidegself.compare')