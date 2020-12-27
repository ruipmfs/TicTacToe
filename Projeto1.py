# Rui Pedro Santos   Aluno nº 98966

X = 1
O = -1
livre = 0
EMPATE = 0
nLinhas = 3
nColunas = 3

def eh_tabuleiro(tab):
	'''Recebe um tabuleiro e verifica se ele e valido ou nao

	INPUT: tabuleiro   OUTPUT: booleano (True or False)'''

	contador = 0
	# Se o contador chegar ao 9 significa que todas as posicoes / constituicao do tabuleiro sao validas

	if (type(tab) == tuple) and (len(tab) == 3):
		for l in range(nLinhas):
			if (type(tab[l]) == tuple) and (len(tab[l]) == 3):
				for c in range(nColunas):
					if (type(tab[l][c]) == int):
						if (tab[l][c] == livre) or (tab[l][c] == X) or (tab[l][c] == O):
							contador += 1
	return contador == 9


def eh_posicao(pos):
	'''Recebe um valor da posicao e devolve se a posicao e valida ou nao

	INPUT: posicao   OUTPUT: booleano (True or False)'''

	return (type(pos) == int) and (pos >= 1) and (pos <= 9)

def obter_coluna(tab, val):
	'''Recebe um tabuleiro e um inteiro entre 1 e 3 e devolve a coluna correspondente em vetor

	INPUT: tabuleiro, inteiro   OUTPUT: vetor (coluna)'''

	if not eh_tabuleiro(tab):
		raise ValueError('obter_coluna: algum dos argumentos e invalido')
	if (type(val) != int) or (val < 1) or (val > 3):
		raise ValueError('obter_coluna: algum dos argumentos e invalido')

	coluna = (tab[0][val-1], tab[1][val-1], tab[2][val-1])
	return coluna

def obter_linha(tab, val):
	'''Recebe um tabuleiro e um inteiro entre 1 e 3 e devolve a linha correspondente em vetor

	INPUT: tabuleiro, inteiro   OUTPUT: vetor (linha)'''

	if not eh_tabuleiro(tab):
		raise ValueError('obter_linha: algum dos argumentos e invalido')
	if type(val) != int or val < 1 or val > 3:
		raise ValueError('obter_linha: algum dos argumentos e invalido')

	linha = tab[val-1]
	return linha

def obter_diagonal(tab, val):
	'''Recebe um tabuleiro e um inteiro (1 ou 2) e devolve a diaginal correspondente em vetor

	INPUT: tabuleiro, inteiro   OUTPUT: vetor (linha)'''

	if not eh_tabuleiro(tab):
		raise ValueError('obter_diagonal: algum dos argumentos e invalido')
	if type(val) != int or val < 1 or val > 2:
		raise ValueError('obter_diagonal: algum dos argumentos e invalido')

	elif val == 1:
		diagonal = (tab[0][0], tab[1][1], tab[2][2])
	elif val == 2:
		diagonal = (tab[2][0], tab[1][1], tab[0][2])
	return diagonal

def tabuleiro_str(tab):
	'''Recebe um tabuleiro e devolve uma cadeia de caracteres com a representacao do tabuleiro

	INPUT: tabuleiro   OUTPUT: cadeia de carateres (tabuleiro)'''

	if not eh_tabuleiro(tab):
		raise ValueError('tabuleiro_str: o argumento e invalido')

	grelha = ''

	#Construcao da grelha caracter a caracter, devolvendo a grelha no final da funcao
	for l in range(nLinhas):
		for c in range(nColunas):
			if tab[l][c] == X:
				grelha += ' X '
			elif tab[l][c] == O:
				grelha += ' O '
			else:
				grelha += '   '

			if c != 2:
				grelha += '|'
		if l != 2:
			grelha += '\n-----------\n'

	return grelha

def eh_posicao_livre(tab, pos):
	'''Recebe um tabuleiro e uma posicao e avalia se esta e livre (se estiver a 0) e devolve
	se esta e verdadeira ou falsa

	INPUT: tabuleiro, posicao   OUTPUT: booleano (True or False)'''

	if not eh_tabuleiro(tab):
		raise ValueError('eh_posicao_livre: algum dos argumentos e invalido')
	if type(pos) != int or pos < 1 or pos > 9:
		raise ValueError('eh_posicao_livre: algum dos argumentos e invalido')

	i = 0
	for l in range(nLinhas):
		for c in range(nColunas):
			i += 1
			if tab[l][c] == livre:
				if i == pos:
					return True
	return False

