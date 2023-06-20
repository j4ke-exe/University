// Replace any alphabetic character with '_' in 2-character string passCode. Ex: If passCode is "9a", output is: 9_
// Hint: Use two if statements to check each of the two characters in the string, using isalpha().

#include <iostream>
#include <string>
#include <cctype>
using namespace std;

int main() {
   string passCode;

   cin >> passCode;

   if (isalpha(passCode[0])) {
        passCode[0] = '_';
   }

   if (isalpha(passCode[1])) {
        passCode[1] = '_';
   }

   cout << passCode << endl;
   return 0;
}
