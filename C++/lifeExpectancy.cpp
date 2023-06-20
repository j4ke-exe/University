#include <iostream>
using namespace std;

int main() {
   double lifeExpectancy;
   double userBmi;
   char userChoice;
   bool isOverweight;
   bool isMale;
   
   // Get user's sex
   cout << "Female (f) or male (m): ";
   cin >> userChoice;
   if (userChoice == 'm') {
      isMale = true;
   }
   else {
      isMale = false;
   }
   
   // Get user's BMI
   cout << "Enter body mass index (BMI): ";
   cin  >> userBmi;
   isOverweight = (userBmi >= 25);
   
   // Determine life expectancy based on sex and BMI
   if (isMale && !isOverweight ) {
      lifeExpectancy = 79.4;
   }
   else if (!isMale && !isOverweight ) {
      lifeExpectancy = 83.5;
   }
   else if (isMale && isOverweight) {
      lifeExpectancy = 77.3;
   }
   else {
      lifeExpectancy = 81.4;
   }
   
   cout << "Life expectancy is " << lifeExpectancy
        << " years." << endl;
   
   return 0;
}
