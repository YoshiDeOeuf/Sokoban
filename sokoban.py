import tkinter as tk

WIDTH = 1100
HEIGHT = 1100
BLOCSIZE = 100      # Unite de mesure d'un bloc

# On crée une fenêtre
fenetre = tk.Tk()
fenetre.title('SOKOBAAAAAAAAAAAN')
fenetre.geometry("1100x1100")

canva = tk.Canvas(fenetre, width=WIDTH, height=HEIGHT, bg='#b1d4e0')
canva.pack()

def win():        # Fonction appelee a chaque deplacement, elle verifie si les conditions de victoires sont valides
    if ((canva.coords(oeuf)[0],canva.coords(oeuf)[1]) == (canva.coords(nid)[0],canva.coords(nid)[1]) or (canva.coords(oeuf)[0],canva.coords(oeuf)[1]) == (canva.coords(nid2)[0],canva.coords(nid2)[1])) and ((canva.coords(oeuf2)[0],canva.coords(oeuf2)[1]) == (canva.coords(nid)[0],canva.coords(nid)[1]) or (canva.coords(oeuf2)[0],canva.coords(oeuf2)[1]) == (canva.coords(nid2)[0],canva.coords(nid2)[1])):
        win = tk.Tk()
        win.title('Bien joué !')
        win.geometry("300x50")
        gg = tk.Label(win, text='Félicitations, c\'est gagné !!')
        gg.pack()
        fenetre.destroy()

yoshiPNG = tk.PhotoImage(file='yoshi2D.png')            # Import des images
oeufPNG = tk.PhotoImage(file='yoshioeuf2D.png')
brique = tk.PhotoImage(file='brique.png')
nidPNG = tk.PhotoImage(file='nid.png')

yoshiPNG = yoshiPNG.subsample(4,4)                   # Resize des images pour que ca rentre dans les carres
oeufPNG = oeufPNG.subsample(6,6)
brique = brique.subsample(3,3)
nidPNG = nidPNG.subsample(3,3)

# Creation de la map

for i in range(100, 1000, 100):
    for j in range(100, 1000, 100):
        if i == 100 or j == 100 or i == 900 or j == 900:
            canva.create_image(i+BLOCSIZE/2, j+BLOCSIZE/2, image=brique)

yoshi = canva.create_image(5.5*BLOCSIZE, 5.5*BLOCSIZE, image=yoshiPNG)         # Positionnement des images sur la map
oeuf = canva.create_image(7.5*BLOCSIZE, 6.5*BLOCSIZE, image=oeufPNG)
oeuf2 = canva.create_image(7.5*BLOCSIZE, 4.5*BLOCSIZE, image=oeufPNG)
nid = canva.create_image(2.5*BLOCSIZE, 5.5*BLOCSIZE, image=nidPNG)
nid2 = canva.create_image(4.5*BLOCSIZE, 3.5*BLOCSIZE, image=nidPNG)

canva.tag_lower(nid)       # z index pour les nids
canva.tag_lower(nid2)

def left(event):
    xYoshi = canva.coords(yoshi)[0]
    yYoshi = canva.coords(yoshi)[1]
    xOeuf = canva.coords(oeuf)[0]
    yOeuf = canva.coords(oeuf)[1]
    xOeuf2 = canva.coords(oeuf2)[0]
    yOeuf2 = canva.coords(oeuf2)[1]

    if xYoshi>2.5*BLOCSIZE and (not (xYoshi == xOeuf+BLOCSIZE and yYoshi == yOeuf or yYoshi == yOeuf2 and xYoshi == xOeuf2+BLOCSIZE)):   
        canva.move(yoshi, -BLOCSIZE,0)
    elif xOeuf>2.5*BLOCSIZE and yYoshi == yOeuf and xYoshi == xOeuf+BLOCSIZE and not(xOeuf == xOeuf2+BLOCSIZE and yOeuf == yOeuf2):
        canva.move(oeuf, -BLOCSIZE, 0)
    elif xOeuf2>2.5*BLOCSIZE and yYoshi == yOeuf2 and xYoshi == xOeuf2+BLOCSIZE and not(xOeuf+BLOCSIZE == xOeuf2 and yOeuf == yOeuf2):
        canva.move(oeuf2, -BLOCSIZE, 0)

    win()

