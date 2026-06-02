dados_missao = [
 [24, 92, 88, 96, 90],
 [27, 80, 72, 94, 85],
 [31, 65, 58, 91, 70],
 [36, 42, 38, 87, 55],
 [39, 28, 19, 78, 35],
 [34, 55, 32, 82, 50]
]
novos_dados = []


def classisficacao_da_missao(valor):
    print("Classificação final da missão:")
    if valor<=2:
        print("MISSÃO ESTÁVEL")
    elif valor >=3 and valor <=5:
        print("MISSÃO EM ATENÇÃO")
    else:
        print("MISSÃO CRÍTICA")

def media_matriz (matriz):
    nomes = ["da temperatura", "da comunicação", "da bateria", "do oxigênio", "da estabilidade"]
    colunas = len(matriz[0])
    for colunas in range(colunas):
        soma=0
        for linhas in matriz:
            soma+=linhas[colunas]

        media = soma/len(matriz)

        print(f"Média {nomes[colunas]}: {media:.2f} ")



def analisar_temperatura(temperatura, pontos):


    if temperatura > 18 and temperatura <= 30:
        print (f"Temperatura: {temperatura}ºC || STATUS: NORMAL || CONDIÇÃO:ESTAVEL")
    elif temperatura > 30 and temperatura <= 35 or temperatura <18:
        print (f"Temperatura: {temperatura}ºC || STATUS: ATENÇÃO || CONDIÇÃO:ALERTA")
        pontos += 1

    else:
        print (f"Temperatura: {temperatura}ºC || STATUS: CRÍTICO || CONDIÇÃO: RISCO DE AQUECIMENTO")
        pontos+=2
    return pontos

def analisar_comunicacao(comuicacao, pontos):
    if comuicacao > 60:
        print (f"SINAL: {comuicacao}% || STATUS: NORMAL || CONDIÇÃO:ESTAVEL")
    elif comuicacao >= 30 and comuicacao <= 59:
        print (f"SINAL: {comuicacao}% || STATUS: ATENÇÃO || CONDIÇÃO:INSTÁVEL")
        pontos += 1

    else:
        print (f"SINAL: {comuicacao}% || STATUS: CRÍTICO || CONDIÇÃO:GRAVE")
        pontos += 2
    return pontos

def analisar_bateria(bateria, pontos):
    if bateria > 50:
        print (f"Bateria: {bateria}% || STATUS: NORMAL || CONDIÇÃO:ESTAVEL")
    elif bateria >= 20 and bateria <= 49:
        print (f"Bateria: {bateria}% || STATUS: ATENÇÃO || CONDIÇÃO:INSTÁVEL")
        pontos += 1

    else:
        print (f"Bateria: {bateria}% || STATUS: CRÍTICO || CONDIÇÃO:GRAVE")
        pontos += 2
    return pontos

def analisar_oxigenio(oxigenio, pontos):
    if oxigenio >= 90:
        print (f"Oxigênio: {oxigenio}% || STATUS: NORMAL || CONDIÇÃO:ESTAVEL")
    elif oxigenio >= 80 and oxigenio <= 89:
        print (f"Oxigênio: {oxigenio}% || STATUS: ATENÇÃO || CONDIÇÃO:INSTÁVEL")
        pontos += 1
    else:
        print (f"Oxigênio: {oxigenio}% || STATUS: CRÍTICO || CONDIÇÃO:GRAVE")
        pontos += 2
    return pontos

def analisar_estabilidade(estabilidade, pontos):
    if estabilidade >= 70:
        print (f"Estabilidade: {estabilidade}% || STATUS: NORMAL || CONDIÇÃO:ESTAVEL")
    elif estabilidade >= 40 and estabilidade <= 69:
        print (f"Estabilidade: {estabilidade}% || STATUS: ATENÇÃO || CONDIÇÃO:INSTÁVEL")
        pontos += 1

    else:
        print (f"Estabilidade: {estabilidade}% || STATUS: CRÍTICO || CONDIÇÃO:GRAVE")
        pontos += 2
    return pontos

print("==========================================================================")
print("                           INICIO DO SISTEMA")
print("==========================================================================")
print("MISSION CONTROL AI:")
print("==========================================================================")
print("Equipe:")
print("José Augusto Ribeiro Freire Manfrinato //RM:571151")
print("Guilherme Figueira Velloso //RM:568827")
print("--------------------------------------------------------------------------")
print("Dados:")
print()

