#include <iostream>
using namespace std;

int main() {
   bool isRed;
   bool isBalloon;

   cin >> isRed;
   cin >> isBalloon;

   if ((isBalloon == true) && (isRed == false)) {
      cout << "Balloon";
   }
   else if ((isBalloon == true) && (isRed == true)) {
      cout << "Red balloon";
   }
   else
      cout << "Not a balloon";
   cout << endl;

   return 0;
}
