f=open('file_handling.txt','w+')
str='This is a demo file to perform different file handling operations.'
f.write(str)
f=open('file_handling.txt','a')
str1='\nThis is append function'
f.write(str1)
f.close()

f=open('file_handling.txt','r+')
f.write("writing in r+ mode")
f.writelines("\nwriting\nusing\nwritelines\n")
r=f.read()
print(r)
f.close()