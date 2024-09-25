
import matplotlib.pyplot as plt
import numpy as np

# plot simple sin & cos function

plt.style.use('classic')

x = np.linspace(1,10,200)
plt.title("graph")
# fig=plt.figure()
plt.plot(x,np.sin(x))
plt.plot(x,np.cos(x))
plt.show()  


x=np.linspace(0,10,200)
fig=plt.figure()
plt.plot(x,np.sin(x),'-')
plt.plot(x,np.cos(x),'-')
fig.savefig('My_fig.png')