# -*- coding: utf-8 -*-
'''
'r' open for reading (default) 
'w' open for writing, truncating the file first 
'x' open for exclusive creation, failing if the file already exists 
'a' open for writing, appending to the end of the file if it exists 
'b' binary mode 
't' text mode (default) 
'+' open a disk file for updating (reading and writing) 
'U' universal newlines mode (deprecated) 
'''

f = open('phonebook.txt','w')
f.write('1;1;1;1\n')
f.write('2;2;2;2\n')
f.write('3;3;3;3\n')
f.write('4;4;4;4\n')
f.close()

print('-'*20)
f2 = open('phonebook.txt')
text = f2.readlines()
print(text[0]) # line 1 from file
f2.close()

print('-'*20)
f3 = open('phonebook.txt')
for line in f3.readlines():
   print(line) # print all lines from file
f3.close()

print('-'*20)
f4 = open('phonebook.txt','a')
f4.write('5;5;5;5\n') # add line from end of file
f4.close()
f4 = open('phonebook.txt')
for line in f4.readlines():
   print(line)
f4.close()
