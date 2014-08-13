import os
import sys
from all_test_data import all_test_data
src_path=os.path.abspath(os.path.join(os.path.dirname(__file__), '../src'))
if not src_path in sys.path:
    sys.path.insert(1, src_path)
import test_framework
import unittest

test_framework.generate_test_classes(test_module=sys.modules[__name__],
    test_data_list=all_test_data, root_test_class=test_framework.RootTest)

if __name__ == '__main__':
    unittest.main()
