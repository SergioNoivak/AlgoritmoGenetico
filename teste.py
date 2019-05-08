
import unittest
import sys
import algoritmos
import constantes

class TesteAlgoritmoGenetico(unittest.TestCase):
    def testeTamanho(self):
         self.assertEqual(len(algoritmos.criar_populacao()),constantes.tamanho_populacao,"o tamanho da populacao esta incorreto")
         
    def testeSelecao(self):
        for i in range(0,100):
            populacao = algoritmos.criar_populacao()
            indice_selecionado = algoritmos.selecao(populacao)
            self.assertTrue(indice_selecionado<constantes.tamanho_populacao and indice_selecionado>=0,"A selecao de roleta escolheu indices fora da faixa")
    def testeEscolhaPais(self):
            for i in range(0,100):
                populacao = algoritmos.criar_populacao()
                lista_de_pais = algoritmos.selecionar_pais(populacao)
                for pai in lista_de_pais:
                      self.assertTrue(pai>=constantes.inicio_intervalo and pai <= constantes.fim_intervalo, "há algum pai selecionado fora do intervalo")                  
                
    def testeCruzamento(self):
            for i in range(0,100):
                populacao = algoritmos.criar_populacao()
                lista_de_pais = algoritmos.selecionar_pais(populacao)
                nova_populacao =  algoritmos.reproduzir(lista_de_pais)
                for individuo in nova_populacao:
                      self.assertTrue(individuo>=constantes.inicio_intervalo and individuo <= constantes.fim_intervalo, "há algum individuo incorreto depois do cruzamento")                  
                    
                    
    def testeMutacao(self):
            for i in range(0,100):
                populacao = algoritmos.criar_populacao()
                lista_de_pais = algoritmos.selecionar_pais(populacao)
                nova_populacao =  algoritmos.reproduzir(lista_de_pais)
                algoritmos.mutar(nova_populacao)
                for individuo in nova_populacao:
                      self.assertTrue(individuo>=constantes.inicio_intervalo and individuo <= constantes.fim_intervalo, "há algum individuo incorreto depois do cruzamento")                  
            
            

if __name__ == '__main__':
    unittest.main()