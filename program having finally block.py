''' program having  finally block to re-raise a exception 
that will a outer try-except block'''
try :
    print ("dividing dividing 2 strings.....")
    try:
        quo="abc"/"abc"
        print(quo)
    finally:
        print("this is the finally block.......which executes every time")    
except TypeError:
    print("here the type error is handled,which is raised in the inner try")        
    

