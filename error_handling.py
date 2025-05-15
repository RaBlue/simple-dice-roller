#validation for numerical inputs
def numValidation(num):
    try:
         int(num)
         verdict = True
    except ValueError:
        verdict = False
    return verdict

#validation for weighted dice imput
def weightValidation(weight):
    try:
        if weight == 'a' or weight == 'd' or weight == 'none':
            verdict = True
        else:
            verdict = False
    except ValueError:
        verdict = False
    return verdict