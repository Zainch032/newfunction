class Product:
  def __init__(self, name, amount, price):
      self.name = name
      self.amount = amount
      self.price = price

  def get_price(self, quantity):
      if quantity < 10:
          return self.price * quantity
      
      if quantity >= 10 and quantity <= 99:
          total_price = self.price * quantity
          discount = (total_price) * (10/100)
          return total_price - discount
      
      if quantity >= 100:
          total_price = self.price * quantity
          discount = (total_price) * (20/100)
          return total_price - discount
def make_purchase(self, quantity):
      pass