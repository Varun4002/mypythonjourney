# f = open('myfile.txt','r')
# text=f.read()
# f.close()
# print(text)


f = open('myfile2.txt','w')
f.write("hello people")


with open('myfile.txt',"a") as f:
    f.write("hey im inside the file")