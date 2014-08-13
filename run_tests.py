#!/usr/bin/env python
import sys
import os
import unittest
from subprocess import call
from optparse import OptionParser
sys.path.insert(1, 'tests/src')

"""
this python script is used as a test runner
It takes the following options and arguments:

./run_tests.py [-v|--verbose|-q|--quiet] [args]

args refer to test names so that individual tests can be run directly from the
tool.
By default, if no args are provided, the script will run all tests from modules
starting from the dir 'tests/'.

Example command to run a single test (with verbose option):
    ./run_tests.py -v logimage_15_15.test_2_nomade

Example command to run all tests (with quiet option):
    ./run_tests.py -q
"""


# parse both the tool arguments and the tool options
parser = OptionParser()
parser.add_option("-q", "--quiet",
		  action="store_const", const=0, dest="verbose", default=1,
                  help="decrease verbosity")
parser.add_option("-v", "--verbose",
                  action="store_const", const=2, dest="verbose", default=1,
                  help="increase verbosity")
(options, args) = parser.parse_args()


#=====
# Main
#=====
"""
check whether arguments are specified in the command-line
- if yes: run individual tests using the unittest command-line
- if no: run all tests together
"""
if len(args) > 0:
    # run individual tests from the command-line
    # open the directory that contains all test packages
    os.chdir('tests')

    # call directly unittest from the command line
    command_args = (["python", "-m", "unittest"])

    # adapt the verbosity level
    if options.verbose == 0:
        command_args.append("-q")
    elif options.verbose == 2:
        command_args.append("-v")

    for arg in args:
        command_args.append(arg)

    call(command_args)

else:
    # run all tests together
    if __name__ == '__main__':
        test_runner = unittest.TextTestRunner(verbosity=options.verbose)
        test_suite = unittest.TestLoader().discover('tests', pattern='*[!.py]')
        test_runner.run (test_suite)
