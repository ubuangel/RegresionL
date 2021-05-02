
#include<iostream>
#include <ctime>
#include <math.h>
using namespace std;
//regresion 




//como clacular los los puntos 
//calculo de la hipotesis 

int hx(int w0,int w1,int x){
	
		
	return w0+w1*x;
	
	}


//calculo de error
void error(int n,int prediccion[]){
	int err,suma;
	
	for (int iter=0;iter<n;iter++){
		suma=suma+(prediccion[iter]-hx(prediccion[iter],a,b);
	}
	 
	for(int iter=0;iter<n;iter++){
	err=(1/2*n)*pow(suma,2);
	
		}

	}

//calculo de las derivadas

//(1/n)*sumatoria(yi-hx)(-1) derivada respecto a w0
//(1/n)*sumatoria(yi-hx)(-x) derivada respecto a w1

void gradiente(int  learning,int epocas,int prediccion[]){

int i;
while(i<epocas){
	int teta=0;
	int sumatoria=0;
	int derivada;
	for (int t=0;t<6;t++){
	
	sumatoria=sumatoria+(prediccion[i]-hx(a,b,c))
	derivada=(1/n)*sumatoria*(-1);
	teta=teta+learning*derivada;
	
	
	}
	i++;	
	}
		}

//calculo de la gradiente 

	
	int main(){
	
	cout<<"regresionn lineal modificar parametros y hiper parametros"<<endl;
		
		srand(time(NULL));
	int a,b,x;
	int prediccion[6];
	
	
	for (int i=0;i<6;i++){
		a=rand()%(10-1)+1;
		 b=rand()%(10-1)+1;
		 x=rand()%(10-1)+1;
		 
		prediccion[i]= hx(a,b,x);
		 }
	for (int i=0;i<6;i++){
		
		cout<<prediccion[i]<<" ";
		
		}
	
	
	}
//










