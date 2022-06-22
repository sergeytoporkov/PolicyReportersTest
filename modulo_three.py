# MODULO THREE

def modThree(string):
    string = int(string)
    value, i = 0, 0
    while(string != 0):
        temp = string % 10
        value += temp * pow(2,i)
        string = string // 10
        i += 1
    return value % 3