#include<iostream>
using namespace std;
int enqueue(int , int);
int main()
{
  int Q[20];
  int head=1;
  int tail=1;
  int items=0;
  int size=length(Q);
  cout<<Q[1];
  enqueue(Q,1);
  cout<<Q[1];
}
int enqueue(int Q,int x)
{
  if(queueFull(Q)){cout<<"Error:Overflow!!!!"<<endl;}
  else
  {
  	Q[tail]=x;
    if(tail==size)
    {
    	tail=1;
    }
    else{
    	tail++;
    }
  }
  return Q
}
void queueFull(Q){
	return items==size;
}