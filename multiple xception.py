#multiple exceptions with single try
try:
    num=int(input("enter number"))
    print(num**3)
except KeyboardInterrupt:
    print("interputed the compiler")
except ValueError:
    print("Enter  number only")    
print("program terminated")
print("bye")

