def rot(num):
    
    num = str(num)
    #хочу баллы не хочу нули
    num = str(num).replace('6', '9', 1)
    return int(num)



