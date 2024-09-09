tabuleiro = [
    ['   ',  '   ', '   '],
    ['   ',  '   ', '   '],
    ['   ',  '   ', '   ']
]

def exibi_tabuleiro(tabuleiro):
  for linha in tabuleiro:
    print('|'.join(linha))
    print('-'*11)

def movimento_humano(tabuleiro):
  while True:
    try:
      linha = int(input('Escolha a linha (0,1,2): '))
      coluna = int(input('Escolha a coluna (0,1,2): '))
      if tabuleiro[linha][coluna] == '   ':
        return linha, coluna
      else:
        print('Essa casa está ocupada, tente outra!')
    except (ValueError, IndexError):
      print('Entrada inválida! Utilize apenas números entre 0 e 2.')

def verifica_vitoria(tabuleiro, player):
    for linha in tabuleiro:
        if linha[0] == linha[1] == linha[2] == player:
            return True
    
    for col in range(3):
        if tabuleiro[0][col] == tabuleiro[1][col] == tabuleiro[2][col] == player:
            return True
    
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == player:
        return True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == player:
        return True
    
    return False

def verifica_empate(tabuleiro):
    for linha in tabuleiro:
        if '   ' in linha:
            return False 
    return True 

player = ' X '

while True:
    print(f'Turno do Jogador {player}')
    exibi_tabuleiro(tabuleiro)
    x, y = movimento_humano(tabuleiro)
    tabuleiro[x][y] = player

    if verifica_vitoria(tabuleiro, player):
        exibi_tabuleiro(tabuleiro)
        print(f'Jogador {player} venceu!')
        break

    if verifica_empate(tabuleiro):
        exibi_tabuleiro(tabuleiro)
        print('O jogo empatou!')
        break 

    player = ' O ' if player == ' X ' else ' X '