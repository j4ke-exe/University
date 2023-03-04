import java.util.Scanner;

public class FindAlpha {
   public static void main (String [] args) {
      Scanner scnr = new Scanner(System.in);
      String passCode;

      passCode = scnr.next();
      
      // Iterate through passCode to find a character that contains a letter
      for (int i = 0; i < passCode.length(); i++) {
         if (Character.isLetter(passCode.charAt(i))) {
            System.out.println("Alphabetic at " + i);
         }
      }
   }
}