def obter_posicoes_livres(tab):
	'''Recebe um tabuleiro e devolve um tuplo com todas as posicoes livres do tabuleiro (0)

	INPUT: tabuleiro   OUTPUT: tuplo'''

	if not eh_tabuleiro(tab):
		raise ValueError('obter_posicoes_livres: o argumento e invalido')

	i = 0
	posLiv = ()
	for l in range(nLinhas):
		for c in range(nColunas):
			i += 1
			if tab[l][c] == livre:
				posLiv += (i,)
	return posLiv

def jogador_ganhador(tab):
	'''Recebe um tabuleiro e devolve um inteiro (-1 se o jog. 'O' ganhou, 0 se houve empate,
	1 se o jog. 'X' ganhou)

	INPUT: tabuleiro   OUTPUT: inteiro (-1, 0, 1)'''

	if not eh_tabuleiro(tab):
		raise ValueError('jogador_ganhador: o argumento e invalido')

	for l in range(nLinhas):
		if tab[l] == (1, 1, 1):
			return X
		elif tab[l] == (-1, -1, -1):
			return O

	for c in range(nColunas):
		if tab[0][c] == tab[1][c] == tab[2][c] == X:
			return X
		elif tab[0][c] == tab[1][c] == tab[2][c] == O:
			return O

	if (tab[0][0] == tab[1][1] == tab[2][2] == X) or (tab[2][0] == tab[1][1] == tab[0][2] == X):
		return X
	elif (tab[0][0] == tab[1][1] == tab[2][2] == O) or (tab[2][0] == tab[1][1] == tab[0][2] == O):
		return O

	return 0

def marcar_posicao(tab, ID, pos):
	'''Recebe um tabuleiro, um identificador do jogador (ID) e um inteiro correspondente a uma
	 posicao do tabuleiro. Devolve um tabuleiro novo com a nova posicao inserida
	 
	 INPUT: tabuleiro, ID, posicao   OUTPUT: tabuleiro (novo)'''

	novoTab = ()
	i = 0

	if not eh_tabuleiro(tab):
		raise ValueError('marcar_posicao: algum dos argumentos e invalido')
		
	if (ID != X and ID != O) or type(ID) != int:
		raise ValueError('marcar_posicao: algum dos argumentos e invalido')

	if not eh_posicao(pos):
		raise ValueError('marcar_posicao: algum dos argumentos e invalido')

	if not eh_posicao_livre(tab, pos):
		raise ValueError('marcar_posicao: algum dos argumentos e invalido')
	
	for l in range(nLinhas):
		novaLinha = ()
		for c in range(nColunas):
			i += 1
			if pos == i:
				novaLinha += (ID,)
			else:
				novaLinha += (tab[l][c],)
		novoTab += (novaLinha,)

	if (eh_tabuleiro(novoTab) == False) or novoTab == ((0, 0, 0), (0, 0, 0), (0, 0, 0)):
		raise ValueError('marcar_posicao: algum dos argumentos e invalido')

	return novoTab

def escolher_posicao_manual(tab):
	'''Verifica um tabuleiro que lhe e dado, e devolve uma posicao do tabuleiro que e inserida
	manualmente pelo jogador
	
	INPUT: tabuleiro   OUTPUT: posicao'''
	
	if not eh_tabuleiro(tab):
		raise ValueError('escolher_posicao_manual: o argumento e invalido')

	pos = eval(input('Turno do jogador. Escolha uma posicao livre: '))

	if (type(pos) != int) or (pos < 1) or (pos > 9):
		raise ValueError('escolher_posicao_manual: a posicao introduzida e invalida')

	if not eh_posicao_livre(tab, pos):
		raise ValueError('escolher_posicao_manual: a posicao introduzida e invalida')

	return pos

