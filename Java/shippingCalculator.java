import java.util.Scanner;

public class ShippingCalculator {
   public static void main(String[] args) {
      Scanner scnr = new Scanner(System.in);
      final int FLAT_FEE_CENTS = 75;
      int shipWeightPounds;
      int shipCostCents = 0;

      final int CENTS_PER_POUND = 25;
      shipWeightPounds = scnr.nextInt();
      shipCostCents = FLAT_FEE_CENTS + (CENTS_PER_POUND * shipWeightPounds);

      System.out.println("Weight(lb): " + shipWeightPounds);
      System.out.println("Flat fee(cents): " + FLAT_FEE_CENTS);
      System.out.println("Cents per pound: " + CENTS_PER_POUND);
      System.out.println("Shipping cost(cents): " + shipCostCents);
   }
}

// Testing shipWeightPounds = 10
// Output: Weight(lb): 10
//         Flat fee(cents): 75
//         Cents per pound: 25
//         Shipping cost(cents): 325
