

def serializeToken(token):
    if not token: return ''
    return ' : '.join(token)

def raiseException(message):
    print(message)
    raise Exception(message)





