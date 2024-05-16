import pygame
from pygame.locals import QUIT
import keyboard
import random

pygame.display.init()

WIDTH = 600
SQUARES = 3
GAP = 0.8
RECLIM = 6
cross = pygame.transform.scale(pygame.image.load('Cross.png'),(WIDTH//SQUARES*GAP,WIDTH//SQUARES*GAP))
cir = pygame.transform.scale(pygame.image.load('Circle.png'),(WIDTH//SQUARES*GAP,WIDTH//SQUARES*GAP))

class Square:
    def __init__(self, x, y, w) -> None:
        self.x = x
        self.y = y
        self.width, self.height = (w,w)
        self.image = None
        self.color = "green"
        self.rect = pygame.Rect(x,y,w,w)
    

def draw(grid, screen):
    screen.fill("black")
    for i in grid:
        for j in i:
            pygame.draw.rect(screen, j.color, j.rect)
            pygame.draw.line(screen, "black", (j.x,j.y),(j.x+j.width, j.y), (WIDTH//SQUARES)//25)
            pygame.draw.line(screen, "black", (j.x,j.y+j.width),(j.x+j.width, j.y+j.width), (WIDTH//SQUARES)//25)
            pygame.draw.line(screen, "black", (j.x,j.y),(j.x, j.y+j.width), (WIDTH//SQUARES)//25)
            pygame.draw.line(screen, "black", (j.x+j.width,j.y),(j.x+j.width, j.y+j.width), (WIDTH//SQUARES)//25)
            if j.image!=None:
                screen.blit(j.image, (j.x + WIDTH//SQUARES*(1-GAP)//2, j.y + WIDTH//SQUARES*(1-GAP)//2))

def check(grid):
    winline = []
    c1, d1 = [], []
    c2, d2 = [], []
    c=0
    for i, j in enumerate(grid):
        s = [b[i].image for b in grid]
        jmg = [b.image for b in j]
        if (jmg.count(jmg[0])==len(jmg) and jmg[0]!=None):
            return (jmg[0], j)
        if (s.count(s[0])==len(s) and s[0]!=None): 
            return (s[0], [b[i] for b in grid])
        c1.append(j[c].image)
        d1.append(j[c])
        c2.append(j[len(grid)-1-c].image)
        d2.append(j[len(grid)-1-c])
        c+=1
    if (c1.count(c1[0])==len(c1) and c1[0]!=None):
        return (c1[0], d1)
    if (c2.count(c2[0])==len(c2) and c2[0]!=None):
        return (c2[0], d2)
    draw = []
    for i in grid:
        for j in i:
            if (j.image == cir or j.image == cross):
                draw.append(j)
    if len(draw)==len(grid)**2:return ("draw", draw)
    return [False, []]

def poss_moves(grid):
    ls = []
    for i,j in enumerate(grid):
        for a,b in enumerate(j):
            if b.image==None:
                ls.append((i, a))
    return ls


def minimax(grid, rec_lim, turn):
    state = check(grid)[0]
    if state==cir:
        return -1
    if state==cross:
        return 1
    if state=="draw" or rec_lim==0:
        return 0

    scores = []
    for move in poss_moves(grid):
        g = list(grid)
        if g[move[0]][move[1]].image!=None:continue
        g[move[0]][move[1]].image = cir if turn else cross
        try: mm = minimax(g, rec_lim-1, not turn)[0]
        except: mm = minimax(g, rec_lim-1, not turn)
        scores.append((mm, move))
        g[move[0]][move[1]].image = None
    return_ls = []
    scorels= [j[0] for j in scores]
    r = max(scorels) if turn else min(scorels)
    for i in scores:
        if i[0]==r:
            return_ls.append(i)
    return random.choice(return_ls)
        

def main():
    run = True
    
    screen = pygame.display.set_mode((WIDTH, WIDTH))
    pygame.display.set_caption('TIC - TAC - TOE AI')

    grid = []
    for i in range(SQUARES):
        grids = []
        for j in range(SQUARES):
            grids.append(Square(j*WIDTH//SQUARES, i*WIDTH//SQUARES, WIDTH//SQUARES))
        grid.append(grids)

    turn = True
    mouse = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(30)

        if not turn:
            cord = minimax(grid, 9 if SQUARES==3 else RECLIM, True)
            grid[cord[1][0]][cord[1][1]].image = cir
            turn = True


        for event in pygame.event.get():
            if event.type==QUIT or keyboard.is_pressed('q'):
                pygame.quit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()
                    xls = [i for i in range(WIDTH) if i%(WIDTH//SQUARES)==0]
                    xls.append(pos[0])
                    x = sorted(xls).index(pos[0])-1
                    yls = [i for i in range(WIDTH) if i%(WIDTH//SQUARES)==0]
                    yls.append(pos[1])
                    y = sorted(yls).index(pos[1])-1
                    obj = grid[y][x]
                    if obj.image == None:
                        if turn:
                            obj.image = cross
                            turn = False
                        else:
                            obj.image = cir
                            turn = True
                if event.button == 3:
                    mouse = False
        
        
        if check(grid)[0]!=False:
            for i in check(grid)[1]:
                i.color = "blue"
            run = False
        
        if keyboard.is_pressed('r') or not mouse:
            break
        
        draw(grid, screen)

        pygame.display.flip()


def play():
    while True:
        main()
        while True:
            if keyboard.is_pressed('r'):break
            if keyboard.is_pressed('q'):
                pygame.quit()
                quit()
            pygame.display.flip()


if __name__ == "__main__":
    play()