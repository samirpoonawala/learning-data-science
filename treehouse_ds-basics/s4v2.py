from s4v1 import *

def write_brand_and_price_file(filename, data_sample):
  brand_field_index = 5
  price_field_index = 2
  
  new_array = []
  for record in data_sample:
    new_record = [None] * 2
    new_record[0] = record[brand_field_index]
    new_record[1] = record[price_field_index]
    new_array.append(new_record)
  
  write_to_file(filename, new_array)
  
write_brand_and_price_file('_data/s4-brand_and_price.csv', gucci_ties)

def write_min_max_csv(filename, data_sample):
  min = find_max_min(data_sample, 2, "min")
  max = find_max_min(data_sample, 2, "max")
  
  new_array = []
  for record in data_sample:
    if (float(record[2]) == min) or (float(record[2]) == max):
      new_array.append(record)
  
  write_to_file(filename, new_array)
  
write_min_max_csv('_data/s4-min_max.csv', gucci_ties[1:])

def write_two_cols(filename, data_sample, col1, col2):
  new_array = []
  for record in data_sample:
    new_record = [None] * 2
    new_record[0] = record[col1]
    new_record[1] = record[col2]
    new_array.append(new_record)
    
  write_to_file(filename, new_array)
  
write_two_cols('_data/s4-write_two_cols.csv', gucci_ties[1:], 3, 7)

def write_append_file(filename, new_data_to_add):
  with open(filename, "a") as myfile:
    for row in new_data_to_add:
      myfile.write(str(row))
      
      
write_to_file('_data/s4_gucci_and_jcrew.csv', gucci_ties) 
write_append_file('_data/s4_gucci_and_jcrew.csv', jcrew_ties)