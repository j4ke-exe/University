// Write a program whose inputs are three integers, and whose output is the smallest of the three values.
// Ex: If the input is: 7 15 3
//     the output is: 3

#include <iostream>
using namespace std;

int main() {
   
   int num1;
   int num2;
   int num3;

   cin >> num1;
   cin >> num2;
   cin >> num3;

   int smallestNum = num1;

   if (num2 < smallestNum) {
	   smallestNum = num2;
   }

   if (num3 < smallestNum) {
	   smallestNum = num3;
   }
   
   cout << smallestNum << endl;

   return 0;
}
