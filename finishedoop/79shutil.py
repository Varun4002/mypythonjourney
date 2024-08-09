#copyfile() = copy content of file
#copy() = copyfile() +permission + destication can be directory
#copy2() = copy() + copies metadata

import shutil

shutil.copy("C:\\Users\\varun\\Desktop\\python\\test.txt","testcopy.txt")
shutil.copy2("C:\\Users\\varun\\Desktop\\python\\test.txt","testcopy.txt")
shutil.copyfile("C:\\Users\\varun\\Desktop\\python\\test.txt","testcopy.txt")