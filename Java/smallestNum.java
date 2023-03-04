import java.util.Scanner;

public class LabProgram {
   public static void main(String[] args) {
      Scanner scnr = new Scanner(System.in);
      int num1, num2, num3, smallestNum;
      
      num1 = scnr.nextInt();
      num2 = scnr.nextInt();
      num3 = scnr.nextInt();
      
      smallestNum = num1;
      
      if (num2 < smallestNum) {
         smallestNum = num2;
      }
      
      if (num3 < smallestNum) {
         smallestNum = num3;
      }
      
      System.out.println(smallestNum);
   }
}
