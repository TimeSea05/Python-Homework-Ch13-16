from die import Die
import pygal

die_1 = Die(6)
die_2 = Die(6)
die_3 = Die(6)

results = []
for i in range(1000):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)

frequencies = []
for j in range(3, 19):
    frequencies.append(results.count(j))

hist = pygal.Bar()

hist.title = "Result of rolling three D8 dices 1000 times"
hist.x_labels = range(3, 19)
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D8 + D8', frequencies)
hist.render_to_file('15-8.svg')
