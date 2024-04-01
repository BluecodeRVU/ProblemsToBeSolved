def listtostr(lst):
    result = ''
    for key, value in lst:
        result += f'{key}={value};'
    return result

print(listtostr([('a','b'),('c','d'),('e','f'),('g','h')]).strip(';'))
