import math

tamanho_populacao = 1000
inicio_intervalo = 0
fim_intervalo = 5
numero_de_pais = 10
numero_de_mutados = 5
taxa_mutacao = 0.01
numero_geracoes = 400

def funcao_fitness(x):
    return math.sin(x*x)/(3-math.cos(math.e)-x)+40