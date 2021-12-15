#below, creating the class "Item" as well as a method
#to be applied on this class.

class Item:
	def calculate_total_price(self, x, y):
		return x * y

item1 = Item()

# assigning attributes to the instance of the Item class
# but this is hardcoding the attributes
item1.name = "Phone"
item1.price = 100
item1.quantity = 5

#calling the method on the instance
print(item1.calculate_total_price(item1.price, item1.quantity));
