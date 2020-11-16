n = 0

def get_unique_name():
    global n
    n = n+1
    return '__n'+str(n)+'__'