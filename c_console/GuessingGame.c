#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
	srand(time(0));
	int rangeStart = 1;
	int rangeEnd = 10;
	int number = rand() % (rangeEnd - rangeStart) + rangeStart;
	printf("Pick a number between %d and %d\n", rangeStart, rangeEnd);

	int notGuessed = -1;
	int guessCount = 0;
	while (notGuessed)
	{
		char userEntered[255];
		int numberGuessed = 0;
		gets(userEntered);
		numberGuessed = atoi(userEntered);
		if (numberGuessed > 0) {
			guessCount += 1;
			if (numberGuessed == number)
			{
				printf("%d was the number. It took you %d guesses\n", numberGuessed, guessCount);
				notGuessed = 0;
			}
			else
			{
				if (numberGuessed < rangeStart || numberGuessed > rangeEnd)
				{
					printf("That number is not between %d and %d\n", rangeStart, rangeEnd);
					continue;
				}
				if (numberGuessed < number)
				{
					printf("That number is too low\n");
					continue;
				}
				if (numberGuessed > number)
				{
					printf("That number is too high\n");
					continue;
				}
			}
		}
		else {
			printf("Invalid number\n");
		}
	}
}