/*مثال لبرنامج يقوم بجمع الارقام الموجبة و إذا ادخل
 المستخدم رقم سالب يتم ايقاف البرنامج وجمع القيم
 الموجبة دون السالبة*/


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

sum=sum+number;
cout<<"enter a number";
cin>>number;


}

cout<<"\n\n The sum is"<<sum<<endl;



















    return 0;
}