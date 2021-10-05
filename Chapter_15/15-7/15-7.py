from die import Die
import pygal

die_1 = Die(8)
die_2 = Die(8)

results = []
for i in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

frequencies = []
for j in range(2, 17):
    frequencies.append(results.count(j))

hist = pygal.Bar()

hist.title = "Result of rolling two D8 dice 1000 times"
hist.x_labels = range(2, 17)
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D8 + D8', frequencies)
hist.render_to_file('15-7.svg')
