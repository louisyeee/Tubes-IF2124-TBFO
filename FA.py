def checkCharacter(x):
    if ((x>='a' and x<='z') or (x>='A' and x <= 'Z')):
        return True
    else:
        return False

def checkNumber(x):
    if(x>= 0 and x<= 9):
        return True
    else:
        return False

def checkVariable(Var):
    if(not checkCharacter(Var[0])):
        return False 
    for i in range(len(Var) - 1):
        if not(checkCharacter(Var[i]) or checkNumber(Var[i]) or Var[i] == '_'):
            return False
        else:
            return True

#untuk testing
# Var = input()
# print(checkVariable(Var))