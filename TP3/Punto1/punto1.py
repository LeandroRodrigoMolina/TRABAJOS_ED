import re

patron = "\\(0345\\)\s[0-9]{2}[0-9]{7}|\\+549345[0-9]{7}|^345[0-9]{7}$"
print("Patron:", patron)

print(re.findall(patron, "(0345) 154123456"))
print(re.findall(patron, "+5493454123456"))
print(re.findall(patron, "3454123456"))
print(re.findall(patron, "345412345632"))