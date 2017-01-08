program GuessingGame;

uses
  SysUtils;

var
  notGuessed: boolean;
  rangeStart, rangeEnd, number, guessCount, numberGuessed: integer;

begin
  Randomize;
  rangeStart := 1;
  rangeEnd := 10;
  number := random(rangeEnd - rangeStart + 1) + rangeStart;
  guessCount := 0;
  notGuessed := True;
  WriteLn(format('Pick a number between %0:d and %1:d.', [rangeStart, rangeEnd]));
  while notGuessed do
  begin
    try
      readln(numberGuessed);
      guessCount += 1;
    except
      writeln('Invalid number.');
    end;
    if numberGuessed = number then
    begin
      WriteLn(format('%0:d was the number. It took you %1:d guesses.',
        [numberGuessed, guessCount]));
      notGuessed := False;
    end
    else
    begin
      if (numberGuessed < rangeStart) or (numberGuessed > rangeEnd) then
      begin
        WriteLn(format('That number is not between %0:d and %1:d.',
          [rangeStart, rangeEnd]));
        continue;
      end;
      if numberGuessed < number then
      begin
        WriteLn('That number is too low.');
        continue;
      end;
      if numberGuessed > number then
      begin
        WriteLn('That number is too high.');
        continue;
      end;
    end;
  end;
end.
