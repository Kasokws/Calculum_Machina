# É uma calculadora simples, feita com o intuito de...
# CALCULAR!

# primeiro solicitamos a entrada do user, que pode ser complex, str, float, e até uma string.
# afinal, o input recebe tudo, até Boolean, mas o user deve ter esse tipo de controle...

def line():
    print('-'*60)

def wlcm():
    line()
    print("Olá, essa é a calculadora mais inteligente das quatro operações básicas :)")
    line()

def calculadora():
    line()
    operation = input('''
Por favor digite a operação matemática que deseja executar:
+ for addition
- for substraction
* for multiplication
/ for division
''')
    line()

    line()
    number_1 = int(input('Digite o primeiro numero aqui:\n'))
    number_2 = int(input('Digite o segundo numero aqui:\n'))
    line()

    line()
    print("Primeiro Numero: ", number_1)
    print("Segundo Numero: ", number_2)
    line()

    if operation == '+':
        #Addition
        line()
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)
        line()

    elif operation == '-':
        #Substraction
        line()
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)
        line()

    elif operation == '*':
        #Multiplication
        line()
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)
        line()

    elif operation == '/':
        #Division
        line()
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)
        line()

    else:
        line()
        print("Você não digitou um operador válido, por favor execute o programa novamente...")
        line()

def again():

    # Recebe o input do user
    line()
    cal_dnv = input('''
Quer realizar algum cálculo novamente?
Por favor, digite S para SIM ou N para NAO.
''')
    line()

    # Se a resposta for S, calculadora() roda novamente :)
    if cal_dnv.upper() == 'S':
        calculadora()

    # Se a resposta for N, o programa dá tchau :D    
    elif cal_dnv.upper() == 'N':
        print("Te vejo mais tarde!")

    # Se não for nenhuma das duas... o que posso dizer? :/
    else:
        again()

# Primeiro as introduções...
wlcm()

# Aqui devemos chamar a função "calculadora"...
calculadora()

# Isso aqui pro caso do usuario ter vontade de executar mais operações em seguida:
again()