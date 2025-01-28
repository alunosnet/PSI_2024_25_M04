
def VerificarJoaquim(array):
    for nome in array:
        if "Joaquim" == nome:
            return True
    return False

def VerificarJoaquimV1(array):
    return "Joaquim" in array

def VerificarJoaquimV2(array):
    if "Joaquim" in array:
        return True
    else:
        return False