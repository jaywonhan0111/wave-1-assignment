#include <iostream>
using namespace std;
int main()
{

int cents;

cout << "Enter number of cents:"; 

cin >> cents;

int toonies, loonies, quarters, dimes, nickles, pennies;

toonies=cents/200;
cents=cents%200;
loonies=cents/100;
cents=cents%100;
quarters=cents/25;
cents=cents%25;
dimes=cents/10;
cents=cents%10;
nickles=cents/5;
cents=cents%5;
pennies=cents;
