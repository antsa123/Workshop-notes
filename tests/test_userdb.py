import os
import sys
import unittest
from unittest.mock import patch, MagicMock

# Add the path to your project directory to the system path
if (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) not in sys.path):
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from app.db import Database

class TestUserDB(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        pass

    @classmethod
    def tearDownClass(self):
        pass

    def setUp(self): #this runs for each test
        self.db = Database()

    def tearDown(self): #for each test also
        pass

    def test_add_user_when_username_is_valid(self):
        self.db.add_user('matti', 'meikalainen')

        self.assertTrue(self.user_with_name_in_db(self.db, 'matti'))
        #print(', '.join(db.userlist))

    def test_add_user_when_username_is_not_valid(self):
        '''test case 1'''
        '''given when then'''

        # test case 1.1
        new_test_username = 'toomuchcharactersinmyusernameiguess'

        def new_print(teksti):
            pass

        with patch('builtins.print', MagicMock(side_effect=new_print)) as mock:
            self.db.add_user(new_test_username, 'pollo')
            self.assertFalse(self.user_with_name_in_db(self.db, new_test_username))
            mock.assert_called_once()

        # test case 1.2
        new_test_username = 'ääpöpöjö'
        self.db.add_user(new_test_username, 'pollo')
        self.assertFalse(self.user_with_name_in_db(self.db, new_test_username))

        # test case 1.3
        new_test_username = 'to'
        self.db.add_user(new_test_username, 'pollo')
        self.assertFalse(self.user_with_name_in_db(self.db, new_test_username))


    def user_with_name_in_db(self, db: Database, username: str) -> bool:
        for user in db.userlist:
            if user.username is username:
                return True
        return False

if __name__ == '__main__':
    unittest.main()
