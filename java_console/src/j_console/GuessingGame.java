/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package j_console;

import java.util.Random;
import java.util.Scanner;

/**
 *
 * @author Kevin
 */
public class GuessingGame {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        Random random = new Random();
        Integer rangeStart = 1;
        Integer rangeEnd = 10;
        Integer number = random.nextInt(rangeEnd - rangeStart) + rangeStart;
        System.out.printf("Pick a number between %d and %d.\n", rangeStart, rangeEnd);

        Boolean notGuessed = true;
        Integer guessCount = 0;
        while (notGuessed) {
            String userEntered = input.nextLine();
            Integer numberGuessed = 0;
            
            try {
                numberGuessed = Integer.parseInt(userEntered);
            } catch (NumberFormatException e) {
                System.out.println("Invalid number. Try again.\n");
            }

            guessCount += 1;
            if (numberGuessed == number) {
                System.out.printf("%d was the number. It took you %d guesses.\n", numberGuessed, guessCount);
                notGuessed = false;
            } else {
                if (numberGuessed < rangeStart || numberGuessed > rangeEnd) {
                    System.out.printf("That number is not between %d and %d.\n", rangeStart, rangeEnd);
                    continue;
                }
                if (numberGuessed < number) {
                    System.out.printf("That number is too low.\n");
                    continue;
                }
                if (numberGuessed > number) {
                    System.out.printf("That number is too high.\n");
                    continue;
                }
            }

        }
    }

}
