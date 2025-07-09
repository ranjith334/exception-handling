#excepton Handling 
# zero division error 
num=int(input("enter numerator :"))
deno=int(input("enter denominator"))
try:
    quo=num/deno
    print("quotient",quo)
except ZeroDivisionError:
    print("denominator cant be a zero...")    
    


