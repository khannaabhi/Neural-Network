import matplotlib.pyplot as plt

sizes = [50,64,95,12,83]

colors = ['red','blue','grey','green','orange']

labels = ['Nokia','Moto','Samsung','Apple','Mi']

plt.pie(sizes,colors=colors,startangle=90,labels=labels)
plt.title('Mobile Brands')
plt.legend(title='Legend',loc='upper left')

plt.show()