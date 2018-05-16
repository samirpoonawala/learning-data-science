attendees = ["Ken", "Alena", "Treasure"]
attendees.append("Ashley")
attendees.extend(["James", "Gill"])
optional_attendees = ["Ben", "Brooke", "Bill"]
potential_attendees = attendees + optional_attendees

print("There are ", len(potential_attendees), "potential attendees currently")

to_line = ", ".join(attendees)
cc_line = ", ".join(optional_attendees)
print("To: " + to_line)
print("To: " + cc_line)