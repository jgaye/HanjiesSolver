from psolver import psolver
import unittest

# Use a dictionnary to define the data for each test.
# Contains input and expected values.
class TestData(dict):
    def __init__(self, **kwargs):
        if 'test_name' in kwargs:
            setattr(self, 'test_name', kwargs['test_name'])
            del kwargs['test_name']
        for key in kwargs:
            setattr(self, key, kwargs[key])
            self[key]=kwargs[key] 

# Utility to create all the test classes under a specific module.
def generate_test_classes(test_module, test_data_list, root_test_class):

    def build_test_class(test_data, root_test_class):

        class Test(root_test_class):
            def __init__(self, *args, **kwargs):
                root_test_class.__init__(self, *args, **kwargs)
                for key in test_data:
                    setattr(self, key, test_data[key])

            def test_func(self):
	        self.assertEqual (
                    self.expected,
                    psolver (self.column_clues, self.row_clues))

        return Test

    for test_data in test_data_list:
        test_class = build_test_class (test_data, root_test_class)
        test_class.__name__ = test_data.test_name
        test_class.__module__ = test_module.__name__
        setattr(test_module, test_class.__name__, test_class)


class RootTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(RootTest, self).__init__(*args, **kwargs)
