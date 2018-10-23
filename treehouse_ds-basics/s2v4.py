from s2v3 import *

def find_average(data_sample, header=False):
  if header:
    data_sample = data_sample[1:]
  total = calculate_sum(data_sample)
  size = number_of_records(data_sample)
  average = total / size
  return average

average_price = find_average(data_from_csv, True)

midpoint = round(number_of_ties / 2)
message = "Average of {} half = ${:03.2f}"
#print(message.format("1st", find_average(data_from_csv[:midpoint], True)))
#print(message.format("2nd", find_average(data_from_csv[midpoint:], False)))
