import unittest
from vending_machine import VendingMachine

class TestVendingMachine(unittest.TestCase):

	def setUp(self):
		self.vend = VendingMachine('num1')

	def test_sale (self):
		self.vend.sale(sprite)
		self.assertEqual (stock[item,0])