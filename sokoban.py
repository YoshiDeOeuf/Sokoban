import tkinter as tk


WIDTH = 1100
HEIGHT = 1100
POPUP_WIDTH = 300
POPUP_HEIGHT = 50
BLOCSIZE = 100    
MARGIN = 100
BACKGROUND_COLOR = '#b1d4e0'

# On cree une fenêtre
fenetre = tk.Tk()
fenetre.title('SOKOBAAAAAAAAAAAN')
fenetre.geometry(str(WIDTH)+'x'+str(HEIGHT))

canva = tk.Canvas(fenetre, width=WIDTH, height=HEIGHT, bg=BACKGROUND_COLOR)
canva.pack()

yoshiPNG = tk.PhotoImage(file='assets/yoshi2D.png')            # Import des images
oeufPNG = tk.PhotoImage(file='assets/yoshioeuf2D.png')
brique = tk.PhotoImage(file='assets/brique.png')
nidPNG = tk.PhotoImage(file='assets/nid.png')

yoshiPNG = yoshiPNG.subsample(4,4)                   # Resize des images
oeufPNG = oeufPNG.subsample(6,6)
brique = brique.subsample(3,3)
nidPNG = nidPNG.subsample(3,3)

def changePosition(pos):
    return pos*BLOCSIZE+3*BLOCSIZE/2


yoshi = canva.create_image(changePosition(4), changePosition(4), image=yoshiPNG)         # Positionnement des images sur la map
oeuf = canva.create_image(changePosition(6), changePosition(5), image=oeufPNG)
oeuf2 = canva.create_image(changePosition(6), changePosition(3), image=oeufPNG)
nid = canva.create_image(changePosition(1), changePosition(4), image=nidPNG)
nid2 = canva.create_image(changePosition(3), changePosition(2), image=nidPNG)

oeufs = []
nids = []
posNids = []

nids.append(nid)
nids.append(nid2)

for nid in nids:
    canva.tag_lower(nid)       # z index pour les nids

def getPosition(item):
    return (canva.coords(item)[0],canva.coords(item)[1])


for nid in nids:
    posNids.append(getPosition(nid))


def checkPositionEquality(item1, item2):
    return getPosition(item1) == getPosition(item2)

def checkWinConditions():        # Fonction appelee a chaque deplacement
    cond = True

    for oeuf in oeufs:
        if getPosition(oeuf) not in posNids:
            cond = False

    if cond:
        win = tk.Tk()
        win.title('Bien joué !')
        win.geometry(str(POPUP_WIDTH)+'x'+str(POPUP_HEIGHT))
        canva.unbind('<Up>', u)
        canva.unbind('<Left>', l)
        canva.unbind('<Right>', r)
        canva.unbind('<Down>', d)
        gg = tk.Label(win, text='Félicitations, c\'est gagné !!')
        gg.pack()

def createMap():
    for i in range(MARGIN, HEIGHT-MARGIN, BLOCSIZE):
        for j in range(MARGIN, WIDTH-MARGIN, BLOCSIZE):
            if i == 100 or j == 100 or i == 900 or j == 900:
                canva.create_image(i+BLOCSIZE/2, j+BLOCSIZE/2, image=brique)
                

def left(event):
    xYoshi = canva.coords(yoshi)[0]
    yYoshi = canva.coords(yoshi)[1]
    xOeuf = canva.coords(oeuf)[0]
    yOeuf = canva.coords(oeuf)[1]
    xOeuf2 = canva.coords(oeuf2)[0]
    yOeuf2 = canva.coords(oeuf2)[1]

    oeufs.append(oeuf)
    oeufs.append(oeuf2)

    if xYoshi>2.5*BLOCSIZE and (not (xYoshi == xOeuf+BLOCSIZE and yYoshi == yOeuf or yYoshi == yOeuf2 and xYoshi == xOeuf2+BLOCSIZE)):   
        canva.move(yoshi, -BLOCSIZE,0)
    elif xOeuf>2.5*BLOCSIZE and yYoshi == yOeuf and xYoshi == xOeuf+BLOCSIZE and not(xOeuf == xOeuf2+BLOCSIZE and yOeuf == yOeuf2):
        canva.move(oeuf, -BLOCSIZE, 0)
    elif xOeuf2>2.5*BLOCSIZE and yYoshi == yOeuf2 and xYoshi == xOeuf2+BLOCSIZE and not(xOeuf+BLOCSIZE == xOeuf2 and yOeuf == yOeuf2):
        canva.move(oeuf2, -BLOCSIZE, 0)

    for pos in posNids:
        print(pos)

    checkWinConditions()


