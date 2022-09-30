#1. Create a file and call it lyrics.txt (it does not need to have any content)
#2. Create a new file and call it songs.docx and in this file write 3 lines of text to it.

#3. open and read the content and write it to your terminal window. 
# * you should use both the read(), readline(), and readlines() methods for this. 
# (so 3 times the same output).


file = open('files/songs.docx')

# Udskriver en linje
print(file.read())

file = open('files/songs.docx')

# Udskriver hver linje 
print(file.readline())

file = open('files/songs.docx')

# Udskriver en liste af linjer
print(file.readlines())

