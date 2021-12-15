#below, creating the class "Item" as well as a method
#to be applied on this class.

class Item:
	def __init__(self, name: str, price: float, quantity=0):
		# Run validations to the received arguments
		assert price >= 0, f"Price {price} is not greater than or equal to zero!"
		assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"

		# Assign to self object
		self.name = name
		self.price = price
		self.quantity = quantity

	def calculate_total_price(self):
		return self.price * self.quantity

item1 = Item("Phone", 100, 5)

# assigning attributes to the instance of the Item class
# but this is hardcoding the attributes
# item1.name = "Phone"
# item1.price = 100
# item1.quantity = 5

#calling the method on the instance
print(item1.calculate_total_price());
