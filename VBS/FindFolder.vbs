Dim Arg, fn 'Set dimensions for variables

Set Arg = WScript.Arguments 'Get the arguments passed to the script

fn = Arg(0) 'Parameter for searching for a filepath

Set fso = CreateObject("Scripting.FileSystemObject") 'Create a new FileSystemObject for fso

If fso.FolderExists(fn) Then 'If the folder exists, then
    msgbox "Found: " & fn 'Display the folder path
Else
    msgbox "Could not find: " & fn & ". Please check the path and try again." 'Display an error message
End If

Set folder = fso.GetFolder(fn) 'Get the folder object
    WScript.Echo "Below is a list of files in the folder: " & fn & "along with their names, size, and date created." 'Display a message containing the folder path and a list of files

Set files = folder.Files

For Each file in files 'For each file in the folder, display the file name, size, and date created
    WScript.Echo "Name: " & (file.name)
    WScript.Echo "Size: " & (file.size)
    WScript.Echo "Date: " & (file.datecreated)
Next
