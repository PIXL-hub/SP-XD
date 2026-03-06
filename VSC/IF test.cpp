#include<iostream>
using namespace std;


int main()
{

    string Name;
    int Episode;
    cout<<"Enter The Name Of The Anime"<<endl;
    cin >> Name;

    if(Name == "Kamonohashi_Ron")
    {
        Episode = 13;
    
    }

    else if(Name == "Ore_Dake_level")
    {
        Episode = 12;
        
    }

    else if(Name == "Jujustu_Kaisen")
    {
        Episode = 23;
        
    }

    else if(Name == "Bungou_Stray_Dogs")
    {
        Episode = 12;
        
    }

    else if(Name == "DeathNote")
    {
        Episode = 37;
        
    }

    else
    {
        cout<<"Anime Doesn't Found";
        
    }

if(Episode >= 12)
{

    cout<<"True";
}

else
{
    cout<<"False";
}
    return 0;

}
