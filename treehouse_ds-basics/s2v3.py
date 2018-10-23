from s2v2 import *

def calculate_sum(data_sample):
  total = 0
  for row in data_sample[1:]:
    price = float(row[2])
    total += price
  return total

def calculate_sum_succinct(data_sample):
  prices = [float(row[2]) for row in data_sample[1:]]
  return sum(prices)

def calculate_sum_concise(data_sample):
  prices = list(map(lambda x: float(x[2]), data_sample[1:]))
  return sum(prices)
  
#print(calculate_sum_concise(data_from_csv))
#print(calculate_sum_succinct(data_from_csv))

def calc_numpy_sum(price):
  prices_in_float = [float(line) for line in price]
  total = numpy.sum(prices_in_float)
  return total

price = my_csv['priceLabel']
my_sum = calc_numpy_sum(price)
# print("The sum (numpy):", my_sum)

