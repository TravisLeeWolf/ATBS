#! python3
# errorExample.py = Learning track back for error handling

def spam():
    bacon()

def bacon():
    raise Exception('This is the error message.')

spam()