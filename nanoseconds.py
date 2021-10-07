import time

def CurrentNanoSeconds():
    return round(time.time() * 10000000000)
