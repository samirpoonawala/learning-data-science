# coding: utf-8

# demo.py
# Intro to Data Science with Python
# Author: Kat Chuang
# Created: Nov 2014

# --------------------------------------

from my_utils import *
from numpy_utils import *

# --------------------------------------

# Reading Data.CSV

sample_file = 'data.csv' 

### Loading data into a data structure (list of lists)
print("Reading file... ", sample_file)

data_from_csv = open_with_csv(sample_file)  # read in data to nested lists
my_csv = load_data(sample_file)             # read in the data captured using numpy

#Stage 2 
how_many = "Processed {} rows in {}, including header.".format(number_of_records(data_from_csv), sample_file)
print(how_many)
size(my_csv)  # show length using numpy array

the_sum = calculate_sum(data_from_csv)
print("The Sum: $", the_sum)

price = my_csv['priceLabel']
my_sum = calculate_numpy_sum(price)
print("The Sum (calculated with numpy.sum): $", my_sum)
print("Average:", find_average(data_from_csv, True))

midpoint = round(len(data_from_csv)/2)
print("Average of first half", find_average(data_from_csv[:midpoint], True))
print("Average of last half", find_average(data_from_csv[midpoint:], False))

price_in_float = [float(item) for item in price]
print("Average (numpy):", find_numpy_average(price_in_float))


print("\n \tHigh\tLow")
print("lists\t", "${}\t ${}".format(find_max(data_from_csv[1:], 2), find_min(data_from_csv[1:], 2) ))
print("numpy\t", "${}\t ${}".format(numpy_max(price_in_float), numpy_min(price_in_float) ))

# Stage 3
my_improved_csv = create_bool_field_from_search_term(data_from_csv, "cashmere")
print("Creating a new column to mark ties made of cashmere...")
cashmere_ties = filter_col_by_bool(my_improved_csv, 11)
count_cashmere_ties = number_of_records(cashmere_ties)
print("Found ", count_cashmere_ties, "ties made with cashmere")

### Filtering Ties by string
# Look at ties of brand Hermes vs JCrew
gucci_ties = filter_col_by_string(data_from_csv, "brandName", "Gucci")
jcrew_ties = filter_col_by_string(data_from_csv, "brandName", "J.Crew")
print("Found ", len(gucci_ties), "Gucci Ties and", len(jcrew_ties), "J.Crew Ties")

# Only look at rows of "silk" ties or only "wool"
silk_ties = filter_col_by_string(data_from_csv, "material", "_silk")
wool_ties = filter_col_by_string(data_from_csv, "material", "_wool")
print("Found ", len(silk_ties), "silk ties and", len(wool_ties), "wool ties")

# Look at ties < $20 vs ties over $100
under_20_dollars = filter_col_by_float(data_from_csv, "priceLabel", "<=", 20)
over_100_dollars = filter_col_by_float(data_from_csv, "priceLabel", ">=", 100)
print("Found ", len(under_20_dollars), " ties < $20 and", len(over_100_dollars), " ties < $100")

print("3.c Grouping rows")
max_gucci_tie_price = find_max(gucci_ties[1:], 2)
max_jcrew_tie_price = find_max(jcrew_ties[1:], 2)
print("Maximum Gucci Tie Price is: ", '{:03.2f}'.format(max_gucci_tie_price))
print("Maximum J.Crew Tie Price is: ", '{:03.2f}'.format(max_jcrew_tie_price))

# Printed vs Solid. Are the printed ties cheaper? 
avg_print_ties = find_average(filter_col_by_string(data_from_csv, "print", "_print"))
avg_paisley_ties = find_average(filter_col_by_string(data_from_csv, "print", "_paisley"))
avg_striped_ties = find_average(filter_col_by_string(data_from_csv, "print", "_striped"))
avg_solid_ties = find_average(filter_col_by_string(data_from_csv, "print", "_solid"))
print("Are printed ties cheaper?")
print("Print\tAverage Price")
print("Paisley\t{}".format(avg_paisley_ties))
print("Stripes\t{}".format(avg_striped_ties))
print("Print\t{}".format(avg_print_ties))
print("Solid\t{}".format(avg_solid_ties))

# Stage 4 
write_to_file("_data/04-gucci_ties.csv", gucci_ties)
write_to_file("_data/04-jcrew_ties.csv", jcrew_ties)

#numpy.savetxt("_data/04-numpy_wool_ties.csv", wool_ties, delimiter=",", fmt="%s")
solid_silk_ties = filter_col_by_string(data_from_csv, "print", "_solid")
#numpy.savetxt("_data/04-numpy_silk_ties.csv", solid_silk_ties, delimiter=",", fmt="%s")

## Writing more functions to export csv files
write_brand_and_price_to_file('_data/04-gucci-price.csv', gucci_ties)
write_min_max_csv('_data/04-min_max.csv', gucci_ties[1:])
write_two_cols('_data/04-two_cols.csv', gucci_ties[1:], 3, 7)
write_append_file('_data/04-gucci_and_jcrew.csv', jcrew_ties[1:])

write_sorted_prices('_data/write_sorted_price.csv', gucci_ties[1:], "ascending")

# How many brands? How many colors are represented?
# What price range is represented?

kiton_ties = filter_col_by_string(data_from_csv, "brandName", "Kiton")
save_spreadsheet('_data/04-kiton.xlsx', kiton_ties)

print("Created these files: 04-gucci-price.csv, 04-min_max.csv, 04-two_cols.csv, 04-gucci_and_jcrew.csv, 04-kiton.xlsx")

# Stage 5
create_line_chart(prices_of(gucci_ties), "Distribution of Prices for Gucci Ties", "_charts/05-line_hermes.png")
#compare to gucci bar chart

create_line_chart(prices_of(jcrew_ties), "Distribution of Prices for J.Crew Ties", "_charts/05-line_jcrew.png")
create_line_chart(prices_of(kiton_ties), "Distribution of Prices for Kiton Ties", "_charts/05-line_kiton.png")

print("Created these files: 05-line_hermes.png, 05-line_jcrew.png, 05-line_kiton.png")

plot_all_bars(price_in_float,  "_charts/05-all_prices.png")
print("_charts/created 05-all_prices.png")

price_groups = group_prices_by_range(price_in_float)
create_bar_chart(price_groups, "_charts/05-price_in_groups.png") 
print("created 05-price_in_groups.png")

brands = my_csv['brandName']
columns = ["$0-50", "$50-100", "$100-150", "$150-200", "$200-250", "$250+"]
write_brand_and_price_to_file("_data/05-temp-table.csv", data_from_csv)
brand_and_price_data = open_with_csv("_data/05-temp-table.csv", d=',')
create_table(brand_and_price_data, price_groups, brands, columns, "_charts/05-prices_in_table.png") 
print("created 05-prices_in_table.png")

print("5.d quickly check to see if there might be discounted items for these brands...")
my_list = ["Burberry", "Dolce & Gabbana", "Gucci", "Yves Saint Laurent"]
for x in my_list:
    print_brand_avg_min(x, data_from_csv)

# Stage 6 

labels = ["$0-50", "$50-100", "$100-150", "$150-200", "$200-250", "$250+"] 
plot1 = plot_minimal_graph(price_groups, labels)
table_text = build_table_text(brand_and_price_data, brands)
plot2 = plot_graph_with_table(table_text[0], table_text[1], labels)

pp = PdfPages('foo.pdf')
pp.savefig(plot1, bbox_inches='tight')
pp.savefig(plot2, bbox_inches='tight')
pp.close()
