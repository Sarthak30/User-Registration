import unittest
from app.models import User

class UserModelTestCase(unittest.testcase):
	def test_password_setter(self):
		u = User(password = 'cat')
		self.assertTrue(u.password_hash is not none)
		
	def test_no_password_getter(self):
		u = User(password = 'cat')
		with self.assertRaises(AttributeError):
			u.password
	
	def test_password_verification(self):
		u = user(password = 'cat')
		self.assertTrue(u.verify_password('cat'))
		self.assertFalse(u.verify_password('dog'))
		
	def test_password_salts_are_random(self):
		u = User(password = 'cat')
		u2 = User(password = 'cat')
		self.assertTrue(u.password_hash != u2.password_hash)
