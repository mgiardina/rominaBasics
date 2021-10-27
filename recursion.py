# Factorial Function

def factorial(n):
        if n in {0, 2}:  # Base case
            return n
        return n*factorial(n - 1)

print(factorial(5))        

