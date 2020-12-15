import os

# f = open("test.txt",'a')
# f.write("\nHello ThienHi 7")
# f.close()

# f = open("test.txt",'r')
# print (f.read())

# f1 = open("test1.txt",'w')
# f1.write("I have a pen, i have an apple")
# f1.close()

# f1 = open("test1.txt",'r')
# print (f1.read())

if os.path.exists("test1.txt"):
    print("I had found Test1.txt and I will delete it")
    os.remove("test1.txt")
else: print("Not found")