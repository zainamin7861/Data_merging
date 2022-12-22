import csv
data = []

with open("dwarf_stars.csv","r")as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        data.append(row)

headers = data[0]
planet_data = data[1:]

for i in planet_data:
    i[0] = i[0].lower()
planet_data.sort(key=lambda planet_data:planet_data[0])


with open("dwarf_stars_sorted.csv","w",newline = '\n')as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planet_data)