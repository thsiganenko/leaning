#!/usr/bin/env python

import unittest
import sys
from io import StringIO
from examples import main


class TestForCollatzSequence(unittest.TestCase):
    def setUp(self):
        self.save_io = sys.stdout
        sys.stdout = StringIO()

    def tearDown(self):
        sys.stdout = self.save_io

    def test_normal_mode(self):
        main(3)
        sys.stdout.seek(0)
        result = [s.strip() for s in sys.stdout.readlines()]
        source = ['10', '5', '16', '8', '4', '2', '1']

        self.assertEqual(result, source)


if __name__ == '__main__':
    unittest.main()