def up(event):
    xYoshi = canva.coords(yoshi)[0]
    yYoshi = canva.coords(yoshi)[1]
    xOeuf = canva.coords(oeuf)[0]
    yOeuf = canva.coords(oeuf)[1]
    xOeuf2 = canva.coords(oeuf2)[0]
    yOeuf2 = canva.coords(oeuf2)[1]

    if yYoshi>2.5*BLOCSIZE and (not (yYoshi == yOeuf+BLOCSIZE and xYoshi == xOeuf or xYoshi == xOeuf2 and yYoshi == yOeuf2+BLOCSIZE)):
        canva.move(yoshi,0, -BLOCSIZE)
    elif yOeuf>2.5*BLOCSIZE and xYoshi == xOeuf and yYoshi == yOeuf+BLOCSIZE and not(yOeuf == yOeuf2+BLOCSIZE and xOeuf == xOeuf2):
        canva.move(oeuf, 0, -BLOCSIZE)
    elif yOeuf2>2.5*BLOCSIZE and xYoshi == xOeuf2 and yYoshi == yOeuf2+BLOCSIZE and not(yOeuf+BLOCSIZE == yOeuf2 and xOeuf == xOeuf2):
        canva.move(oeuf2, 0, -BLOCSIZE)

    win()

def right(event):
    xYoshi = canva.coords(yoshi)[0]
    yYoshi = canva.coords(yoshi)[1]
    xOeuf = canva.coords(oeuf)[0]
    yOeuf = canva.coords(oeuf)[1]
    xOeuf2 = canva.coords(oeuf2)[0]
    yOeuf2 = canva.coords(oeuf2)[1]

    if xYoshi<8.5*BLOCSIZE and (not (xYoshi == xOeuf-BLOCSIZE and yYoshi == yOeuf or yYoshi == yOeuf2 and xYoshi == xOeuf2-BLOCSIZE)):   
        canva.move(yoshi,BLOCSIZE,0)
    elif xOeuf<8.5*BLOCSIZE and yYoshi == yOeuf and xYoshi == xOeuf-BLOCSIZE and not(xOeuf == xOeuf2-BLOCSIZE and yOeuf == yOeuf2):
        canva.move(oeuf, BLOCSIZE, 0)
    elif xOeuf2<8.5*BLOCSIZE and yYoshi == yOeuf2 and xYoshi == xOeuf2-BLOCSIZE and not(xOeuf-BLOCSIZE == xOeuf2 and yOeuf == yOeuf2):
        canva.move(oeuf2, BLOCSIZE, 0)

    win()

def down(event):
    xYoshi = canva.coords(yoshi)[0]
    yYoshi = canva.coords(yoshi)[1]
    xOeuf = canva.coords(oeuf)[0]
    yOeuf = canva.coords(oeuf)[1]
    xOeuf2 = canva.coords(oeuf2)[0]
    yOeuf2 = canva.coords(oeuf2)[1]

    if yYoshi<8.5*BLOCSIZE and (not (yYoshi == yOeuf-BLOCSIZE and xYoshi == xOeuf or xYoshi == xOeuf2 and yYoshi == yOeuf2-BLOCSIZE)):
        canva.move(yoshi,0,BLOCSIZE)
    elif yOeuf<8.5*BLOCSIZE and xYoshi == xOeuf and yYoshi == yOeuf-BLOCSIZE and not(yOeuf == yOeuf2-BLOCSIZE and xOeuf == xOeuf2):
        canva.move(oeuf, 0, BLOCSIZE)
    elif yOeuf2<8.5*BLOCSIZE and xYoshi == xOeuf2 and yYoshi == yOeuf2-BLOCSIZE and not(yOeuf-BLOCSIZE == yOeuf2 and xOeuf == xOeuf2):
        canva.move(oeuf2, 0, BLOCSIZE)

    win()

# Bind des fleches du clavier avec les fonctions correspondantes

canva.bind_all('<Right>', right)
canva.bind_all('<Up>', up)
canva.bind_all('<Left>', left)
canva.bind_all('<Down>', down)


fenetre.mainloop()
