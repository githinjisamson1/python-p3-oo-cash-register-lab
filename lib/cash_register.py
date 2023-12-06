#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
      # initialization
        self.discount = discount
        self.total = 0
        self.items = []
        
        # attribute to keep track of the last transaction
        self.lastTransaction = 0

    def add_item(self, title, price, quantity=None):
      # if quantity is provided
        if quantity:
            self.total += price * quantity
            
            # append each item to items list
            for item in range(quantity):
                self.items.append(title)

            # update lastTransaction
            self.lastTransaction = price * quantity
        else:
            self.total += price

            self.items.append(title)

            self.lastTransaction = price

    def apply_discount(self):
      # if discount is provided
        if self.discount:
            self.total -= int(self.discount/100 * self.total)
            
            print(f"After the discount, the total comes to ${self.total}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
      # subtracts the last item from the total
        self.total -= self.lastTransaction
