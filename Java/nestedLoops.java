import java.util.Scanner;
public class NestedLoop {
   public static void main (String [] args) {
      Scanner scnr = new Scanner(System.in);
      int userNum;
      int i;
      int j;

      userNum = scnr.nextInt();

      for (i = 0; i <= userNum; i++) {
         for (j = 0; j < i; j++) {
            System.out.print(" ");
         }
         System.out.println(i);
      }
   }
}

/* 

Testing with userNum = 20

Output:
0
 1
  2
   3
    4
     5
      6
       7
        8
         9
          10
           11
            12
             13
              14
               15
                16
                 17
                  18
                   19
                    20
                    
*/
