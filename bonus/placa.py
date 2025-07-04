def validar_placa_br(placa):
    if len(placa) == 7:   
        if placa[0:3].isalpha() and placa[3:].isnumeric():
            return True
    return False

def validar_placa_mercosul(placa):
    if len(placa) == 7:   
        if placa[0:3].isalpha() and placa[3].isnumeric() and placa[4].isalpha() and placa[5:].isnumeric():
            return True
    return False

def validar_placa(placa):
    if validar_placa_br(placa) or validar_placa_mercosul(placa):
        return True
    return False

assert validar_placa_br('ABC1234') == True
assert validar_placa_br('ABCD234') == False
assert validar_placa_br('XYZ3435') == True

assert validar_placa_mercosul('ABC1D34') == True
assert validar_placa_mercosul('ABC1234') == False

assert validar_placa('ABC1234') == True
assert validar_placa('ABCD234') == False
assert validar_placa('ABC1D34') == True
