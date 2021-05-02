
#include<iostream>
#include <ctime>
#include <math.h>
using namespace std;
//regresion 


//como clacular los los puntos 

int main(){

int x[]={1,2,4,3,5};
int y[]={1,3,3,2,5};

//hipotesis
//y=w0+w1[dx]
//calculo de error
double w0=0;
double w1=0;

double learning=0.01;
for (int i =0;i <20;i++){
	int dx=i%5;
	//prediccion
	double p=w0+w1*x[dx];
	
//e=p(i)-y(i)
	double error=p-y[dx];
//	actualizando pesos
	w0=w0-learning*error;
	w1=w1-learning*error*x[dx];

cout<<" w0: "<<w0<<" w1 "<<w1<<" error"<<error<<endl;
	}

}

//calculo de las derivadas

//(1/n)*sumatoria(yi-hx)(-1) derivada respecto a w0










