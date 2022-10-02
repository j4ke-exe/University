' variables '
fname = InputBox("What's your name?")
lname = InputBox("What's your last name?")
age = InputBox("How old are you?")

' if-then statement to determine characters in name '
if (fname = fname) and (lname = lname) then
    WSH.Echo ("Your first name contains " & Len(fname) & " characters and your last name contains " & Len(lname) & " characters.")
end if

' print age '
WSH.Echo ("You are " & age & " years old.")

' if-then to determine years until 100 '
for n = age to 100
    WSH.Echo ("You will be " & n & " years old in " & n - age & " years.")
next
