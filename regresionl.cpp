
#include<iostream>
#include <ctime>
#include <math.h>
using namespace std;
//regresion 


//como clacular los los puntos 
//calculo de la hipotesis 

int hx(int w0,int w1){
	int f;
	int tam=6;
	for (int i=0;i<tam;i++){
		
	 f=w0+w1*i;
	
	}
	return f;
	
	}


//calculo de error
void error(int n,int x[],int w0,int w1,int prediccion[]){
	int err,suma;
	
	for (int iter=0;iter<n;iter++){
		suma=suma+(prediccion[iter]-hx(w0,w1));
	}
	 
	for(int iter=0;iter<n;iter++){
	err=(1/2*n)*pow(suma,2);
	
		}

	}

//calculo de las derivadas

//(1/n)*sumatoria(yi-hx)(-1) derivada respecto a w0
//(1/n)*sumatoria(yi-hx)(-x) derivada respecto a w1

void gradiente(int n,int  learning,int epocas,int prediccion[],int w0,int w1){

int i;
	int teta;
while(i<epocas){
	int sumatoria=0;
	int derivada;
	for (int t=0;t<6;t++){
	
	sumatoria=sumatoria+(prediccion[t]-hx(w0,w1));
	derivada=(1/n)*sumatoria*(-1);
	teta=teta+learning*derivada;
	
	
		}
	i++;	
	}
	cout<<teta;
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
		 
		//prediccion[i]= hx(a,b,x);
		 }
	for (int i=0;i<6;i++){
		prediccion[i]=i;
		//cout<<prediccion[i]<<" ";
//		
		}
		gradiente(2,0.3,6,prediccion,2,3);

	
	
	}
//










