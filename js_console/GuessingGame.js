const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function random(min, max) {
    return Math.trunc(Math.random() * (max - min) + min);
}

rangeStart = 1;
rangeEnd = 10;
number = random(rangeStart, rangeEnd);

console.log(`Pick a number between ${rangeStart} and ${rangeEnd}`);

notGuessed = true;
guessCount = 0;
numberGuessed = 0;
rl.on('line', function (userEntered) {
    try {
        numberGuessed = parseInt(userEntered)
        guessCount += 1;
    } catch (err) {
        console.log("Invalid number. Try again.");
        return;
    }
    if (numberGuessed == number) {
        console.log(numberGuessed + ` was the number. It took you ${guessCount} guesses`);
        process.exit(0);
    }
    else {
        if (numberGuessed < rangeStart || numberGuessed > rangeEnd) {
            console.log(`That number is not between ${rangeStart} and ${rangeEnd}`);
            return;
        }
        if (numberGuessed < number) {
            console.log("That number is too low");
            return;
        }
        if (numberGuessed > number) {
            console.log("That number is too high");
            return;
        }
    }
});

