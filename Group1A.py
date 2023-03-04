# Author: Noah Hicks
# This program does what it do.

import random

class Order:
    def __init__(self):
        self.burger_count = self.randomBurgers()

    def randomBurgers(self):
        return random.randint(1, 20)

class Person:
    def __init__(self):
        self.customer_name = self.randomName()

    def randomName(self):
        asCustomers = ["Jefe", "El Guapo", "Lucky Day", "Ned Nederlander", "Dusty Bottoms", "Harry Flugleman", "Carmen", "Invisible Swordsman", "Singing Bush"]
        return random.choice(asCustomers)

class Customer(Person):
    def __init__(self):
        super().__init__() # Just grabs a name for customer_name attribute
        self.order = Order() # Just sets a number 1-20 for burger_count attribute

# Create a queue of 100 customers
customer_queue = []
for i in range(100):
    customer = Customer() # Create new customer object with name and burger amount, basically.
    customer_queue.append(customer) # Add that to the list, does 100 times.

# print(customer_queue) #Shows the addresses in the list for each customer object. Not required

# Create a dictionary to store the burger count for each customer
customer_dict = {}

# Loop through the customer queue and update the dictionary
for customer in customer_queue:
    name = customer.customer_name
    burgers_ordered = customer.order.burger_count
    if name in customer_dict:
        customer_dict[name] += burgers_ordered
    else:
        customer_dict[name] = burgers_ordered

# Sort the dictionary by the burger count in descending order
list_sorted_customers = sorted(customer_dict.items(), key=lambda x: x[1], reverse=True)

# Print the results
print("Customer Name".ljust(19), "Burgers Ordered")
print("-" * 40)
for customer in list_sorted_customers:
    name = customer[0].ljust(19)
    burgers = str(customer[1])
    print(name, burgers)
