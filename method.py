def factorial(n):
  if n == 0:
    return 1
  return n * factorial(n-1)

def combination(m,n):
  if n == 0:
    return 1
  return int(m/n * combination(m-1,n-1))

def permutation(m,n):
  if n == 0:
    return 1
  return m * permutation(m-1,n-1)

def fibonacci(n):
  if n == 1 or n == 2:
    return 1
  return fibonacci(n-1) + fibonacci(n-2)

def power(n,m):
  if m == 0:
    return 1
  return n * power(n,m-1)

def triangular(n):
  if n == 1:
    return 1
  m = triangular(n-1)
  return n + m

def max(array):
  num = array[0]
  for i in range(1, len(array)):
    if array[i] > num:
      num = array[i]
  return num

def max(array):
  num = array[0]
  i = 1
  while i < len(array):
    if array[i] > num:
      num = array[i]
    i += 1
  return num

def index(array, n):
  i = 0
  for i in range(len(array)):
    if array[i] == n:
      return i
  raise ValueError



n = fibonacci(7)
print(n)