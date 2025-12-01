#!/bin/python3

#file=open("samplefile.txt","a")
#file.write("hello world\ntoday is monday")
#file.close
file=open("samplefile.txt","w")
file.write("write1\n")
file.write("write2\n")
file.write("write3\n")
file=open("samplefile.txt","r")
print(file.read(),end="")
#print(file.read())
#list_number=1
#for l in file:
#	print(list_number,l,end="")
#	list_number+=1
file.close

