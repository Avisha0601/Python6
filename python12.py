import matplotlib.pyplot as plt

activities = ['study', 'school', 'extracurricular', 'sports', 'sleep', 'eat']

slices = [6, 5, 2, 3, 7, 2]

colors=['magenta', 'aqua', 'red', 'green', 'purple', 'blue']

plt.pie(slices, labels = activities, colors=colors,
        startangle=90, shadow = False, explode = (0,0,0,0,0,0),
        radius =1.3, autopct = '%2.2f%%')

plt.legend()

plt.show()