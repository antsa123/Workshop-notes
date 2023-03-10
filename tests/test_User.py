import unittest

class TestUser(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        print('This is run only once when starting the tests')

    @classmethod
    def tearDownClass(self):
        print('This is run only once when finishing the tests')

    def setUp(self): #this runs for each test
        print('Setting up test')

    def tearDown(self): #for each test also
        print("Tearing down")

    def test_username_is_valid(self):
        print('testing username is of valid for')

    def test_username_is_not_valid(self):
        print('testing username is not of valid form')


if __name__ == '__main__':
    unittest.main()
