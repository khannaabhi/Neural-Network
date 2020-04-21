from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

fig = plt.figure()

chart = fig.add_subplot(1,1,1,projection='3d')

X,Y,Z = [1,2,3,4],[2,5,6,7],[4,6,2,6]
Xx,Yy,Zz = [-1,-2,-3,-4],[-2,-5,-6,-7],[-4,-6,-2,-6]

chart.scatter(X,Y,Z,c='green',marker='o')
chart.scatter(Xx,Yy,Zz,c='red',marker='^')

chart.set_xlabel('x axis')
chart.set_ylabel('y axis')
chart.set_zlabel('z axis')

plt.show()
