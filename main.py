def criar_mapa_padrao():
	altura = 5
	largura = 5

	bombas = []
	revelado = []
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

	for r, c in coordenadas_bombas:
		bombas[r][c] = True

	return bombas, revelado, altura, largura


def contar_bombas_vizinhas(bombas, altura, largura, linha, coluna):
	total = 0
	for di in [-1, 0, 1]:
		for dj in [-1, 0, 1]:
			if di == 0 and dj == 0:
				continue
			nl = linha + di
			nc = coluna + dj
			if 0 <= nl < altura and 0 <= nc < largura:
				if bombas[nl][nc]:
					total += 1
	return total


def mostrar_mapa(bombas, revelado, altura, largura, mostrar_bombas):
	print()
	print("   ", end="")
	for c in range(largura):
		print(c, end=" ")
	print()
	print("   " + "-" * (largura * 2))

	for l in range(altura):
		print(str(l) + "|", end=" ")
		for c in range(largura):
			if mostrar_bombas and bombas[l][c]:
				print("*", end=" ")
			elif not revelado[l][c]:
				print("#", end=" ")
			elif bombas[l][c]:
				print("*", end=" ")
			else:
				n = contar_bombas_vizinhas(bombas, altura, largura, l, c)
				if n == 0:
					print("-", end=" ")
				else:
					print(n, end=" ")
		print()


def abrir_casa(bombas, revelado, altura, largura, linha, coluna):
	if revelado[linha][coluna]:
		return "repetida"

	revelado[linha][coluna] = True

	if bombas[linha][coluna]:
		return "bomba"

	n = contar_bombas_vizinhas(bombas, altura, largura, linha, coluna)
	if n > 0:
		return "numero"

	# Regra pedida: abre so os 8 vizinhos imediatos (sem recursao).
	for di in [-1, 0, 1]:
		for dj in [-1, 0, 1]:
			if di == 0 and dj == 0:
				continue
			nl = linha + di
			nc = coluna + dj
			if 0 <= nl < altura and 0 <= nc < largura:
				revelado[nl][nc] = True

	return "vazio"


def checar_vitoria(bombas, revelado, altura, largura):
	for l in range(altura):
		for c in range(largura):
			if (not bombas[l][c]) and (not revelado[l][c]):
				return False
	return True


def pedir_linha_coluna(altura, largura):
	while True:
		texto = input("Digite linha e coluna: ")
		partes = texto.split()

		if len(partes) != 2:
			print("Digite exatamente 2 numeros. Exemplo: 2 3")
			continue

		try:
			linha = int(partes[0])
			coluna = int(partes[1])
		except:
			print("Linha e coluna devem ser numeros inteiros.")
			continue

		if linha < 0 or linha >= altura or coluna < 0 or coluna >= largura:
			print("Coordenada fora do mapa.")
			continue

		return linha, coluna


def main():
	print("=== Campo Minado ===")
	print("Mapa fixo de 5x5 carregado dentro do codigo")
	print("Voce so precisa digitar: linha coluna")
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
			print("Voce perdeu.")
			break

		if checar_vitoria(bombas, revelado, altura, largura):
			mostrar_mapa(bombas, revelado, altura, largura, True)
			print("Voce venceu.")
			break


main()
