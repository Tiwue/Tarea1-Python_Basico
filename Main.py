print("Hola Mundo")

def fibonacci(n,a=0,b=1):
    while n!=0:
        return fibonacci(n-1,b,a+b)
    return a

print(fibonacci(900))