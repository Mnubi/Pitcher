import unittest

class UserTest(unittest.TestCase):
    def setUp(self):
        self.new_user = User(username='rial',password='12345')
   

    def test_no_access_password(self):
        with self.assertRaises(AttributeError):
            self.new_user.password

    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('12345'))

if __name__ == '__main__':
    unittest.main()