# -*- coding: utf-8 -*-
# Como estou usando o Python 3.6.4 devo usar o BeautifulSoup 4.4.6 (usei versões anteriores e não funcionou)

from bs4 import BeautifulSoup
arquivo = "x.html"
ref_arquivo = open(arquivo,"r")
arquivoLido = ref_arquivo.read()
soup = BeautifulSoup(arquivoLido, 'html.parser')
tabela = soup.find(id="accordion")
hora = soup.select("td")
contador  = 1
resultados = []
resultado = ""
for i in hora:
	elemento = i.find(text=True)
	if contador <= 4:
		resultado += str(elemento) + ","
		contador += 1
	elif contador == 8:
		contador = 1
		resultados.append(resultado)
		resultado = ""
	else:
		contador += 1

tamanhoAnterior  = 0
contador = 0
resultado = ""
niveis_intermediario = []
tabela2 = soup.find_all(class_='fightlog')
niveis = soup.select("dd")
for i in range(len(niveis)):
	elemento = niveis[i].find(text=True)
	if tamanhoAnterior > 5 and len(elemento) <= 3 and contador>6:
		contador = 0	
	if contador == 0:
		resultado += str(elemento) + ","		
		contador += 1			
	elif contador == 7:
		resultado += str(elemento) + ","
		niveis_intermediario.append(resultado)
		resultado = ""	
	tamanhoAnterior = len(elemento)
	contador += 1

resultadofinal = []

for i in range(len(resultados)):
	selecao = resultados[i] + niveis_intermediario[i]
	resultadofinal.append(selecao)

#print (resultadofinal)
contador = 0
soma = ""
nomeDoJogador = "x"

for linha in resultadofinal:		
	dia = int(linha[0:2])
	if (dia <= 10):
		linhaSplit = linha.split(",")		
		if (linhaSplit[2] == nomeDoJogador):
			#print (linhaSplit)
			nivelAtacante = int(linhaSplit[5])
			nivelDefensor = int(linhaSplit[6])
			diferenca = nivelDefensor - nivelAtacante
			if (diferenca >0):
				print (linhaSplit)
				soma += " + " + str(diferenca)
				contador += diferenca

print ("Todos os pontos obtidos" + soma)
print ("Pontuação Final: " + str(contador))
			
	

