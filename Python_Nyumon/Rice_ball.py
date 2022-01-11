class Rice_ball:

  def __init__(self, id: int, name: str, price: int):
    self.id = id
    self.name = name
    self.price = price
  
  def raise_price(self, markup: int=10) -> int:
    self.price += markup
    return self.price

print(Rice_ball.__doc__)