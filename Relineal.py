import numpy as np
import matplotlib.pyplot as plt

x_ds=[i for i in range (100)]
y_ds=[i+np.random.normal(0,5) for i in x_ds]	




def h(x,w):
	return w[0]+w[1]*x
	
w=np.random.rand(2)
print(w)
y_prediccion=[h(i,w) for i in x_ds]


#for i in x_ds:
#	y_prediccion=h(i,w) #voy aplicar una funcion h a cada elemento i pero cada elemto i esta en el conjunto x_ds
#plt.plot(x_ds,y_ds,'*')#nube de puntos
#plt.plot(x_ds,y_prediccion)#prediccion


#mse
#mse

def error(y,x,w):
	return sum( [ (e[0] - h(e[1],w))**2 for  e in zip(y,x) ])/(2*len(y))
	
print(error)


plt.plot(x_ds,y_ds,'*')#nube de puntos
plt.plot(x_ds,y_prediccion)#prediccion
#otra forma
#def error(x,y,w):
#for i in range(len(y))
#	suma=suma+(y[i]-h(x[i],w))**2
#	return suma/2*len(y)
	
#creamos un algoritmo de aprendisaje


