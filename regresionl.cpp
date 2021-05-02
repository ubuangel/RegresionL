
#include<iostream>
#include<bits/stdc++.h>
#include <ctime>
#include <math.h>
using namespace std;
//regresion 


//como clacular los los puntos 

bool personalizar_sort(double a,double b){
	double a1=(a-0);
	double b1=(b-0);
	return a1<b1;
	}


int main(){

int x[]={1,2,4,3,5};
int y[]={1,3,3,2,5};

//hipotesis
//y=w0+w1[dx]
//calculo de error
double w0=0;
double w1=0;
double error;
vector<double>err;

double learning=0.01;
for (int i =0;i <20;i++){
	int dx=i%5;
	//prediccion
	double p=w0+w1*x[dx];
	
//e=p(i)-y(i)
	 error=p-y[dx];
//	actualizando pesos
	w0=w0-learning*error;
	w1=w1-learning*error*x[dx];

cout<<" w0= "<<w0<<" w1= "<<w1<<" error"<<error<<endl;
	}
	err.push_back(error);
	
	cout<<"el menor error "<<endl;
	sort(err.begin(),err.end(),personalizar_sort);
	cout<<" w0= "<<w0<<" w1= "<<w1<<" error"<<err[0]<<endl;
	
	

}

//calculo de las derivadas

//(1/n)*sumatoria(yi-hx)(-1) derivada respecto a w0










