with open("myfile.txt",'r') as f:
    f.seek(5)
    data = f.read(5)
    print(data)
