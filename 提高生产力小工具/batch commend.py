import os

fr = open("ip.txt","r")


li = fr.readlines()

pythonver = "c:\\Python27\\python.exe "
tool = "POC-zookeeper.py "

#print(comm)
#a = os.system(comm)
#a = os.system(r'pwd')
#print(a)
print(li)
for i in li:
    print(i)
    i = i.replace('\n','')
    comm = pythonver + tool + i + "2181 " + "envi "
    #print(comm)
    res = os.system(comm)
