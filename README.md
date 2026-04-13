# Campo Minado em Python

Projeto simples de **Campo Minado no terminal**, feito em Python, com mapa fixo de `5x5` e bombas definidas no próprio código.

## Funcionalidades

- Mapa `5x5` com casas ocultas (`#`)
- Bombas fixas no mapa
- Entrada do jogador por coordenadas: `linha coluna`
- Abertura de casa selecionada
- Exibição de número de bombas vizinhas
- Condição de derrota ao abrir bomba
- Condição de vitória ao revelar todas as casas sem bomba

## Regras do jogo

- Você deve digitar duas posições: `linha` e `coluna`
- Se abrir uma bomba (`*`), o jogo termina com derrota
- Se abrir uma casa segura:
  - mostra um número (`1`, `2`, etc.) quando há bombas vizinhas
  - mostra `-` quando não há bombas vizinhas
- Quando abre uma casa vazia (`0` bombas vizinhas), o programa abre os 8 vizinhos imediatos (sem recursão)

## Como executar

1. Tenha Python 3 instalado.
2. No terminal, entre na pasta do projeto.
3. Execute:

```bash
python main.py
```

## Exemplo de entrada

```text
Digite linha e coluna: 2 3
```

## Estrutura do projeto

```text
trabalho2-python/
├── main.py
└── README.md
```

## Principais funções

- `criar_mapa_padrao()`: cria o tabuleiro e posiciona bombas fixas
- `contar_bombas_vizinhas(...)`: conta bombas ao redor de uma casa
- `mostrar_mapa(...)`: desenha o mapa no terminal
- `abrir_casa(...)`: abre casa escolhida e aplica regra de vizinhança
- `checar_vitoria(...)`: verifica se o jogador venceu
- `pedir_linha_coluna(...)`: valida a entrada do usuário

## Observações

- O mapa e as bombas estão definidos diretamente no código.
- Não há leitura de arquivo externo.
- O jogo roda totalmente no terminal.
