#multiple exceptions with single try
try:
    num=int(input("enter number"))
    print(num**3)
except (KeyboardInterrupt,ValueError,TypeError):
        print("check while entering  the data......")
print("program terminated")

