import matplotlib.pyplot as plt

food = [Pizza, noodles, idli]
slices = [6,4,8]
colors= [orange, green, aqua] 
plt.pie(slices, labels = food, colors- colors,
        startangle=90, shadow = False, explode = (0,0,0), radius = 1.6, autopct = '%5.5f%%')

plt.legend()

plt.show()