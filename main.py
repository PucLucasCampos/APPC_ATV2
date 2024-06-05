import os
funcionarios = {}

def Limpar():
    os.system("cls")

def Calculo_imposto(salario_bruto):
    if salario_bruto < 2259.20:
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
    id_matricula = int(input("Digite o ID da matrícula:"))
    # VALIDAÇÃO MATRICULA
    while id_matricula in funcionarios:
        print("ID de matricula ja existe >>> Tente novamente!!! ")
        id_matricula = int(input("Digite o ID da matrícula:"))
    nome = str(input("Nome do funcionario: "))
    print("[101] - Vendedor\n[102] - Administrativo")
    cod_funcao = int(input("Código da função: "))
    #! VALIDAÇÃOO COD FUNÇÃO
    while cod_funcao != 101 and cod_funcao != 102:
        print("Código da função invalido >>> Tente novamente!!! ")
        cod_funcao = int(input("Código da função: "))
    numero_faltas = int(input("Número de faltas por mês: "))
    # SALARIO FUNÇÃO 101
    if cod_funcao == 101: 
        salario_fixo = 1500
        falta = (salario_fixo / 30) * numero_faltas
        volume_vendas = int(input("Volume de vendas: "))
        salario_bruto = (volume_vendas * 0.9) + 1500 - falta
        imposto = Calculo_imposto(salario_bruto)
        salario_liquido = salario_bruto - (salario_bruto * imposto)
    # SALARIO FUNÇÃO 102
    else: 
        print("Salário varia entre R$2150,00 até R$6950,00")
        salario_fixo = float(input("Salário do funcionário: "))
        # VALIDAÇÃO 2150 < SALARIO FIXO < 6950
        while salario_fixo < 2150 or salario_fixo > 6950:
            print("Por favor, digite um salário dentro da faixa especificada.")
            salario_fixo = float(input("Salário do funcionário: "))
        falta = (salario_fixo / 30) * numero_faltas
        salario_bruto = salario_fixo - falta
        imposto = Calculo_imposto(salario_bruto)
        salario_liquido = salario_bruto - (salario_bruto * imposto)
    
    funcionarios[id_matricula] = [nome, cod_funcao, numero_faltas, salario_liquido, salario_bruto, imposto, falta]

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
    if key not in funcionarios.keys():
        print(">>> ID não existe")
    else:
        print(f"""
        ID: {key}
        NOME: {funcionarios[key][0]}
        CODIGO: {funcionarios[key][1]}
        SALÁRIO BRUTO: R${funcionarios[key][4]:.2f}
        PORCENTUAL DE IMPOSTO: {funcionarios[key][5] * 100:.2f}%
        """)

def Relatorio():
    print("Relatório com salario bruto e liquido de todos os funcionarios")
    print("\nMATRÍCULA\tNOME\t\tCÓDIGO\t\tSALÁRIO BRUTO\t\tSALÁRIO LIQUIDO")
    for id, index in funcionarios.items():
            print(f"{id}\t\t{index[0]}\t\t{index[1]}\t\t{index[4]:.2f}\t\t\t{index[3]:.2f}")

def Maior_salario_liquido():
    maior = 0
    key = 0

    for id, func in funcionarios.items():
        if func[3] > maior:
            maior = func[3]
            key = id
    func_maior = funcionarios[key]   
    print(f"""
        ID: {key}
        NOME: {func_maior[0]}
        CODIGO: {func_maior[1]}
        SALÁRIO BRUTO: R$ {func_maior[4]:.2f}
        SALÁRIO LIQUIDO: R$ {func_maior[3]:.2f}
        """)
    
def Mais_faltas():
    maior = 0
    key = 0

    for id, func in funcionarios.items():
        if func[2] > maior:
            maior = func[2]
            key = id
    func_maior = funcionarios[key] 
    print(f"""
        ID: {key}
        NOME: {func_maior[0]}
        CODIGO: {func_maior[1]}
        NÚMERO DE FALTAS: {func_maior[2]:.2f}
        DESCONTO: {func_maior[6]:.2f}
        """)

menu = 1
while menu > 0:
    menu = int(input(""" 
            ╔════════════════════════════════════╗
                            MENU  
            ╚════════════════════════════════════╝
                  [1] - Inserir Funcionários 
                     
                  [2] - Remover Funcionários 
                     
                  [3] - Folha de Pagamento
                     
                  [4] - Relatório de Salário
                     
                  [5] - Maior Salário Liquido
                     
                  [6] - Maior número de faltas
            ╚═════════════════════════════════════╝
                          OPÇÃO: """))
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
    elif menu == 6:
        Mais_faltas()