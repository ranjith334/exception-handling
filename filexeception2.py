try:
    file=open('file1.txt')
    str=file.readline()
    print(str)
except IOError:
    print("error occured due to input")    
else:
    print("program executed sucessfully!!!")    



