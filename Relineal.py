import numpy as np
import matplotlib.pyplot as plt

x_ds=[i for i in range (100)]
y_ds=[i*np.random.normal(0,5) for i in x_ds]	




def h(x,w):
	return w[0]+w[1]*x
	
w=np.random.rand(2)
print(w)
y_prediccion=[h(1,w) for i in x_ds]

plt.plot(x_ds,y_ds,'*')
plt.plot(x_ds,y_prediccion)
#for i in x_ds:
#	y_p=h(i,w)#voy aplicar una funcion h a cada elemento i pero cada elemto i esta en el conjunto x_ds
