using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace cs_console
{
    class GuessingGame
    {
        static void Main(string[] args)
        {
            var random = new Random((Int32)DateTime.Now.Ticks);
            var rangeStart = 1;
            var rangeEnd = 10;
            var number = random.Next(rangeStart, rangeEnd);
            Console.WriteLine("Pick a number between {0} and {1}", rangeStart, rangeEnd);

            var notGuessed = true;
            var guessCount = 0;
            while (notGuessed)
            {
                var userEntered = Console.ReadLine();
                var numberGuessed = 0;
                if (Int32.TryParse(userEntered, out numberGuessed))
                {
                    guessCount += 1;
                    if (numberGuessed == number)
                    {
                        Console.WriteLine("{0} was the number. It took you {1} guesses", numberGuessed, guessCount);
                        notGuessed = false;
                    }
                    else
                    {
                        if (numberGuessed < rangeStart || numberGuessed > rangeEnd)
                        {
                            Console.WriteLine("That number is not between {0} and {1}", rangeStart, rangeEnd);
                            continue;
                        }
                        if (numberGuessed < number)
                        {
                            Console.WriteLine("That number is too low");
                            continue;
                        }
                        if (numberGuessed > number)
                        {
                            Console.WriteLine("That number is too high");
                            continue;
                        }
                    }
                }
                else
                {
                    Console.WriteLine("Invalid number. Try again.");
                }
            }
        }
    }
}
