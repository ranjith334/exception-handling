try:
    file=open('file1.txt')
    str=f.readline()
    print(str)
except IOError:
    print("error occured due to input")    
except ValueError:
    print("could not covert to integer")
except:
    print("unexpectd error")    