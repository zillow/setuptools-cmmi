import unittest

# write functional, low overhead tests like this
def test_has_tests():
    pass
    # assert_true (False, "There aren't any tests.")

def test_import_setuptools_cmmi():
    import setuptools_cmmi

# write tests that require member variables like this
class Test_setuptools_cmmi(unittest.TestCase):

    def setUp (self):
        pass

    def tearDown (self):
        pass

    def test_has_tests (self):
        pass
        # assert_true (False, "There aren't any tests.")
        # or, if you prefer using the member function
        #self.assertTrue (False, "There aren't any tests.")
