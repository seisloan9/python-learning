def greatestInt(integer1, integer2, integer3):
    if integer1 > integer2 and integer1 > integer3:
        return integer1
    elif integer2 > integer3:
        return integer2
    else:
        return integer3
