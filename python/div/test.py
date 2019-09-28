from matplotlib import pyplot as plt
from datetime import datetime
from dateutil import parser
import csv

filename = 'data/ten.csv'

with open(filename) as data:
    reader = csv.reader(data)
    header_row = reader.next()

    stations = []
    dates = []
    for row in reader:
        stations.append(int(row[0]))
        # 2017-06-01 02:17:05 +0200
        dates.append(parser.parse(row[1]))

fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(stations, c='red')

plt.title('Stations', fontsize=12)
plt.xlabel('', fontsize=12)
plt.ylabel('ID', fontsize=12)
plt.tick_params(axis='both', which='major', labelsize=12)

plt.show()

print(stations)