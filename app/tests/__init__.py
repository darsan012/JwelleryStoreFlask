"""
 running all the unit test through __init__.py, all tests in a single place
"""

import unittest

if __name__ == "__main__":
    loader = unittest.TestLoader()
    # testing file that begins with test_ and ends with.py
    suite = loader.discover(start_dir=".", pattern="test_*.py")

    runner = unittest.TextTestRunner(verbosity=2)
    # verbosity=2 for detailed output (displays test names and results in a verbose format)

    # running the test
    runner.run(suite)