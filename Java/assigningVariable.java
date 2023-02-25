public class Mice {
   public static void main(String[] args) {
      int litterSize;
      int yearlyLitters;
      int annualMice;
   
      litterSize    = 3; // Low end of litter size range
      yearlyLitters = 5; // Low end of litters per year

      System.out.print("One female mouse may give birth to ");
      annualMice = litterSize * yearlyLitters;
      System.out.println(annualMice + " mice,");

      litterSize    = 14; // High end
      yearlyLitters = 10; // High end

      System.out.print("and up to ");
      annualMice = litterSize * yearlyLitters;
      System.out.println(annualMice + " mice, in a year.");
   }
}

// Output: One female mouse may give birth to 15 mice, and up to 140 mice, in a year.
