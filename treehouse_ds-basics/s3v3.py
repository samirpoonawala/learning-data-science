from s3v2 import *

gucci_ties = filter_col_by_string(data_from_csv, "brandName", "Gucci")
jcrew_ties = filter_col_by_string(data_from_csv, "brandName", "J.Crew")

max_gucci = find_max(gucci_ties[1:], 2)
max_jcrew = find_max_min(jcrew_ties[1:], 2)

message = "{} {} tie price is = ${:03.2f}"
#print(message.format("Maximum", "Gucci", max_gucci))
#print(message.format("Maximum", "J.Crew", max_jcrew))

avg_gucci = find_average(gucci_ties, True)
avg_jcrew = find_average(jcrew_ties, True)
#print(message.format("Average", "Gucci", avg_gucci))
#print(message.format("Average", "J.Crew", avg_jcrew))

striped_ties = filter_col_by_string(data_from_csv, "print", "_striped")
print_ties = filter_col_by_string(data_from_csv, "print", "_print")
paisley_ties = filter_col_by_string(data_from_csv, "print", "_paisley")
solid_ties = filter_col_by_string(data_from_csv, "print", "_solid")

message2 = "{}\t${:03.2f}"
#print("Print\tAverage")
#print(message2.format("striped", find_average(striped_ties)))
#print(message2.format("print", find_average(print_ties)))
#print(message2.format("paisley", find_average(paisley_ties)))
#print(message2.format("solid", find_average(solid_ties)))

