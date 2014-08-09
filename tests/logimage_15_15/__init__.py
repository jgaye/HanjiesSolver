import sys
sys.path.insert(0, "../src")
from all_test_data import all_test_data
import test_framework
import unittest
import inspect

current_module=sys.modules[__name__]

#def discover():
test_framework.generate_test_classes(test_module=current_module,
    test_data_list=all_test_data, root_test_class=test_framework.RootTest)


if __name__ == '__main__':
    unittest.main()
