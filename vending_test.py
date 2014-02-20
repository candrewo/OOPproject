import unittest
from vending_machine import VendingMachine, NewItem

class TestVendingMachine(unittest.TestCase):



	def setUp(self):
		self.vending = VendingMachine(156700)
		self.oj = NewItem('oj', 3)
		self.stock = {'coca-cola': 10, 'sprite': 10,'root beer': 10}
		
	def get_stock_test (self):
		self.assertEqual(self.vending.get_stock(),{'coca-cola': 10,
		 'sprite': 10,'root beer': 10})

	def replenish_test(self):
		self.vending.replenish('sprite',20)
		self.assertEqual(self.stock,{'coca-cola': 10,
		 'sprite': 30,'root beer': 10})

	def sell(self):
		self.vending.sell(sprite)
		self.assertEqual(self.stock,{'coca-cola': 10,
		 'sprite': 10,'root beer': 10})

	def add_new_item(self):
		self.vending.add_new_item(oj.item, oj.amount)
		self.assertEqual(self.stock,{'coca-cola': 10, 'sprite': 10,
			'root beer': 10, 'oj': 3})

if __name__ == '__main__':
	unittest.main()
