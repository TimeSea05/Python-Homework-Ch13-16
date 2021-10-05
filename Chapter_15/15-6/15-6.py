import pygal
from die import Die

# 创建两个D6
die_1 = Die()
die_2 = Die()

# 掷几次骰子，并将结果存储在一个列表中
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# 分析结果
frequencies = []
max_result = die_1.num_sides + die_1.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

x_set = set()
for result in results:
    x_set.add(result)

x_labels = []
while len(x_set) > 0:
    x_labels.append(x_set.pop())
x_labels.sort()

# 对结果进行可视化
hist = pygal.Bar()

hist.title = "Result of rolling two D6 dice 1000 times."
hist.x_labels = x_labels
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D6', frequencies)
hist.render_to_file('15-6.svg')
