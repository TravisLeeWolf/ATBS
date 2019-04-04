def spam():
    eggs = 'spam local'
    print(eggs) # Prints 'spam local'

def bacon():
    eggs = 'bacon local'
    print(eggs) # Prints 'bacon local'
    spam()

eggs = 'global'
bacon()
print(eggs) # Prints 'global'