import unittest
from vending_machine import VendingMachine, NewItem

class TestVendingMachine(unittest.TestCase):



	def setUp(self):
		self.vending = VendingMachine(156700)
		self.oj = NewItem('oj', 3)
		self.stock = {'coca-cola': 10, 'sprite': 10,'root beer': 10}
		
	def test_sell (self):
		self.vending.sell(self.stock['sprite'])
		self.assertEqual(self.stock['sprite'],9)