n=0
ciclo=1
pontos=0
temp=0
com=0
bat=0
oxi=0
est=0
while n < len(dados_missao):
    print()
    temperatura,comunicacao, bateria, oxigenio, estabilidade = dados_missao[n]
    print("Ciclo:", ciclo)
    print("------------------------------------------------------------------")
    p_temp = analisar_temperatura(temperatura, pontos)
    p_com =analisar_comunicacao(comunicacao,pontos)
    p_bat =analisar_bateria(bateria, pontos)
    p_oxi =analisar_oxigenio(oxigenio, pontos)
    p_est =analisar_estabilidade(estabilidade, pontos)

    pontos = p_temp + p_com + p_bat + p_oxi + p_est

    print()
    n += 1

    if pontos <=2:
        print()
        print(f"Valor de risco do ciclo: {pontos}")
        print("Classificação do ciclo: Missão estável")
        print("Recomendação: Manter operação normal e continuar monitoramento.")
    elif pontos >=3 and pontos <=5:
        print()
        print(f"Valor de risco do ciclo: {pontos}")
        print("Classificação do ciclo: Missão em Atenção")
        print("Recomendação: Verificar a áreas que está mais instáveis")
    elif pontos >=6 and pontos <=8:
        print()
        print(f"Valor de risco do ciclo: {pontos}")
        print("Classificação do ciclo: Missão em risco")
        print("Recomendação: Verificar áreas mais criticas")
    else:
        print(f"Valor de risco do ciclo: {pontos}")
        print("Classificação do ciclo: Missão em risco")
        print("Recomendação:Ativar modo de segurança e priorizar suporte à vida, energia e comunicação.")



    novos_dados.append(pontos)
    ciclo += 1
    temp += p_temp
    com += p_com
    bat += p_bat
    oxi += p_oxi
    est += p_est
    pontos = 0


print()
print("============================================================")
print("RELATORIO FINAL DA MISSÃO")
print("============================================================")
print()

print(f"Quantidade de ciclos analisados: {len(dados_missao)}")

print()


maxciclo = 0
ciclo = 1
maxpontos = 0

for i in novos_dados:
    if i > maxpontos:
        maxpontos = i
        maxciclo = ciclo

    ciclo += 1



media_matriz(dados_missao)


print()
print(f"Ciclo mais crítico: Ciclo {maxciclo}")
print(f"Maior pontuação de risco: {maxpontos}")

media = sum(novos_dados)/len(novos_dados)
print(f"Risco médio da missao:{media:.2f}")

missaocritica = 0
for i in novos_dados:
    if i >=6:
        missaocritica +=1

print(f"quantidade de ciclos críticos: {missaocritica}")


add = 1
tes = add
for i in novos_dados:
    if i <= 2:
        tes = add
        add /= add
    elif i>=3 and i<=5:
        add += 2/len(novos_dados)
    else:
        add += 3
missao = "Conclusão"
print()
print("Tendência da missão:")
if add == tes:
    print ("missao terminou perfeitamente")
    missao = "A missão apresentou desempenho estável durante todos os ciclos analisados, sem registros de condições de alerta ou risco crítico. Todos os sistemas permaneceram dentro dos parâmetros esperados, indicando operação segura e eficiente da nave."
elif add >= 1 and add <2.6 and tes == 1:
    print ("a missão começou bem e terminou em alerta")
    missao = "A missão iniciou em condições estáveis, porém foram observadas alterações nos indicadores ao longo dos ciclos. Apesar de não apresentar risco crítico, a presença de alertas demonstra a necessidade de monitoramento mais rigoroso para evitar possíveis falhas futuras."
elif add >= 1 and add <2.6 and tes <3:
    print ("A missao teve uma variação durante seu progresso mas terminou bem")
    missao = "Durante a missão foram identificadas oscilações temporárias em alguns sistemas, gerando momentos de atenção. Entretanto, os parâmetros retornaram a níveis adequados ao final da análise, indicando que a missão conseguiu manter sua estabilidade operacional."
elif add <2.6 and tes >=3 and tes <=5:
    print("A missão teve momento de risco mas terminou como planejado")
    missao = "Apesar da ocorrência de situações de risco em determinados ciclos, os sistemas conseguiram se recuperar e concluir a missão dentro do planejado. Recomenda-se investigar as causas dos eventos críticos para aumentar a segurança em futuras operações."
elif add >= 2.6 and add <10 and tes <=3:
    print("Missao teve uma piora durante o tempo")
    missao = "Os indicadores demonstraram deterioração progressiva ao longo da missão, com aumento dos níveis de risco e instabilidade. Embora a missão tenha sido concluída, os resultados apontam a necessidade de ações corretivas e manutenção dos sistemas."
else:
    print("Missao alto risco de falha")
    missao = "A missão apresentou múltiplos ciclos críticos e elevado nível de risco operacional. Os sistemas monitorados registraram condições severas que poderiam comprometer os objetivos da missão. Recomenda-se uma análise completa das falhas antes da realização de novas operações."

ponto = [temp, com, bat, oxi, est]
print()
print(f"Pontuação acumulada por área:")
print(f"Temperatura interna: {temp} pontos")
print(f"Comunicação com a base: {com} pontos")
print(f"Sistema de energia: {bat} pontos")
print(f"Suporte de oxigênio: {oxi} pontos")
print(f"Estabilidade operacional: {est} pontos")



pontotal = 0
for i in ponto:
    if i > pontotal:
        pontotal = i
    elif i == pontotal:
        pontotal = 0

print()
print("Área mais afetada:")
if pontotal ==temp:
    print("Temperatura interna")
elif pontotal ==com:
    print("Comunicação com a base")
elif pontotal ==bat:
    print("Sistema de energia")
elif pontotal == oxi:
    print("Suporte de oxigênio")
elif pontotal ==est:
    print("Estabilidade operacional")
else:
    print("A uma equivalência")
print()

classisficacao_da_missao(media)

print()
print("Conclusão:")
print(missao)