def escolher_posicao_auto(tab, botID, estg):
	'''Recebe um tabuleiro e le a posicao introduzida manualmente pelo jogador, devolvendo
	outra posicao que varia consoante a estrategia (estg)
	
	INPUT: tabuleiro, ID (bot), estrategia   OUTPUT: posicao'''

	if not eh_tabuleiro(tab):
		raise ValueError('escolher_posicao_auto: algum dos argumentos e invalido')

	if botID != X and botID != O or type(botID) != int:
		raise ValueError('escolher_posicao_auto: algum dos argumentos e invalido')

	if type(estg) != str or estg != 'basico' and estg != 'normal' and estg != 'perfeito':
		raise ValueError('escolher_posicao_auto: algum dos argumentos e invalido')

	if estg == 'basico':
		return estg_basico(tab, botID)
	if estg == 'normal':
		return estg_normal(tab, botID)
	if estg == 'perfeito':
		return estg_perfeito(tab, botID)

	
def vitoria_bloqueio(tab, botID, operacao):
	'''FUNCAO AUXILIAR:
	Recebe o tabuleiro, o identificador do computador, e a operacao (vitoria ou bloqueio).
	Esta ultima ira decidir se o objetivo e ganhar o jogo (vitoria) ou bloquear o adversario
	(bloqueio). Devolve uma posicao do tabuleiro se a vitoria/bloqueio for possivel ou -1 se
	nenhuma for possivel
	
	INPUT: tabuleiro, ID (bot), operacao   OUTPUT: posicao'''

	if operacao == 'vitoria':
		jogadorID = botID
		simbolo = botID
	elif operacao == 'bloqueio':
		jogadorID = -botID
		simbolo = botID

	for l in range(nLinhas):
		if (tab[l][0] == tab[l][1] == jogadorID) and eh_posicao_livre(tab, 3*l+3):
			return 3*l+3
		elif (tab[l][0] == tab[l][2] == jogadorID) and eh_posicao_livre(tab, 3*l+2):
			return 3*l+2
		elif (tab[l][1] == tab[l][2] == jogadorID) and eh_posicao_livre(tab, 3*l+1):
			return 3*l+1

	for c in range(nColunas):
		if (tab[0][c] == tab[1][c] == jogadorID) and eh_posicao_livre(tab, 7+c):
			return 7+c
		elif (tab[0][c] == tab[2][c] == jogadorID) and eh_posicao_livre(tab, 4+c):
			return 4+c
		elif (tab[1][c] == tab[2][c] == jogadorID) and eh_posicao_livre(tab, 1+c):
			return 1+c

	if tab[0][0] == tab [1][1] == jogadorID and eh_posicao_livre(tab, 9):
		return 9
	elif tab[0][0] == tab[2][2] == jogadorID and eh_posicao_livre(tab, 5):
		return 5
	elif tab[1][1] == tab[2][2] == jogadorID and eh_posicao_livre(tab, 1):
		return 1
	elif tab[2][0] == tab[1][1] == jogadorID and eh_posicao_livre(tab, 3):
		return 3
	elif tab[2][0] == tab[0][2] == jogadorID and eh_posicao_livre(tab, 5):
		return 5
	elif tab[1][1] == tab[0][2] == jogadorID and eh_posicao_livre(tab, 7):
		return 7

	return -1

def crit_1(tab, botID):
	'''CRITERIO 1 (Vitoria):
	Se o jogador tiver duas das suas pecas em linha e uma posicao livre, entao deve
	marcar na posicao livre (ganhando o jogo)
	
	INPUT: tabuleiro, ID (bot)   OUTPUT: posicao'''

	return vitoria_bloqueio(tab, botID, 'vitoria')

def crit_2(tab, botID):
	'''CRITERIO 2 (Bloqueio):
	Se o adversario tiver duas das suaspecas em linha e uma posicao livre entao deve marcar
	na posicao livre (para bloquear o adversario)
	
	INPUT: tabuleiro, ID (bot)   OUTPUT: posicao'''

	return vitoria_bloqueio(tab, botID, 'bloqueio')

