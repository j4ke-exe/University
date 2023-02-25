import java.util.Scanner;

// Estimates distance of lightning based on seconds
// between lightning and thunder

public class LightningDist {
   public static void main(String[] args) {
      Scanner scnr = new Scanner(System.in);
      final double SPEED_OF_SOUND   = 761.207; // Miles/hour (sea level)
      final double SECONDS_PER_HOUR = 3600.0;  // Secs/hour
      double secondsBetween;
      double timeInHours;
      double distInMiles;

      System.out.println("Enter seconds between");
      System.out.print("lightning strike and thunder: ");
      secondsBetween = scnr.nextDouble();

      timeInHours = secondsBetween / SECONDS_PER_HOUR;
      distInMiles = SPEED_OF_SOUND * timeInHours;

      System.out.println("Lightning strike was approximately");
      System.out.println(distInMiles + " miles away.");
   }
}

// Output: Enter seconds between
// lightning strike and thunder: 7
// Lightning strike was approximately
// 1.4801247222222222 miles away.

// ...

// Enter seconds between
// lightning strike and thunder: 1
// Lightning strike was approximately
// 0.2114463888888889 miles away.
