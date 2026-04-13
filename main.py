# Gabriel Debiasi Meurer, Kamilli Correa, Melissa Melendez
def criar_mapa_padrao():
	altura = 5
	largura = 5

	bombas = []
	revelado = []
	# cria uma matriz de bombas e outra de revelado, ambas com as dimensoes altura x largura, inicialmente com False.
	for _ in range(altura): 
		linha_bombas = []
		linha_revelado = []
		for _ in range(largura):
			linha_bombas.append(False)
			linha_revelado.append(False)
		bombas.append(linha_bombas)
		revelado.append(linha_revelado)

	# Bombas fixas para nao depender de arquivo.
	coordenadas_bombas = [
		(1, 1),
		(2, 3),
		(4, 0),
	]

	# Coloca as bombas nas coordenadas especificadas.
	for r, c in coordenadas_bombas:
		bombas[r][c] = True

	return bombas, revelado, altura, largura # retorna a matriz de bombas, a matriz de revelado, e as dimensoes do mapa (altura e largura).


def contar_bombas_vizinhas(bombas, altura, largura, linha, coluna):
	# Verifica as 8 casas vizinhas pra ver se tem bomba. Se tiver, incrementa o total. No final, retorna o total de bombas vizinhas.
	total = 0
	for di in [-1, 0, 1]: # Loop para percorrer as linhas vizinhas (linha-1, linha, linha+1).
		for dj in [-1, 0, 1]: # Loop para percorrer as colunas vizinhas (coluna-1, coluna, coluna+1).
			if di == 0 and dj == 0:
				continue
			nl = linha + di
			nc = coluna + dj
			if 0 <= nl < altura and 0 <= nc < largura: # Verifica se a coordenada vizinha (nl, nc) esta dentro dos limites do mapa.
				if bombas[nl][nc]:
					total += 1
	return total # Retorna o total de bombas vizinhas encontrado.


def mostrar_mapa(bombas, revelado, altura, largura, mostrar_bombas): # Mostra o mapa escondendo casas não abertas.
	print()
	print("   ", end="")
	for c in range(largura):
		print(c, end=" ") # Imprime os numeros das colunas no topo do mapa.
	print()
	print("   " + "-" * (largura * 2)) # Imprime uma linha horizontal abaixo dos numeros das colunas para separar o cabeçalho do mapa.

	for l in range(altura):
		print(str(l) + "|", end=" ") # Imprime o numero da linha fora do mapa.
		for c in range(largura):
			if mostrar_bombas and bombas[l][c]: # Imprime a bomba quando o mostrar_bombas for True e houver uma bomba na coordenada (l, c).
				print("*", end=" ")
			elif not revelado[l][c]: # Imprime "#" para casas que não foram reveladas (revelado[l][c] é False).
				print("#", end=" ")
			elif bombas[l][c]: # Se a casa foi revelada e tem uma bomba, imprime "*".
				print("*", end=" ")
			else: # Se a casa foi revelada e não tem bomba, conta as bombas vizinhas e imprime o numero correspondente (ou "-" se for 0).
				n = contar_bombas_vizinhas(bombas, altura, largura, l, c)
				if n == 0:
					print("-", end=" ")
				else:
					print(n, end=" ")
		print()


def abrir_casa(bombas, revelado, altura, largura, linha, coluna):
	if revelado[linha][coluna]: # Verifica se o jogador digitou uma cordenada que já foi revelada.
		return "repetida" # Retorna o status da jogada.

	revelado[linha][coluna] = True # Marca a casa como revelada, mesmo que seja uma bomba, para mostrar a bomba no mapa quando o jogador perder.

	if bombas[linha][coluna]: # Verifica se é uma bomba na cordenada digitada.
		return "bomba" # Retorna o status da jogada.

	n = contar_bombas_vizinhas(bombas, altura, largura, linha, coluna) # Joga na função de contar as bombas vizinhas, para saber se tem bombas em volta da casa digitada.
	if n > 0:
		return "numero" # Retorna o status da jogada.

	# Regra pedida: abre só os 8 vizinhos imediatos.
	for di in [-1, 0, 1]:
		for dj in [-1, 0, 1]:
			if di == 0 and dj == 0:
				continue
			nl = linha + di
			nc = coluna + dj
			if 0 <= nl < altura and 0 <= nc < largura:
				revelado[nl][nc] = True

	return "vazio" # Retorna o status da jogada.


def checar_vitoria(bombas, revelado, altura, largura): # Função para checar se o jogador venceu, ou seja, se todas as casas sem bomba foram reveladas.
	for l in range(altura):
		for c in range(largura):
			if (not bombas[l][c]) and (not revelado[l][c]):
				return False
	return True


def pedir_linha_coluna(altura, largura): # Função para pedir as cordenadas ao usuário.
	while True:
		texto = input("Digite linha e coluna: ")
		partes = texto.split() # Divide o texto em partes usando espaço como separador.

		if len(partes) != 2: # verifica se o usuario digitou exatamente 2 partes (linha e coluna).
			print("Digite exatamente 2 numeros. Exemplo: 2 3")
			continue

		try:
			linha = int(partes[0])
			coluna = int(partes[1])
		except:
			print("Linha e coluna devem ser numeros inteiros.")
			continue

		if linha < 0 or linha >= altura or coluna < 0 or coluna >= largura: # Verifica se as cordenadas digitadas estão dentro dos limites do mapa.
			print("Coordenada fora do mapa.")
			continue

		return linha, coluna


def main():
	print("=== Campo Minado ===")
	print("Mapa fixo de 5x5 carregado dentro do codigo")
	print("Você só precisa digitar: linha coluna")
	bombas, revelado, altura, largura = criar_mapa_padrao()

	while True:
		mostrar_mapa(bombas, revelado, altura, largura, False)
		linha, coluna = pedir_linha_coluna(altura, largura)
		resultado = abrir_casa(bombas, revelado, altura, largura, linha, coluna)

		if resultado == "repetida":
			print("Essa casa ja foi aberta.")
			continue

		if resultado == "bomba":
			mostrar_mapa(bombas, revelado, altura, largura, True)
			print("Você perdeu.")
			break

		if checar_vitoria(bombas, revelado, altura, largura):
			mostrar_mapa(bombas, revelado, altura, largura, True)
			print("Você venceu.")
			break


main()
