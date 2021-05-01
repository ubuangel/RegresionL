import numpy as np
import matplotlib.pyplot as plt

def h(x,w):
  return w[0] + w[1]*x


def Error(y,x,w):
 return sum( [ (e[0] - h(e[1],w))**2 for  e in zip(y,x) ])/(2*len(y))

def Error2(y,x,w):
 return sum( [ abs(e[0] - h(e[1],w)) for  e in zip(y,x) ])/(len(y))

def Error1(y,x,w):
  suma =0
  for i in range(len(y)):
    suma = suma + (y[i] - h(x[i],w ))**2
  return suma/(2*len(y))


w = np.random.rand(2)
y_pd  = [ h(i,w) for i in x_ds ]
plt.plot(x_ds,y_ds, '*')
plt.plot(x_ds,y_pd)

print("Error MSE :" + str(Error(y_ds, x_ds,w)))


# no modificar 
def grad(y,x,w):

  grad_w0 = sum([ (e[0] - h(e[1],w))*(-1)    for e in zip(y,x) ])/len(y)
  grad_w1 = sum([ (e[0] - h(e[1],w))*(-e[1]) for e in zip(y,x) ])/len(y)
  return grad_w0, grad_w1

def grad2(y,x,w):

  grad_w0 = sum([ (e[0] - h(e[1],w)/abs(e[0] - h(e[1],w))*(-1)    for e in zip(y,x) ])/len(y)
  grad_w1 = sum([ (e[0] - h(e[1],w)/abs(e[0] - h(e[1],w))*(-e[1]) for e in zip(y,x) ])/len(y)
  return grad_w0, grad_w1

def grad2_desdoblado(y,x,w):
  grad_w0=0
  grad_w1=0
  for e in zip(y,x):
    grad_w0=grad_w0+(e[0] - h(e[1],w)/abs(e[0] - h(e[1],w))*(-1))
    grad_w1=grad_w1+(e[0] - h(e[1],w)/abs(e[0] - h(e[1],w))*(-e[1]))
  return grad_w0/len(y),grad_w1/len(y)
  
  

x_ds = [i for i in range(20)]
y_ds = [ i + np.random.normal(0,1) for i in x_ds ]



    s    
w = np.random.rand(2) 

def train(x_ds, y_ds, w, epochs, alpha):
  list_error = []
  time = []
  for i in range(epochs):
    Err = Error(y_ds,x_ds,w)
    
    list_error.append(Err)
    time.append(i)
    grad_w0, grad_w1 = grad(y_ds,x_ds,w)
    w[0] = w[0] - alpha*grad_w0
    w[1] = w[1] - alpha*grad_w1
  return time,list_error
  


 
  
 


train(x_ds,y_ds, w, 1000,0.007)



plt.plot(x_ds, y_ds,'*')
plt.plot(x_ds, [ h(i,w) for i in x_ds])


