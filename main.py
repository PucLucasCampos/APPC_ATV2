import os

funcionarios = {}

def Limpar():
    os.system("cls")

def Validar_codigo_funcao():
    cod_funcao = int(input("Código da função: "))
    while cod_funcao != 101 and cod_funcao != 102:
        print("Código da função invalido >>> Tente novamente!!! ")
        cod_funcao = int(input("Código da função: "))
    return cod_funcao

def Validar_id_matricula():
    id_matricula = int(input("Digite o ID da matrícula:"))
    while id_matricula in funcionarios:
        print("ID de matricula ja existe >>> Tente novamente!!! ")
        id_matricula = int(input("Digite o ID da matrícula:"))
    return id_matricula

def Calculo_imposto(salario_bruto):
    if salario_bruto <= 2259.20:
        imposto = 0
    elif salario_bruto <= 2828.65:
        imposto = 0.075
    elif salario_bruto <= 3751.05:
        imposto = 0.15
    elif salario_bruto <= 4664.68:
        imposto = 0.225    
    else:
        imposto = 0.275
    return imposto


def Cadastro_funcionario():
    id_matricula = Validar_id_matricula()
    nome = str(input("Nome do funcionario: "))
    print("[101] - Vendedor\n[102] - Administrativo")
    cod_funcao = Validar_codigo_funcao()
    numero_faltas = int(input("Número de faltas por mês: "))
    if cod_funcao == 101:
        salario_fixo = 1500
        falta = (salario_fixo / 30) * numero_faltas
        volume_vendas = int(input("Volume de vendas: "))
        salario_bruto = (volume_vendas * 0.9) + 1500 - falta
        imposto = Calculo_imposto(salario_bruto)
        print(imposto)
        salario_liquido = salario_bruto - (salario_bruto * imposto)

        print(salario_bruto)
    else:
        print("Salário varia entre R$2150,00 até R$6950,00")
        salario_fixo = float(input("Salário do funcionário: "))
        while salario_fixo < 2150 or salario_fixo > 6950:
            print("Por favor, digite um salário dentro da faixa especificada.")
            salario_fixo = float(input("Salário do funcionário: "))
        falta = (salario_fixo / 30) * numero_faltas
        salario_bruto = salario_fixo - falta
        imposto = Calculo_imposto(salario_bruto)
        salario_liquido = salario_bruto - (salario_bruto * imposto)
    
    funcionarios[id_matricula] = [nome, cod_funcao, numero_faltas, salario_liquido, salario_bruto, imposto]

def Remover_funcionario():
    print(">>> Remoção de Funcionario >>>")
    remover = int(input("ID Matriucla do funcionário: "))
    while remover not in funcionarios:
        print("ID de matricula não existe >>> Tente novamente!!!")
        remover = int(input("ID Matriucla do funcionário: "))
    del funcionarios[(remover)]

def Folha_pagamento():
    print("Determinar folha de pagamento por ID de determinado funcionário")
    key = int(input("ID do(a) funcionário: "))
    for id, index in funcionarios.items(): 
        if key == id:
            print(f"""
            ID: {id}
            NOME: {index[0]}
            CODIGO: {index[1]}
            SALÁRIO BRUTO: R${index[3]}
            PORCENTUAL DE IMPOSTO: {index[5]}
            """)
        else:
            print(">>> ID não existe")

def Relatorio():
    print("Relatório com salario bruto e liquido de todos os funcionarios")
    for id, index in funcionarios.items():
            print(f"""
            ID: {id}
            NOME: {index[0]}
            CODIGO: {index[1]}
            SALÁRIO BRUTO: R${index[4]}
            SALÁRIO LIQUIDO: R$ {index[3]}
            """)

def Maior_salario_liquido():
    maior = auxM = 0
    for sl in funcionarios.values():
        auxM = sl[3]
        if auxM > maior:
            maior = sl[3]
    print(maior)

menu = 1
while menu > 0:
    menu = int(input("""
       |=====================================|
       | [1] - Adicionar funcionários.       |
       |                                     |
       | [2] - Remover funcionários.         |
       |                                     |
       | [3] - Folha de pagamento por ID     |
       |                                     |
       | [4] - Relatório                     |
       |                                     |
       | [5] - Maior salario liquido         |
       |                                     |
       | [6] - Maior número de faltas no mês |
       |                                     |
       | [0] - Sair do programa              |
       |=====================================|
                    OPÇÃO:"""))
    Limpar()
    if menu == 1:
        Cadastro_funcionario()
    elif menu == 2:
        Remover_funcionario()
    elif menu == 3:
        Folha_pagamento()
    elif menu == 4:
        Relatorio()
    elif menu == 5:
        Maior_salario_liquido()