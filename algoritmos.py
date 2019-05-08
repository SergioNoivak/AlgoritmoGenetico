import random
import constantes

def criar_populacao():
    tamanho_populacao=constantes.tamanho_populacao
    inicioIntervalo=constantes.inicio_intervalo
    fimIntervalo=constantes.fim_intervalo
    populacao = []
    for i in range(0,tamanho_populacao):
        populacao.append(random.uniform(inicioIntervalo,fimIntervalo))
    return populacao


def selecao(populacao):
    soma_aptidoes = 0
    for individuo in populacao:
        fitness = constantes.funcao_fitness(individuo)
        if(fitness >0):
            soma_aptidoes+=fitness 
        else:
            soma_aptidoes+=0.000001
    valor = random.uniform(0,1)*soma_aptidoes
    for i in range(0,len(populacao)):
        fitness = constantes.funcao_fitness(individuo)
        individuo = populacao[i]
        if(fitness >0):
            valor-=fitness
            if(valor<0):
                return i
    return len(populacao)-1
    
        
def selecionar_pais(populacao):
    lista_de_pais = []
    for i in range(0, constantes.numero_de_pais):
        indice_escolhido = selecao(populacao)
        lista_de_pais.append(populacao[indice_escolhido])
    
    return lista_de_pais
    

def crossover(pai1,pai2):
    percentual = random.uniform(0,1)
    percentual2 = random.uniform(0,1)
    filho = pai1*percentual +pai2*percentual2
    filho/= (pai1+pai2)*random.uniform(0,1)
    return filho
    

def reproduzir(lista_de_pais):
    nova_populacao = []
    for i in range(0,constantes.tamanho_populacao):
        indice_pai1=int(random.uniform(0,len(lista_de_pais)  -1))
        indice_pai2=int(random.uniform(0,len(lista_de_pais)  -1))
        nova_populacao.append(crossover(lista_de_pais[indice_pai1],lista_de_pais[indice_pai2]))
    
    return nova_populacao


# def reproduzir2(lista_de_pais):
#     nova_populacao = []
#     i=0
#     while i<lista_de_pais:
        
    
#     for i in range(0,constantes.tamanho_populacao):
#         indice_pai1=int(random.uniform(0,len(lista_de_pais)  -1))
#         indice_pai2=int(random.uniform(0,len(lista_de_pais)  -1))
#         nova_populacao.append(crossover(lista_de_pais[indice_pai1],lista_de_pais[indice_pai2]))
    
#     return nova_populacao




def metodo_mutacao(individuo):
    
    # return random.uniform(0,constantes.fim_intervalo)
    numero_aleatorio = round(random.uniform(0,1))
    if(numero_aleatorio==0):
        if (individuo + constantes.taxa_mutacao)>constantes.fim_intervalo:
            individuo =constantes.fim_intervalo
        elif (individuo + constantes.taxa_mutacao)<constantes.inicio_intervalo:
            individuo =constantes.inicio_intervalo
        elif (individuo + constantes.taxa_mutacao)<constantes.fim_intervalo and (individuo +constantes.taxa_mutacao)>constantes.inicio_intervalo:
            individuo += constantes.taxa_mutacao
            
    else:
        if (individuo - constantes.taxa_mutacao)>constantes.fim_intervalo:
            individuo =constantes.fim_intervalo
        elif (individuo - constantes.taxa_mutacao)<constantes.inicio_intervalo:
            individuo =constantes.inicio_intervalo
        elif (individuo - constantes.taxa_mutacao)<constantes.fim_intervalo and (individuo +constantes.taxa_mutacao)>constantes.inicio_intervalo:
            individuo -=constantes.taxa_mutacao
               
    
    
    
def mutar(populacao):
    for i in range(0,constantes.numero_de_mutados):
        indice=int(random.uniform(0,len(populacao)-1))
        metodo_mutacao(populacao[indice])


def algoritmo_genetico():
    populacao = criar_populacao()
    for i in range(0,constantes.numero_geracoes):
        lista_de_pais = selecionar_pais(populacao)
        nova_populacao =  reproduzir(lista_de_pais)
        mutar(nova_populacao)
        
        populacao = nova_populacao
        
    
    maior = -999999999
    indice = -1
    i=0
    for individuo in populacao:
        if constantes.funcao_fitness(individuo)>maior:
            maior = constantes.funcao_fitness(individuo)
            indice = i
        i=i+1
    return [populacao[indice],maior]
    
    