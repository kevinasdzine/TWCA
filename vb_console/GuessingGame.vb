Module GuessingGame

    Sub Main()
        Dim random As New Random(CType(DateAndTime.Now.Ticks Or &HFFFF0000, Int32))
        Dim rangeStart = 1
        Dim rangeEnd = 10
        Dim number = random.Next(rangeStart, rangeEnd)
        Console.WriteLine("Pick a number between {0} and {1}", rangeStart, rangeEnd)
        Dim notGuessed = True
        Dim guessCount = 0
        Do While notGuessed
            Dim userEntered = Console.ReadLine()
            Dim numberGuessed = 0
            If Int32.TryParse(userEntered, numberGuessed) Then
                guessCount += 1
                If numberGuessed = number Then
                    Console.WriteLine("{0} was the number. It took you {1} guesses", numberGuessed, guessCount)
                    notGuessed = False
                Else
                    If numberGuessed < rangeStart Or numberGuessed > rangeEnd Then
                        Console.WriteLine("That number is not between {0} and {1}", rangeStart, rangeEnd)
                        Continue Do
                    End If
                    If (numberGuessed < number) Then
                        Console.WriteLine("That number is too low")
                        Continue Do
                    End If
                    If (numberGuessed > number) Then

                        Console.WriteLine("That number is too high")
                        Continue Do
                    End If
                End If
            Else
                Console.WriteLine("Invalid number. Try again.")
            End If
        Loop
    End Sub

End Module
