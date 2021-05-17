def addition(a, b):  #function to return addition of two values
    return a+b

def subtraction(a,b):  #function to return Subtraction of two values
    return a-b

def multiplication(a,b):  #function to return multiplication of two values
    return a*b

def division(a,b):   #function to return Divison of two values
    if b==0:
        raise ValueError('Divide by zero')  #If denominator happes to be zero then raise the exception 
    return a/b

