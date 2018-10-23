from s2v4 import *

def find_max(data_sample, col):
  temp_list = []
  for row in data_sample:
    price = float(row[col])
    temp_list.append(price)
  return max(temp_list)

def find_min(data_sample, col):
  temp_list = []
  for row in data_sample:
    price = float(row[col])
    temp_list.append(price)
  return min(temp_list)

def find_max_min(data_sample, col, m='max'):
  temp_list=[]
  val = 0
  for row in data_sample:
    price = float(row[col])
    temp_list.append(price)  
  if m == "max":
    val = max(temp_list)
  elif m == "min":
    val = min(temp_list)
  else: #hopefully we don't come to this
    pass
  return val

#print(find_max_min(data_from_csv[1:], 2, 'min'))

price = my_csv['priceLabel']
price_in_float = [float(x) for x in price]
numpy_max = numpy.amax(price_in_float)
numpy_min = numpy.amin(price_in_float)

