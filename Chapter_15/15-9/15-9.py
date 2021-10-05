from die import Die
import pygal

die_1 = Die(6)
die_2 = Die(6)

results = []
for i in range(1000):
    result = die_1.roll() * die_2.roll()
    results.append(result)
"""
x_set = set()
for result in results:
    x_set.add(result)

x_labels = []
while len(x_set) > 0:
    x_labels.append(x_set.pop())
x_labels.sort()
"""
frequencies = []
for j in range(1, 37):
    frequencies.append(results.count(j))

hist = pygal.Bar()

hist.title = "Result of rolling three D6 dices 1000 times"
hist.x_labels = range(1, 37)
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 * D6', frequencies)
hist.render_to_file('15-9.svg')
