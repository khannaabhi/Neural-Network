import matplotlib.pyplot as plt
import numpy as np

pos = np.arange(6)+0.5

names = ["a","b","c","d","e","f"]

plt.bar(pos,(2,4,5,6,5.7,7),align='center',color='green')

plt.xlabel("Students",color='black')
plt.ylabel("Height in FT",color='black')
plt.title("Height of Students")

plt.show()