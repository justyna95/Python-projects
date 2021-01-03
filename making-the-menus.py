# Creating the Menu class that will have the constructor for all of our menus.

class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
  # Giving the Menu class a string representation method and indicating when the menu is available:
  def __repr__(self):
    return self.name + " menu is available " + str(self.start_time) + " - " + str(self.end_time) + "."
  
  # Calculating the total price of a purchase consisting of all the items in purchased_items:
  def calculate_bill(self, purchased_items):
    bill = 0
    for item in purchased_items:
      if item in self.items:
        bill += self.items[item]
    return bill
    
# Creating 4 different menus:
brunch_items = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}
brunch_menu = Menu("Brunch", brunch_items, 1100, 1600)
#print(brunch_menu.name)

early_bird_items = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00
}
early_bird_menu = Menu("Early Bird", early_bird_items, 1500, 1800)
#print(early_bird_menu.items)

dinner_items = {
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00
}
dinner_menu = Menu("Dinner", dinner_items, 1700, 2300)

kids_items = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}
kids_menu = Menu("Kids", kids_items, 1100, 2100)

# print(brunch_menu)
# Testing the calculate_bill method:
print(brunch_menu.calculate_bill(['pancakes', 'home fries', 'coffee']))
print(early_bird_menu.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))

# Creating a Franchise class that contains all the locations and available menus within a franchise:
class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus
  def __repr__(self):
    return "The restaurant is located at {address}".format(address = self.address)
  
  # Creating a function that returns available at any specific time menus:
  def available_menus(self, time):
    available_menus = []
    for menu in self.menus:
      if time >= menu.start_time and time <= menu.end_time:
        available_menus.append(menu)
    return available_menus
  
menus = [brunch_menu, early_bird_menu, dinner_menu, kids_menu]
flagship_store = Franchise("1232 West End Road", menus)
new_installment = Franchise("12 East Mulberry Street", menus)
#print(flagship_store)
#print(flagship_store.available_menus(1200))
#print(flagship_store.available_menus(1700))

# Creating a Business class that holds all our franchises:
class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises

basta_business = Business("Basta Fazoolin", [flagship_store, new_installment])

# Creating here the second Business, starting with menus:
arepas_items = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}
arepas_menu = Menu("Take a' Arepa", arepas_items, 1000, 2000)
arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])
arepa_business = Business("Take a' Arepa", [arepas_place])
#print arepa.franchises[0]



