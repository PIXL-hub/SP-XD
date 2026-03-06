#include <iostream>
#include <stdlib.h>
#include <ctime>
#include <cmath>
using namespace std;

                                                 //Functions Test
void def()
{
    cout << "hello!!!!\n";
}

// find the maximum number between three numbers.
void find(int num1, int num2, int num3)
{

    if (num1>num2 && num1>num2)
    {
        cout << num1 << "is the maximum number";
    }
     
    else if (num2>num3 && num2>num3)
    {
        cout << num2 << "is the maximum number";
    }

    else
    {
        cout << num3 << "is the maximum number";
    }
}

//Over Loading Function
void print()
{
    cout << "Hello!" << endl;
}

void print(int a)
{
    cout << "int is:" << a << endl;
}

int sum(int x, int z);

// Recursion & Factorial
    int get(int n)
    {
        if(n == 1)
        {
            return 1;
        }
            
        else
        {
            return 1+get(n-1);
        }
           

    }

    int fact(int n)
    {
        if(n == 1)
        {
            return 1;
        }
            
        else
        {
            return n * fact(n-1);
        }
           

    }



int sum(int x, int z);

int main()
{
    cout << "Hello World!\n";  
    cout << sum(2,4) << endl;
    def(); 
    //int x, y, z;
    //cout << "Enter three number\n";
    //cin >> x;
    //cin >> y;
    //cin >> z;
    //find(x, y, z);
    srand(static_cast<unsigned int>(time(0)));

    for (int i = 0; i<= 10;i++)
    {
         cout << rand()%2 << endl;
        //Start + rand() % (End - Start + 1);
        cout << "Random number between 5 and 15: " << 50 +rand() % (56-50+1)<<endl;
    }
   

    
                                            //Built in Function
    cout << "Hello World!\n";  
    float num = 25;
    cout << "Absolute value of num is: " << abs(num) << endl;
    cout << "Ceiling value of num is: " << ceil(num) << endl;
    cout << "Floor value of num is: " << floor(num) << endl;
    cout << "Round value of num is: " << round(num) << endl;
    cout << "Square root of 25 is: " << sqrt(25) << endl;
    cout << "2 raised to the power 3 is: " << pow(2, 3) << endl;
    cout << "Logarithm of 10 is: " << log(10) << endl;
    cout << "Sine of 90 degrees is: " << sin(90 * 3.14159 / 180) << endl;
    cout << "Cosine of 0 degrees is: " << cos(0 * 3.14159 / 180) << endl;
    cout << "Tangent of 45 degrees is: " << tan(45 * 3.14159 / 180) << endl;


                                            //Random Number Generation
    cout << "Hello World!\n";  
    // Seed the random number generator with the current time
    srand(static_cast<unsigned int>(time(0)));

    // Generate and print 10 random numbers between 0 and 99
    for (int i = 0; i < 10; ++i) 
    {
        int randomNum = rand() % 100; // Random number between 0 and 99
        cout << randomNum << endl;
    }


    //Function Prototypes
    cout << "Hello World!\n";  
    cout << sum(2, 4) << endl;
    
    //Function Overloading
    cout << "Hello World!\n";  
    // Function to add two integers
    cout << "Sum of 5 and 10: " << sum(5, 10) << endl;
    // Function to add two doubles
    cout << "Sum of 5.5 and 10.3: " << sum(5.5, 10.3) << endl;
    // Function to add three integers
    cout << "Sum of 5, 10 and 15: " << sum(5,15) << endl;
    // Function to add three doubles
    cout << "Sum of 5.5, 10.3 and 15.2: " << sum(5.5, 10.3) << endl;
    cout << fact(4) << endl;
    cout << get(4) << endl;
    // Pointers Test 
    cout << "Hello World!\n";
    float ltX = 10.5;
    cout << &ltX << endl; // Address of ltX
    float *ptr = &ltX; // Pointer to ltX
    cout << ptr << endl; // Address stored in ptr
    cout << *ptr << endl; // Value pointed to by ptr

    int y = 9;
    int *p = &y; // x is assigned the value of y using pointer dereferencing

    cout << "Value of p: " << p << endl; // Output the value of p
    cout << *p << endl; // Output the value pointed to by x
    cout << y << endl; // Output the value of y

    return 0;
}

int sum(int x , int z)
    {
        return x + z;
    }

