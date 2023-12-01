import turtle

screen = turtle.Screen()
screen.setup(800,800)
screen.title("jogo da velha")
screen.setworldcoordinates(-5,-5,5,5)
screen.tracer(0,0) #pra n exibir cada etapa dos desenhos
#turtle.hideturtle()

def tabuleiro():
    turtle.pencolor('gray')
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
    turtle.goto(x,y-0.80)
    turtle.seth(0)
    turtle.color('red')
    turtle.down()
    turtle.circle(0.80, steps=100)

def des_x(x,y):
    turtle.color('blue')
    turtle.up()
    turtle.goto(x-0.80,y-0.80)
    turtle.down()
    turtle.goto(x+0.80,y+0.80)
    turtle.up()
    turtle.goto(x-0.80,y+0.80)
    turtle.down()
    turtle.goto(x+0.80,y-0.80)
    
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

def play(x, y):
    global turn
    i = 3 - int(y + 5) // 2
    j = int(x + 5) // 2 - 1
    if not (0 <= i < 3 and 0 <= j < 3 and b[i][j] == 0):
        return
    player = 1 if turn == 'x' else 2
    turn = 'o' if turn == 'x' else 'x'
    b[i][j] = player
    desen(b)
    #converte x e y pra o tabuleiro e ve se a posiçao ta valida pra colocar as peça e se a posiçao esta preenchida
    #depois, o jogo se atualiza e chama a funçao desen pra atualizar o novo estado do jogo e as peças n serem posicionadas o msm lugar
b = [ [ 0,0,0 ], [ 0,0,0 ], [ 0,0,0 ] ]    
desen(b)
turn = 'circle'
#o jogo começa na matriz b que representa o tabuleiro vazio, a funcao desen(b) é chamada pra desenhar o  tabuleiro  logo de cara
#o turn é pra controlar quem começa que no caso é o circulo
screen.onclick(play)
turtle.mainloop()