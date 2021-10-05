import csv
from datetime import datetime
from matplotlib import pyplot as plt

dates, highs_new_york, lows_new_york, highs_honolulu, lows_honolulu = [], [], [], [], []

with open("new_york_weather_2020.csv") as f1:
    reader = csv.reader(f1)
    head_reader = next(reader)

    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        dates.append(current_date)

        high_new_york = int(row[4])
        highs_new_york.append(high_new_york)

        low_new_york = int(row[5])
        lows_new_york.append(low_new_york)

with open("honolulu_weather_2020.csv") as f2:
    reader = csv.reader(f2)
    head_reader = next(reader)

    for row in reader:

        high_honolulu = int(row[4])
        highs_honolulu.append(high_honolulu)

        low_honolulu = int(row[5])
        lows_honolulu.append(low_honolulu)

fig = plt.figure(dpi=128, figsize=(10, 6))

plt.plot(dates, highs_new_york, c='red')
plt.plot(dates, highs_honolulu, c='orange')
plt.plot(dates, lows_new_york, c='blue')
plt.plot(dates, lows_honolulu, c='green')

plt.fill_between(dates,
                 highs_new_york,
                 lows_new_york,
                 facecolor='yellow',
                 alpha=0.2)
plt.fill_between(dates,
                 highs_honolulu,
                 lows_honolulu,
                 facecolor='purple',
                 alpha=0.2)

plt.title("16-2 High and Low Temperatures in New York and Honolulu")
plt.xlabel('', fontsize=16)
plt.ylabel("Temperature (F)", fontsize=16)
fig.autofmt_xdate()

plt.show()