def crit_3(tab, botID):
	'''Se o adversario tiver apenas uma bifurcacao entao o jogador deve bloquear a bifurcacao (escolher a posicao
	livre da intersecao) senao o jogador deve criar um dois em linha para forcar o oponente a defender, desde que a defesa
	nao resulte na criacao de uma bifurcacao para o oponente
	
	INPUT: tabuleiro, ID (bot)   OUTPUT: posicao'''

	return -1

def crit_4(tab, botID):
	'''Se o jogadortiver duas linhas/colunas/diagonais que se intersetam, onde cada contem uma das suas pecas
	e se a posicao de intersecao estiver livre entao deve marcarna posicao de intersecao (criando duas hipoteses
	de vitoria na jogada seguinte)
	
	INPUT: tabuleiro, ID (bot)   OUTPUT: posicao'''
	return -1

def crit_5(tab, botID):
	'''CRITERIO 5 (Centro):
	Se a posicao central do tabuleiro (5) estiver livre, marcar a posicao central
	
	INPUT: tabuleiro, ID (bot)   OUTPUT: posicao'''

	if eh_posicao_livre(tab, 5) == True:
		return 5
	return -1

def crit_6(tab, botID):
	'''CRITERIO 6 (Canto oposto):
	Se o adversario estiver num canto e se o canto diagonalmente oposto estiver livre, marque-o
	
	INPUT: tabuleiro, ID (bot)   OUTPUT: posicao'''

	if tab[0][0] == -botID and eh_posicao_livre(tab, 9):
		return 9
	elif tab[0][2] == -botID and eh_posicao_livre(tab, 7):
		return 7
	elif tab[2][0] == -botID and eh_posicao_livre(tab, 3):
		return 3
	elif tab[2][2] == -botID and eh_posicao_livre(tab, 1):
		return 1
	return -1

def crit_7(tab, botID):
	'''CRITERIO 7 (Canto vazio):
	Se o adversario estiver num canto e se o canto diagonalmente oposto estiver livre, marque-o
	
	INPUT: tabuleiro, ID (bot)   OUTPUT: posicao'''

	if tab[0][0] == 0 and eh_posicao_livre(tab, 1):
		return 1
	elif tab[0][2] == 0 and eh_posicao_livre(tab, 3):
		return 3
	elif tab[2][0] == 0 and eh_posicao_livre(tab, 7):
		return 7
	elif tab[2][2] == 0 and eh_posicao_livre(tab, 9):
		return 9
	return -1

def crit_8(tab, botID):
	'''CRITERIO 8 (Lateral vazio):
	Se uma posicao lateral (que nem e o centro, nem um canto) for livre, entao jogar nesse lateral
	
	INPUT: tabuleiro, ID (bot)   OUTPUT: posicao'''

	if tab[0][1] == 0 and eh_posicao_livre(tab, 2):
		return 2
	if tab[1][0] == 0 and eh_posicao_livre(tab, 4):
		return 4
	if tab[1][2] == 0 and eh_posicao_livre(tab, 6):
		return 6
	if tab[2][1] == 0 and eh_posicao_livre(tab, 8):
		return 8
	return -1

def estg_basico(tab, botID):
	'''ESTRATEGIA BASICA
	Esta funcao auxiliar recebe o tabuleiro e o ID (bot) e devolve uma posicao. Essa posicao e gerida
	pela ordem de criterios definida no enunciado para a estrategia basica (5, 7, 8)
	
	INPUT: tabuleiro, ID (bot)   OUTPUT: posicao'''
	
	posDisponiveis = obter_posicoes_livres(tab)
	
	crit5 = crit_5(tab, botID)
	if crit5 in posDisponiveis:
		return crit5

	crit7 = crit_7(tab, botID)
	if crit7 in posDisponiveis:
		return crit7
		
	crit8 = crit_8(tab, botID)
	if crit8 in posDisponiveis:
		return crit8
	
