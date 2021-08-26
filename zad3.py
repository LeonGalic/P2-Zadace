import re

string = str(input("Unesite neki string: "))
string = string.lower()

regex = "^l.*[0-5]\s.*g$" 

result = re.findall(regex, string)

if result:
  print("Podudaranje")
else:
  print("Nema podudaranja")  