import numpy as np
import matplotlib.pyplot as plt

x_ds=[i for i in range (20)]
y_ds=[i+np.random.normal(0,5) for i in x_ds]	


def h(x,w):
	return w[0]+w[1]*x
	

#print(w)



#for i in x_ds:
#	y_prediccion=h(i,w) #voy aplicar una funcion h a cada elemento i pero cada elemto i esta en el conjunto x_ds
#plt.plot(x_ds,y_ds,'*')#nube de puntos
#plt.plot(x_ds,y_prediccion)#prediccion


#mse
#mse
#manera de lsitas pro compresion

def error(y,x,w):
	return sum( [ (e[0] - h(e[1],w))**2 for  e in zip(y,x) ])/(2*len(y))

w=np.random.rand(2)

y_prediccion=[h(i,w) for i in x_ds]

	
print("error mse"+str( error(y_ds,x_ds,w)))


plt.plot(x_ds,y_ds,'*')#nube de puntos
plt.plot(x_ds,y_prediccion)#prediccion
#otra forma
#def error(x,y,w):
#for i in range(len(y))
#	suma=suma+(y[i]-h(x[i],w))**2
#	return suma/2*len(y)
	
#calcular las derivadas
#def grad(y,x,w):
#	gra_w0= sum ([(e[0] -h(e[1],w))*(-1) for e in zip(y,x)])/len(y)
#	gra_w1= sum ([(e[0] -h(e[1],w))*(-e[1]) for e in zip(y,x)])/len(y)
#	return gra_w0,gra_w1
#	
##creamos un algoritmo de aprendisaje


#def train(x_ds,y_ds,w,epochs,alpha):
#	for i in range(epochs):
#		err=(y_ds,x_ds,w)
#		#print(err)
#		grad_w0=grad(y_ds,x_ds,w)
#		grad_w1=grad(y_ds,x_ds,w)
#	
#		w[0]=w[0]-alpha*grad_w0
#		w[1]=w[1]-alpha*grad_w1
#	

#train(x_ds,y_ds,w,100,0.0001)
