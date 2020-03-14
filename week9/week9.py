import matplotlib
import matplotlib.pyplot as plt
import numpy as np

grades = ['Kindergarten','First grade','Second grade','Third grade','Fourth grade','Fifth grade','Sixth grade','Seventh grade','Eighth grade','Ninth grade','10th grade','11th grade','12th grade']
hours_needed = [9.5, 9.1, 9.3, 8.6, 8.9, 8.9, 8.6, 8.5, 8.5, 8.3, 8.4, 8.4, 8.0]
hours_averaged =[8.5, 8.4, 8.3, 8.1, 7.9, 7.8, 7.6, 7.3, 7.4, 7.1, 6.8, 6.9, 6.6]

x = np.arange(len(grades))  # the label locations
width = 0.35  # the width of the bars

matplotlib.rcParams.update({'font.size': 6})

fig, ax = plt.subplots()
bar1 = ax.bar(x - width/2, hours_needed, width, label='Hours Needed')
bar2 = ax.bar(x + width/2, hours_averaged, width, label='Hours Averaged')

ax.set_ylabel('Hours')
ax.set_xticks(x)
plt.xticks(rotation=45)
ax.set_xticklabels(grades)
ax.legend()

def autolabel(rects):
    """Attach a text label above each bar, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(bar1)
autolabel(bar2)

fig.tight_layout()

plt.show()
