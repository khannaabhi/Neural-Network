import matplotlib
import matplotlib.pyplot as pt

# pt.plot([1,2,3,4],[3,8,10,12])

# pt.title("Rain")
# pt.xlabel("Rain in Jan")
# pt.ylabel("Rain in inches")
# pt.show()

# readFile = open("note.txt","r")
# data = readFile.read().split("\n")

# x = []
# y = []

# for i in data:
#   val = i.split(",")
#   x.append(int(val[0]))
#   y.append(int(val[1]))

# pt.plot(x,y)
# pt.title("Rain")
# pt.xlabel("Rain in Jan")
# pt.ylabel("Rain in inches")
# pt.show()

fig = pt.figure()
rect = fig.patch
rect.set_facecolor('lightblue')

x = [1,2,3,4,5,6,7,8,9]
y = [23,45,75,34,73,46,35,42,53]
x1 = [1,3,5,7]
y1 = [53,63,24,46]


graph1 = fig.add_subplot(3,1,1)
graph1.plot(x,y,'red',linewidth=2.0)
graph1.set_facecolor('grey')
graph1.tick_params(axis="x",color="yellow")
graph1.tick_params(axis="y",color="yellow")

graph1.spines["top"].set_color('blue')
graph1.spines["bottom"].set_color('blue')
graph1.spines["left"].set_color('blue')
graph1.spines["right"].set_color('blue')

graph1.set_xlabel('x-axis',color='white')
graph1.set_ylabel('y-axis',color='white')
graph1.set_title("Random graph",color="white")

graph2 = fig.add_subplot(3,1,3)
graph2.plot(x1,y1,'green',linewidth=2.0)
graph2.set_facecolor('grey')
graph2.tick_params(axis="x",color="yellow")
graph2.tick_params(axis="y",color="yellow")

graph2.spines["top"].set_color('pink')
graph2.spines["bottom"].set_color('pink')
graph2.spines["left"].set_color('pink')
graph2.spines["right"].set_color('pink')

graph2.set_xlabel('x-axis',color='white')
graph2.set_ylabel('y-axis',color='white')
graph2.set_title("Random graph",color="white")

pt.show()
