class VendingMachine(object):

    # class variables
    stock = {'coca-cola': 10, 'sprite': 10,'root beer': 10}

    # instance variables
    def __init__ (self, serial_num):
        self.serial_num = serial_num

    def sell(self, item): #method: sell items
        if self.stock[item] > 0:
            self.stock[item] -= 1
            return self.stock
        else:
            raise Exception('empty')

    def replenish(self, item, number): #method: restock the vending machine
        self.stock[item] = number
        return self.stock

    def get_stock(self): #method: current stock of drinks
        return self.stock

    def add_new_item(self, new_item, amount):
    	self.stock[new_item] = amount
    	return self.stock


class NewItem(object):

    def __init__(self, item,amount):
        self.item = item
        self.amount = amount



# vending = VendingMachine(156700)
# # oj = NewItem('oj',3)
# print vending.sell('sprite')
# # print vending.replenish('sprite', 20)
# vending.sell('sprite')
# vending.sell('sprite')
# vending.sell('sprite')
# vending.sell('sprite')
# # vending.add_new_item(oj.item,oj.amount)
# # vending.add_new_item('oj',3)
# print vending.sell('sprite')
# print vending.get_stock()