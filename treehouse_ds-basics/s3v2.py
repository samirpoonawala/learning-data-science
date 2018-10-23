from s3v1 import *

def filter_col_by_string(data_sample, field, filter_condition):
  filtered_rows = []
  
  col = int(data_sample[0].index(field))
  filtered_rows.append(data_sample[0])
  
  for item in data_sample[1:]:
    if item[col] == filter_condition:
      filtered_rows.append([str(x).encode('utf8') for x in item])
  
  return filtered_rows

silk_ties = filter_col_by_string(data_from_csv, "material", "_silk")
wool_ties = filter_col_by_string(data_from_csv, "material", "_wool")
cotton_ties = filter_col_by_string(data_from_csv, "material", "_cotton")
gucci_ties = filter_col_by_string(data_from_csv, "brandName", "Gucci")


def filter_col_by_float(data_sample, field, direction, filter_condition):
  filtered_rows = []
  
  col = int(data_sample[0].index(field))
  cond = float(filter_condition)
  
  for row in data_sample[1:]:
    element = float(row[col])
    
    if direction == "<":
      if element < cond:
        filtered_rows.append(row)
    elif direction == "<=":
      if element <= cond:
        filtered_rows.append(row)
    elif direction == ">":
      if element > cond:
        filtered_rows.append(row)
    elif direction == ">=":
      if element >= cond:
        filtered_rows.append(row)
    elif direction == "==":
      if element == cond:
        filtered_rows.append(row)  
    else:
      pass
  return filtered_rows


under_20_bucks = filter_col_by_float(data_from_csv, "priceLabel", "<=", 20)
# print("Found {} ties < $20".format(number_of_records(under_20_bucks)))