def estg_normal(tab, botID):
	'''ESTRATEGIA NORMAL
	Esta funcao auxiliar recebe o tabuleiro e o ID (bot) e devolve uma posicao. Essa posicao e gerida
	pela ordem de criterios definida no enunciado para a estrategia normal (1, 2, 5, 6, 7, 8)
	
	INPUT: tabuleiro, ID (bot)   OUTPUT: posicao'''

	posDisponiveis = obter_posicoes_livres(tab)

	crit1 = crit_1(tab, botID)
	if crit1 in posDisponiveis:
		return crit1

	crit2 = crit_2(tab, botID)
	if crit2 in posDisponiveis:
		return crit2
		
	crit5 = crit_5(tab, botID)
	if crit5 in posDisponiveis:
		return crit5

	crit6 = crit_6(tab, botID)
	if crit6 in posDisponiveis:
		return crit6

	crit7 = crit_7(tab, botID)
	if crit7 in posDisponiveis:
		return crit7
		
	crit8 = crit_8(tab, botID)
	if crit8 in posDisponiveis:
		return crit8

def estg_perfeito(tab, botID):
	'''ESTRATEGIA PERFEITA
	Esta funcao auxiliar recebe o tabuleiro e o ID (bot) e devolve uma posicao. Essa posicao e gerida
	pela ordem de criterios definida no enunciado para a estrategia perfeita (1, 2, 3, 4, 5, 6, 7, 8)
	
	INPUT: tabuleiro, ID (bot)   OUTPUT: posicao'''

	posDisponiveis = obter_posicoes_livres(tab)

	crit1 = crit_1(tab, botID)
	if crit1 in posDisponiveis:
		return crit1

	crit2 = crit_2(tab, botID)
	if crit2 in posDisponiveis:
		return crit2

	crit3 = crit_3(tab, botID)
	if crit3 in posDisponiveis:
		return crit3

	crit4 = crit_4(tab, botID)
	if crit4 in posDisponiveis:
		return crit4
		
	crit5 = crit_5(tab, botID)
	if crit5 in posDisponiveis:
		return crit5

	crit6 = crit_6(tab, botID)
	if crit6 in posDisponiveis:
		return crit6

	crit7 = crit_7(tab, botID)
	if crit7 in posDisponiveis:
		return crit7
		
	crit8 = crit_8(tab, botID)
	if crit8 in posDisponiveis:
		return crit8

def jogo_do_galo(ID, estg):
	'''Funcao pricipal do projeto. Recebe o identificador do jogador e a estrategia e devolve dois
	tabuleiros a cada jogada: um tabuleiro com a jogada do jogador e outro com a jogada do computador
	
	INPUT: ID (jogador), estrategia   OUTPUT: tabuleiro (2)'''

	tab = ((0, 0, 0),(0, 0, 0),(0, 0, 0))
	if ID == 'O':
		jogadorID = O
	elif ID == 'X':
		jogadorID = X
	else:
		raise ValueError('jogo_do_galo: algum dos argumentos e invalido')

	botID = -jogadorID

	print("Bem-vindo ao JOGO DO GALO.\nO jogador joga com '" + ID + "'.")

	#Funcoes auxiliares para as jogadas (jogador e computador)
	
	def jogada_jogador(tab, jogadorID):
		'''Realiza a jogada por parte do jogador

		INPUT: tabuleiro, ID (jogador)   OUTPUT: tabuleiro'''

		pos = escolher_posicao_manual(tab)
		tab = marcar_posicao(tab, jogadorID, pos)
		return tab

	def jogada_bot(tab, botID, estg):
		'''Realiza a jogada do computador

		INPUT: tabuleiro, ID (computador)'''

		pos = escolher_posicao_auto(tab, botID, estg)
		tab = marcar_posicao(tab, botID, pos)
		print("Turno do computador (" + estg + "):")
		return tab

	vencedor = False
	nPosicoesLivres = 9
	resultado = EMPATE
	vezJogador = False

	if (jogadorID == X):
		vezJogador = True

	while (not vencedor and nPosicoesLivres != 0):

		if vezJogador:
			tab = jogada_jogador(tab, jogadorID)
		
		else:
			tab = jogada_bot(tab, botID, estg)
			
		print(tabuleiro_str(tab))
		resultado = jogador_ganhador(tab)

		if resultado != EMPATE:
			vencedor = True

		vezJogador = not vezJogador
		nPosicoesLivres -= 1

	if resultado == X:
		return 'X'
	elif resultado == O:
		return 'O'
	else:
		return 'EMPATE'