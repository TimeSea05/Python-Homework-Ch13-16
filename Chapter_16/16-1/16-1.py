import csv
from matplotlib import pyplot as plt
from datetime import datetime

with open("san_francisco_weather_2014.csv") as f:
    reader = csv.reader(f)
    header_low = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[5], "%Y-%m-%d")
        dates.append(current_date)

        high = int(row[12])
        highs.append(high)

        low = int(row[14])
        lows.append(low)

    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.title("Daily High and Low Temperatures in San Francisco, 2014",
              fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)")
    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.plot(dates, highs, c='orange')
    plt.plot(dates, lows, c='blue')

    plt.show()