#include<iostream>
using namespace std;

int main()
{
   

float number;
float sum = 0;

cout<<"enter a number";
cin>>number;

while(number >=0)

 {

sum += number;
cout<<"enter a number";
cin>>number;


}

cout<<"\n\n The sum is"<<sum<<endl;


    return 0;
}