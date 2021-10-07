import random

def GenerateRandomArray(n):
    array = [random.randint(-500,500) for i in range(n)]
    return array