def up(event):
    xYoshi = canva.coords(yoshi)[0]
    yYoshi = canva.coords(yoshi)[1]
    xOeuf = canva.coords(oeuf)[0]
    yOeuf = canva.coords(oeuf)[1]
    xOeuf2 = canva.coords(oeuf2)[0]
    yOeuf2 = canva.coords(oeuf2)[1]

    oeufs.append(oeuf)
    oeufs.append(oeuf2)

    if yYoshi>2.5*BLOCSIZE and (not (yYoshi == yOeuf+BLOCSIZE and xYoshi == xOeuf or xYoshi == xOeuf2 and yYoshi == yOeuf2+BLOCSIZE)):
        canva.move(yoshi,0, -BLOCSIZE)
    elif yOeuf>2.5*BLOCSIZE and xYoshi == xOeuf and yYoshi == yOeuf+BLOCSIZE and not(yOeuf == yOeuf2+BLOCSIZE and xOeuf == xOeuf2):
        canva.move(oeuf, 0, -BLOCSIZE)
    elif yOeuf2>2.5*BLOCSIZE and xYoshi == xOeuf2 and yYoshi == yOeuf2+BLOCSIZE and not(yOeuf+BLOCSIZE == yOeuf2 and xOeuf == xOeuf2):
        canva.move(oeuf2, 0, -BLOCSIZE)

    checkWinConditions()

def right(event):
    xYoshi = canva.coords(yoshi)[0]
    yYoshi = canva.coords(yoshi)[1]
    xOeuf = canva.coords(oeuf)[0]
    yOeuf = canva.coords(oeuf)[1]
    xOeuf2 = canva.coords(oeuf2)[0]
    yOeuf2 = canva.coords(oeuf2)[1]

    oeufs.append(oeuf)
    oeufs.append(oeuf2)

    if xYoshi<8.5*BLOCSIZE and (not (xYoshi == xOeuf-BLOCSIZE and yYoshi == yOeuf or yYoshi == yOeuf2 and xYoshi == xOeuf2-BLOCSIZE)):   
        canva.move(yoshi,BLOCSIZE,0)
    elif xOeuf<8.5*BLOCSIZE and yYoshi == yOeuf and xYoshi == xOeuf-BLOCSIZE and not(xOeuf == xOeuf2-BLOCSIZE and yOeuf == yOeuf2):
        canva.move(oeuf, BLOCSIZE, 0)
    elif xOeuf2<8.5*BLOCSIZE and yYoshi == yOeuf2 and xYoshi == xOeuf2-BLOCSIZE and not(xOeuf-BLOCSIZE == xOeuf2 and yOeuf == yOeuf2):
        canva.move(oeuf2, BLOCSIZE, 0)

    checkWinConditions()

def down(event):
    xYoshi = canva.coords(yoshi)[0]
    yYoshi = canva.coords(yoshi)[1]
    xOeuf = canva.coords(oeuf)[0]
    yOeuf = canva.coords(oeuf)[1]
    xOeuf2 = canva.coords(oeuf2)[0]
    yOeuf2 = canva.coords(oeuf2)[1]

    oeufs.append(oeuf)
    oeufs.append(oeuf2)

    if yYoshi<8.5*BLOCSIZE and (not (yYoshi == yOeuf-BLOCSIZE and xYoshi == xOeuf or xYoshi == xOeuf2 and yYoshi == yOeuf2-BLOCSIZE)):
        canva.move(yoshi,0,BLOCSIZE)
    elif yOeuf<8.5*BLOCSIZE and xYoshi == xOeuf and yYoshi == yOeuf-BLOCSIZE and not(yOeuf == yOeuf2-BLOCSIZE and xOeuf == xOeuf2):
        canva.move(oeuf, 0, BLOCSIZE)
    elif yOeuf2<8.5*BLOCSIZE and xYoshi == xOeuf2 and yYoshi == yOeuf2-BLOCSIZE and not(yOeuf-BLOCSIZE == yOeuf2 and xOeuf == xOeuf2):
        canva.move(oeuf2, 0, BLOCSIZE)

    checkWinConditions()

# Bind des fleches du clavier avec les fonctions correspondantes

r = canva.bind_all('<Right>', right)
u = canva.bind_all('<Up>', up)
l = canva.bind_all('<Left>', left)
d = canva.bind_all('<Down>', down)

createMap()

fenetre.mainloop()
