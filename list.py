class list:
  def __init__(self, iter):
    self.iter = []
    if type(iter) == str:
      for i in range(len(iter)):
        self.iter += [iter[i]]
  
  def append(self, a):
    self.iter += [a]

a = list()
print(a)