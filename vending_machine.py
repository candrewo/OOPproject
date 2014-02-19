class VendingMachine(object):
	def __init__ (self, serial_num):
		self.serial_num = serial
		stock = {
            'coca-cola': 0,
            'sprite': 1,
            'fanta': 0,
        }
	def sale(self, item):
		self.stock = item
		if stock[item] > 0:
			stock[item] -= 1
		else:
			raise Exception('empty')
