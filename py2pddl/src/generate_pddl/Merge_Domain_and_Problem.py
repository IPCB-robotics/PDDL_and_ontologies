#!/usr/bin/python

data = data2 = ""
 
# Reading data from file1
with open('domain.py') as fp:
    data = fp.read()
  
# Reading data from file2
with open('problem.py') as fp:
    data2 = fp.read()
  
data += "\n"
data += data2
  
with open ('Domain_and_Problem.py', 'w') as fp:
    fp.write(data)