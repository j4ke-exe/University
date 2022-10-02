Option Explicit

Const cGreetingsMsg = "Pick a number between 1 - 100"

Dim intUserNumber, intRandomNo, strOkToEnd, intNoGuesses

intNoGuesses = 0

' Generate a random number between 1 and 100
Randomize 
intRandomNo = FormatNumber(Int((100 * Rnd) + 1))

Do Until strOkToEnd = "yes"
    intUserNumber = InputBox("Type your guess:", cGreetingsMsg)
    intNoGuesses = intNoGuesses + 1
    If Len(intUserNumber) <> 0 Then
        If IsNumeric(intUserNumber) = True Then
            If FormatNumber(intUserNumber) = intRandomNo Then
                MsgBox "Congratulations! You guesset it. The number was " & _
                intUserNumber & "." & vbCrLf & vbCrLf & "You guessed it " & _
                "in " & intNoGuesses & " tries.", ,cGreetingsMsg
                strOkToEnd = "yes"
    End If
    If FormatNumber(intUserNumber) < intRandomNo Then
        MsgBox "Your guess is too low. Try again.", ,cGreetingsMsg
        strOkToEnd = "no"
    Else If FormatNumber(intUserNumber) > intRandomNo Then
        MsgBox "Your guess was too high. Try again.", ,cGreetingsMsg
        strOkToEnd = "no"
    End If
    End If
    Else
        MsgBox "Invalid input. Please type a number.", ,cGreetingsMsg
    End If
    Else
        MsgBox "You either failed to type a value or you clicked on 'Cancel'. " & vbCrLf & _
        "" & vbCrLf & "Play again soon!", ,cGreetingsMsg
        strOkToEnd = "yes"
    End If
Loop
