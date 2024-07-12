import numpy as np
from matplotlib import pyplot as plt

ages_x = list(range(25,36))


x_indexes = np.arange(len(ages_x))
width = 0.25

dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]

plt.bar(x_indexes - width, dev_y, width=width, color="#e5ae38", label="All Devs")

py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]

plt.bar(x_indexes, py_dev_y, width=width, color="#008fd5", label="Python")


plt.legend()

plt.xticks(ticks=x_indexes, labels=ages_x)

plt.title("Median Salary (USD) by Age")
plt.ylabel("Ages")
plt.xlabel("Salaries")

plt.show()