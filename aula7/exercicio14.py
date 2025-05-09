valores = {
    1: 'I',
    5: 'V',
    10: 'X',
    50: 'L',
    9: 'IX',
    4: 'IV',
    40: 'XL',
    90: 'XC',
    100: 'C',
    500: 'D',
    900: 'CM',
    1000: 'M',
    400: 'CD',
}

def numeros_romanos(numero):
    inner_list = sorted(valores, reverse=True)
    roman = ''
    for value in inner_list:
        while numero >= value:
            roman += valores.get(value)
            numero = numero - value
    return roman

assert numeros_romanos(58) == 'LVIII'
assert numeros_romanos(15) == 'XV'
assert numeros_romanos(8) == 'VIII'
assert numeros_romanos(9) == 'IX'
assert numeros_romanos(4) == 'IV'
assert numeros_romanos(14) == 'XIV'
assert numeros_romanos(40) == 'XL'
assert numeros_romanos(42) == 'XLII'
assert numeros_romanos(100) == 'C'
assert numeros_romanos(142) == 'CXLII'
assert numeros_romanos(190) == 'CXC'
assert numeros_romanos(500) == 'D'
assert numeros_romanos(890) == 'DCCCXC'
assert numeros_romanos(800) == 'DCCC'
assert numeros_romanos(900) == 'CM'
assert numeros_romanos(400) == 'CD'
