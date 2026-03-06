#include<iostream>
using namespace std;

int main()
{
    
    cout <<"enter firs number ";
    int x;
    cin >>x;
    cout <<"enter op ";
    string y;
    cin>>y;
    cout <<"enter second number";
    int z;
    cin>>z;
    if (y == "+")
    {
        cout<<"summation is "<<x+z ;
    }

     if (y == "-")
    {
        cout<<"excretions is "<<x-z ;
    }

     if (y == "*")
    {
        cout<<"multiplication is "<<x*z ;
    }

     if (y == "/")
    {
        cout<<"quotient is "<<x/z ;
    }

     if (y == "%")
    {
        cout<<"Modals is "<<x%z ;
    }
    


    return 0;  
}