/*
Question: Given numRows and numColumns, print a list of all seats in a theater. 
          Rows are numbered, columns lettered, as in 1A or 3E. Print a space after each seat, including after the last. 
          Use separate print statements to print the row and column. Ex: numRows = 2 and numColumns = 3 prints:
          1A 1B 1C 2A 2B 2C
*/

// Solution
import java.util.Scanner;
public class NestedLoops {
   public static void main (String [] args) {
      Scanner scnr = new Scanner(System.in);
      int numRows;
      int numColumns;
      int currentRow;
      int currentColumn;
      char currentColumnLetter;

      numRows = scnr.nextInt();
      numColumns = scnr.nextInt();

      for (currentRow = 1; currentRow <= numRows; currentRow++) {
         for (currentColumn = 1; currentColumn <= numColumns; currentColumn++) {
            currentColumnLetter = (char)('A' + currentColumn - 1);
            System.out.print(currentRow + "" + currentColumnLetter + " ");
         }
      }
      System.out.println("");
   }
}

/*
Input: Testing with 5 rows and 3 columns
Output: 1A 1B 1C 2A 2B 2C 3A 3B 3C 4A 4B 4C 5A 5B 5C
*/
