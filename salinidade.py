
#--------------------------------INICIO da função salinidade_ppt------------------------------------

def salinidade_ppt(condutividade_uScm,T_C,P_dBar):
    R = condutividade_uScm/42.914
    rt = 0.6766097+0.0200564*T_C+0.0001104259*(T_C**2)-0.00000069698*(T_C**3)+0.0000000010031*(T_C**3)
    Rp = 1+((0.00002070*P_dBar-0.0000000006370*(P_dBar**2)+0.000000000000003989*(P_dBar**3))/(1+0.03426*T_C+0.0004464*(T_C**2)+0.4215*R-0.003107*(T_C*R)))
    R_t=R/(rt*Rp)
    DeltaS = ((T_C-15.)/(1.+0.0162*(T_C-15.)))*(0.0005-0.0056*(R_t**(1/2))-0.0066*R_t-0.0375*(R_t**(3/2))+0.0636*(R_t**2)-0.0144*(R_t**(5/2)))
    S_15 = 0.008 - 0.1692*(R_t**(1/2)) + 25.3851*R_t+14.0941*(R_t**(3/2))-7.0261*(R_t**2)+2.7081*(R_t**(5/2))
    S = S_15+DeltaS
    return S

#------------------------------FIM da função salinidade_ppt-----------------------------------------

#------------------------------CÓDIGO PRINCIPAL ----------------------------------------------------
print('+ ================================================================================== +')
print('|                                                                                    |')
print('| Título: Cálculo da Salinidade (ppt) a partir da Condutividade                      |')
print('| Referência: Practical Salinity Scale 1978 (PSS-78)                                 |')
print('| Autor: Oceanógrafo Marcelo Di Lello Jordão                                         |')
print('| Data: 13/09/2022                                                                   |')
print('| Contato: dilellocn@gmail.com                                                       |')
print('|                                                                                    |')
print('+ ================================================================================== +\n\n')



condutividade_uScm = []
T_C = [] # International Practical Temperature Scale (1968)
P_dBar = []
while True:
    try:
        opcao = int(input('Escolha a poção desejada [1 ou 2]:\n1 - Iniciar calculadora de Salinidade\n2 - Sair\n>>'))
        if opcao == 1:
            condutividade_uScm = float(input('Entrar com valor de condutividade em microS/cm:\n>> '))
            T_C = float(input('Entrar com valor de temperatura em graus Celsius (ITPS68):\n>> '))
            P_dBar = float(input('Entrar com valor de pressão em dBar (no caso de 1 atm = 10.1325 dBar):\n>> '))
            salinidade = salinidade_ppt(condutividade_uScm,T_C,P_dBar)
            format_float = "{:.2f}".format(salinidade)
            print('A salinidade é '+format_float+' ppt')
            continue
        else:
            break
    except ValueError:
        print('Opção inválida. Entrar novamente, apenas com números.')
        continue
print('Programa finalizado!')

#------------------------------FIM DO CÓDIGO PRINCIPAL----------------------------------------------
