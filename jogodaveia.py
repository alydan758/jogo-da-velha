import turtle

screen = turtle.Screen()
screen.setup(800,800)
screen.title("jogo da velha")
screen.setworldcoordinates(-5,-5,5,5)
#screen.bgcolor('light gray')
screen.tracer(0,0)
#turtle.hideturtle()

def tabuleiro():
    turtle.pencolor('green')
    turtle.pensize(10)
    turtle.up()
    turtle.goto(-3,-1)
    turtle.seth(0)
    turtle.down()
    turtle.fd(6)
    turtle.up()
    turtle.goto(-3,1)
    turtle.seth(0)
    turtle.down()
    turtle.fd(6)
    turtle.up()
    turtle.goto(-1,-3)
    turtle.seth(90)
    turtle.down()
    turtle.fd(6)
    turtle.up()
    turtle.goto(1,-3)
    turtle.seth(90)
    turtle.down()
    turtle.fd(6)

def des_circ(x,y):
    turtle.up()
    turtle.goto(x,y-0.90)
    turtle.seth(0)
    turtle.color('red')
    turtle.down()
    turtle.circle(0.90, steps=100)

def des_x(x,y):
    turtle.color('blue')
    turtle.up()
    turtle.goto(x-0.90,y-0.90)
    turtle.down()
    turtle.goto(x+0.90,y+0.90)
    turtle.up()
    turtle.goto(x-0.90,y+0.90)
    turtle.down()
    turtle.goto(x+0.90,y-0.90)
    
def verif(i,j,p):
    if p==0: return #verifica se o valor de p é 0, a posiçao no tabuleiro ta vazia e n desenha nada
    x,y = 2*(j-1), -2*(i-1) #as coordenadas sao ajustadas para serem usadas dps
    if p==1: #se o quadrado tiver cheio, é a vez do proximo
        des_x(x,y)
    else: #se for o circulo primeiro, é a vex do x
        des_circ(x,y)
    
def desen(b): #desenha o estado atual do tabuleiro, chama a funcao tabuleiro dps chama a funcao verif pra desenhar as peças de cada posiçao
    tabuleiro()
    for _ in range(3):
        for x in range(3):
            verif(_,x,b[_][x]) #chama a funcao verif pra desenhar a peça na posiçao atual da repetiçao, a coluna (_,x,b[_][x]) representa 0, 1 ou 2
    screen.update()

# return 1 if player 1 wins, 2 if player 2 wins, 3 if tie, 0 if game is not over
def gameover(b):
    if b[0][0]>0 and b[0][0] == b[0][1] and b[0][1] == b[0][2]: return b[0][0]
    if b[1][0]>0 and b[1][0] == b[1][1] and b[1][1] == b[1][2]: return b[1][0]
    if b[2][0]>0 and b[2][0] == b[2][1] and b[2][1] == b[2][2]: return b[2][0]
    if b[0][0]>0 and b[0][0] == b[1][0] and b[1][0] == b[2][0]: return b[0][0]
    if b[0][1]>0 and b[0][1] == b[1][1] and b[1][1] == b[2][1]: return b[0][1]
    if b[0][2]>0 and b[0][2] == b[1][2] and b[1][2] == b[2][2]: return b[0][2]
    if b[0][0]>0 and b[0][0] == b[1][1] and b[1][1] == b[2][2]: return b[0][0]
    if b[2][0]>0 and b[2][0] == b[1][1] and b[1][1] == b[0][2]: return b[2][0]
    p = 0
    for i in range(3):
        for j in range(3):
            p += (1 if b[i][j] > 0 else 0)
    if p==9: return 3
    else: return 0
    #verifica se o jogo acabou, 1 se o X ganhar, 2 se o circulo ganhar, 3 pra empate e 0 se o jogo n terminou, 
    # verifica todas as linhas possiveis pra vitoria, colunas, linhas e diagonais
def play(x,y):
    global turn
    i = 3-int(y+5)//2
    j = int(x+5)//2 - 1
    if i>2 or j>2 or i<0 or j<0 or b[i][j]!=0: return
    if turn == 'x': b[i][j], turn = 1, 'o'
    else: b[i][j], turn = 2, 'x'
    desen(b)
    r = gameover(b) #verifica se o jogo acabou a cada peça posicionada
    if r==1:
        screen.textinput("acabou!","X venceu!")
    elif r==2:
        screen.textinput("acabou!","circulo venceu!")
    elif r==3:
        screen.textinput("acabou!", "Tie!")
    #converte x e y pra o tabuleiro e ve se a posiçao ta valida pra colocar as peça e se a posiçao esta preenchida
    #depois, o jogo se atualiza e chama a funçao desen pra atualizar o novo estado do jogo e as peças n serem posicionadas o msm lugar
b = [ [ 0,0,0 ], [ 0,0,0 ], [ 0,0,0 ] ]    
desen(b)
turn = 'circle'#o jogo começa na matriz b que representa o tabuleiro vazio, a funcao desen(b) é chamada pra desenhar o  tabuleiro  logo de cara
#o turn é pra controlar quem começa que no caso é o circulo
screen.onclick(play)
turtle.mainloop()