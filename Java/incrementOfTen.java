/*
LAB: Output range with increment of 10

Write a program whose input is two integers, and whose output is the first integer and subsequent 
increments of 10 as long as the value is less than or equal to the second integer.

Ex: If the input is:
-15 30

the output is:
-15 -5 5 15 25

Ex: If the second integer is less than the first as in:
20 5

the output is:
Second integer can't be less than the first.

For coding simplicity, output a space after every integer, including the last.
*/

// Solution
import java.util.Scanner;

public class LabProgram {
   public static void main(String[] args) {
      Scanner scnr = new Scanner(System.in);
      
      int one = scnr.nextInt();
      int two = scnr.nextInt();
      
      if (two < one) {
         System.out.println("Second integer can't be less than the first.");
      } else {
         int selected = one;
         while (selected <= two) {
            System.out.print(selected + " ");
            selected += 10;
         }
      }
   }
}

/*
Input: -15 30
Output: -15 -5 5 15 25 

Input: 20 5
Output: Second integer can't be less than the first.
*/
