' This is a simple script to take the sum and average of three numbers. '
' To begin, simply imput the following into your console:               '
' cscript .\SumOfThree.vbs 2 3 5 > results.txt                          '
' --------------------------------------------------------------------- '
' Example results:                                                      '
' The Total = 10                                                        '
' The Average = 3.33333333333333                                        '
' --------------------------------------------------------------------- '

' fnum, snum, and tnum will query their respective variable and process '
fnum = cint(WScript.arguments(0))
snum = cint(WScript.arguments(1))
tnum = cint(WScript.arguments(2))

' sum of the three numbers '
total = fnum + snum + tnum

' average of the three numbers '
average = (fnum + snum + tnum)/3

' print results to console '
WSH.Echo ("The Total = " & total)
WSH.Echo ("The Average = " & average)

' if-then statement to print numbers in ascending order '
if (fnum > tnum) then
    WSH.Echo ("Oops... your first number is " & fnum & ". Numbers must be in ascending order for this to work. Please try again.")
elseif (snum > tnum) then
    WSH.Echo ("Oops... your second number is " & snum & ". Numbers must be in ascending order for this to work. Please try again.")
elseif (tnum > fnum) and (tnum > snum) then
    for I = fnum to tnum
        WSH.Echo ("I = " & I)
    next
else
    WSH.Echo ("All numbers are equal.")
end if
