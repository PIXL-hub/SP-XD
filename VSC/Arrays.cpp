#include<iostream>
using namespace std;

int main()
{
    
// Array
    int Size = 5;
    string Array[Size];
    cout<<" *Enter the elements* " <<endl;
// For statement to get input from user
    for (int i=0; i<Size; i++)
    {
       cout<<"Enter Name of ; "<< "["<< i+1 <<"]" << endl;
       cin>>Array[i];
    }
// For statement to display values of array
    cout<< "***Array***" <<endl;
    for (int i=0; i<Size; i++)
    {
        cout<<Array[i]<< " " << endl;
    }
    
//Shifting elements after the input from the user
    int siz = 5;    
    int elements = 0;
    int index = 0;
    int Arr[siz] = {10,20,30,40,50};

    cout<< "***Array Before Edition**" <<endl;
    for (int i=0; i<siz; i++)
    {
        cout<<Arr[i]<< " " << endl;
    }

    cout<< "Enter elements you want to insert: ";
    cin>>elements;cout<<endl;
    cout<< "Enter index that you want locate: ";
    cin>>index;cout<<endl;

    if(index>siz)
    {
        cout<< "invalid value";
    }

    else
    {
        for(int i=siz; i>index; i--)
        {
            //Shifting code
            Arr[i] = Arr[i-1]; 
        }
        Arr[index] = elements;
        siz++;

        cout<< "***Array After Edition**" <<endl;
    for (int i=0; i<siz; i++)
    {
        cout<<Arr[i]<< " " << endl;
    }
    cout<< endl;
    
    }
// Deleting an Element From an Array 
    int Size1 = 5;
    int element = 0;
    int ARRAY[Size1] = {10, 20, 30, 40, 50};
    int index1 =0;
    cout <<"Array before edition: ";
    for(int i=0; i<Size; i++)
    {
        cout<<ARRAY[i]<<" ";

    }
    cout<<"\n";
    cout<< "Enter an element that you want to delete\n";
    cin >> element;

    for(int i =1; i<Size; i++)
    {
        if (element == ARRAY[i])
        {
            //Knowing the index of element
            index1 = i; 
        }
    }

    for(int i= index1; i<Size1-1; i++)
    {
        //Shifting Code
        ARRAY[i] = ARRAY[i+1]; 
    }
    //Deleting the last Box
    Size--; 

    cout <<"Array after edition: \n";
    for(int i=0; i<Size1; i++)
    {
        cout<<ARRAY[i]<<" ";
    }
    cout<<endl;

    int size=6;
    int element2=0;
    int index2=0;
    int entity=0;
    int ARRA[size] = {11,64,28,20,88,4};

    for(int i=0;i<size;i++)
    {
        cout<<ARRA[i]<<" ";
    }
    cout<<"\n";

    cout<<"Enter the element that you want to search on: ";
    cin>>element2;cout<<endl;

    for(int y=0; y<size; y++)
    {
        if(element2 == ARRA[y])
        {
            index2 = y;
            entity++;
        }
    }

    if(entity ==1)
    {
        cout<<" Founded!\n";
        cout<< "Index of element is: "<< index <<endl;
    }
    else
    {
        cout<<"Not Founded!\n";
    }


    return 0;

}