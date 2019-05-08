
import algoritmos
import view

# função AlgoritmoGenético(população, função-objetivo) saídas: indivíduo
#   entradas: população→ uma lista de indivíduos
#             função-objetivo→ uma função que recebe um indivíduo e retorna um número real.
#   repetir
#      lista de pais := seleção(população, função-objetivo)
#      população := reprodução(lista de pais)
#   enquanto nenhuma condição de parada for atingida
#   retorna o melhor indivíduo da população de acordo com a função-objetivo

ponto = algoritmos.algoritmo_genetico()

print("X: ",ponto[0],"Y: ",ponto[1])
view.exibir_funcao(ponto[0],ponto[1])












