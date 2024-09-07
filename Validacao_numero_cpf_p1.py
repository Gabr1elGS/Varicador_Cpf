#Validação do CPF.
import os

while True:
    
    CPF_user= input("Digite seu CPF: ").replace('.', '')\
        .replace('-', '')

    digitos_9 = CPF_user[:9]
    digitos_10 = CPF_user[:10]
    count_1= 10
    count_2= 11

    result_1= 0
    result_2= 0
    for digito_1 in digitos_9:
        result_1 += int(digito_1) * count_1
        count_1 -=1
    digito_1 =(result_1*10)%11
    digito_1 = digito_1 if digito_1<=9 else 0


    for digito_2 in digitos_10:
        result_2 += int(digito_2) *count_2
        count_2 -=1
    digito_2 =(result_2*10)%11
    digito_2 = digito_2 if digito_2 <=9 else 0

    CPF_Calculado = (f"{digitos_9}{digito_1}{digito_2}")

    if CPF_user == CPF_Calculado:
        print (f"O CPF: {CPF_user}, enviado é valido")
    else:
        print ("CPF Invalido!")
    cont = input("Desaja continuar? : ").upper
    os.system("cls")
    if cont == "SIM":
        continue
    print("Exit...")
    break
       