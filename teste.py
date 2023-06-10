import re

padrao_mercosul = r'^[A-Z]{3}\d[A-Z]\d{2}$'
padrao_antigo = r'^[A-Z]{3}\d{4}$'


placa = '   aci6j67    '
placa = placa.strip().upper()
print(placa)


if len(placa) != 7:
    print("Placa inválida: Verifique a quantidade a sua quantidade de digitos")
else:
    quinto_digito = placa[4]
    print(quinto_digito)
    if re.match(padrao_mercosul, placa):
        print("Placa no padrão Mercosul")
    elif re.match(padrao_antigo, placa):
        print("Placa no padrão antigo")
    else:
        print("Placa inválida: Padrão desconhecido")



