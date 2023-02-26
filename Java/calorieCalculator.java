import java.util.Scanner;

public class LabProgram {
   public static void main(String[] args) {
      Scanner scnr = new Scanner(System.in);
      double years;
      double pounds;
      double bpm;
      double minutes;
      double women;
      double men;
      
      years = scnr.nextDouble();
      pounds = scnr.nextDouble();
      bpm = scnr.nextDouble();
      minutes = scnr.nextDouble();
      
      women = ((years * 0.074) - (pounds * 0.05741) + (bpm * 0.4472) - 20.4022 ) * minutes / 4.184;
      men = ((years * 0.2017) + (pounds * 0.09036) + (bpm * 0.6309) - 55.0969 ) * minutes / 4.184;
      
      System.out.printf("Women: %.2f calories\n", women);
      System.out.printf("Men: %.2f calories\n", men);
   }
}

/* 
   Input: 49 155 148 60
   Output: Women: 580.94 calories
           Men: 891.47 calories
*/
