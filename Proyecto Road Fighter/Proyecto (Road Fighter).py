from tkinter import *
import time
import random
import pygame ##El módulo pygame fue utilizado con el único fin de implementar música al juego
"""
Esta parte del juego es sólo el menú de inicio, éste contiene tres opciones para
el jugador que son: 1. iniciar el juego. 2. Ver las instrucciones. 3. Abandonar
el juego.
Además, al presionar el botón "jugar" se abre otra pantalla en la cuál puedo ver
los 5 niveles, cada uno con máximo 1 minuto de juego

"""

def level1():
    """
    [1] = eje y
    [0] = eje x
    """
    global entradaJugador1, w, direccion, m, gasolina
    ventana.geometry("650x500")
    presiono = False
    x = None
    i = 0
    j = 0
    c = Canvas(ventana,width=1500,height=500, bg = "Black")
    c.place(x=0,y=0)
    backGround = PhotoImage(file="carretera finalpre2.png")
    f = c.create_image(270,0,image=backGround)    
    carro1 = PhotoImage(file="carro.png")
    n = c.create_image(273,400,image=carro1)    
    pygame.mixer.music.stop()
    jugadorPantalla1= Label(ventana, text= "JUGADOR 1: \n \n" + entradaJugador1.get(),bg = "black", fg= "white", highlightbackground= "red", font = ("Bodoni MT Black", 11)).place(x=530,y=20)    
    minivan= PhotoImage(file="minivan.png")
    m = c.create_image(random.randint(200,324),0,image=minivan)    
    runner = PhotoImage(file="runner.png")    
    w = c.create_image(random.randint(200,290),-50,image=runner)
    p = c.create_image(random.randint(295,324),-300, image = runner)
   
    fighter = PhotoImage(file="Fighter.png")
    z = c.create_image(random.randint(200,324),-2800,image=fighter)
    gasolina = IntVar()
    gasolina.set(5000)
    velocidad = IntVar()
    gasLbL= Label(ventana,textvariable=gasolina,bg = "black", fg= "white", font = ("Bodoni MT Black", 11)).place(x=555,y=150)
    gasolinaLbl = Label(ventana,text="GASOLINA: \n",bg = "black", fg= "white", font = ("Bodoni MT Black", 10)).place(x=540,y=100) 
    velLbl = Label(ventana,textvariable=velocidad,bg = "black", fg= "white", font = ("Bodoni MT Black", 11)).place(x=555,y=300)
    velocidadLbl = Label(ventana,text="VELOCIDAD: \n",bg = "black", fg= "white", font = ("Bodoni MT Black", 10)).place(x=540,y=250) 
    tda = PhotoImage(file="Tanque de aceite.png")
    TdA = c.create_image(random.randint(200,324),-3000,image=tda)
    mda = PhotoImage(file="Mancha de aceite.png")
    MdA = c.create_image(random.randint(200,324),10,image=mda)
    pygame.mixer.music.load("Car Driving Sound Effect.mp3")
    pygame.mixer.music.play(3)
    
    

    def carroPrincipal(event):

        global x,i,j,u,p
        tecla = repr(event.char)
        
        if(tecla == "'d'" or tecla == "'D'"):
            if(c.coords(n)[0] <= 340):
                c.move(n,26,0)
                c.update()
            else:
                c.move(1,0,0)                          
                
        if(tecla == "'a'" or tecla == "'A'"):
            if(c.coords(n)[0] >= 200):
                c.move(n, -26 ,0)
                c.update()
            else:
                c.move(1,0,0)
               

    def carretera():
        """
        movimiento de la carretera, de la minivan, del runner, fighter y colisiones
        f= fondo
        m = minivan
        w = runner 1
        p = runner 2

        """
        global gasolina
        for i in range(0,100000):            
            colisionCarro1 = c.find_overlapping(c.coords(n)[0]-7,c.coords(n)[1]-30,c.coords(n)[0]+7,c.coords(n)[1]+30)            
            colisionTdA= c.find_overlapping(c.coords(TdA)[0]-7,c.coords(TdA)[1]-30,c.coords(TdA)[0]+7,c.coords(TdA)[1]+30)
            ##Carretera y minivan
            if(c.coords(f)[1] < 27000): 
                c.move(f,0,1.5)
                c.move(m,0,1)
                c.update()
                c.move(w,0,0.5)
                c.move(p,0,0.5)
                c.move(z,0,0.5)
                c.move(TdA,0,1)
                c.move(MdA,0,1.5)
                
            else:
                c.move(f,0,0)
                ganadorLabel = Label(ventana,text="GANASTE",bg = "green", fg= "white", font = ("Elephant", 40)).place(x=100,y=150)
                botonNiveles = Button(ventana, text= "Siguiente >>",command=level2).place(x=350,y=450)
                return False
            if(c.coords(m)[1] > 550):
                c.coords(m,random.randint(200,324),-800)
               
            ##colision, gasolina y mancha

            if(m in colisionCarro1 or w in colisionCarro1 or p in colisionCarro1 or z in colisionCarro1):
                pygame.mixer.music.stop()
                c.move(n,1,0)
                c.move(f,0,1)
                gasolina.set(gasolina.get()-10)
                velocidad.set(velocidad.get()-10)
                                   
            if(TdA in colisionCarro1):
                gasolina.set(gasolina.get()+50)

            if(MdA in colisionCarro1):
                c.move(n,1,0)
                c.move(f,0,1)
                gasolina.set(gasolina.get()-10)
                velocidad.set(velocidad.get()-10)                
                
 
                
            ##Runner

            if(c.coords(w)[0] > 190 and c.coords(w)[0]<290):
                if(c.coords(w)[1] >= 250):                               
                    c.move(w,1,0)
                    c.update()
            if(c.coords(p)[0] > 260 and c.coords(p)[0]<324):
                if(c.coords(p)[1] >= 250):                               
                    c.move(p,-1,0)
                    c.update()

            if(c.coords(w)[1]>600):
                c.coords(w,random.randint(200,290),-3000)
            if(c.coords(p)[1]>600):
                c.coords(p,random.randint(295,324),-1500)

            ##Fighter
            if(c.coords(z)[0]<c.coords(n)[0]):
                c.move(z,0.08,0)
            if(c.coords(z)[0]>c.coords(n)[0]):
                c.move(z,-0.08,0)

            if(c.coords(z)[1]>600):
                c.coords(z,random.randint(295,324),-700)

            ##gasolina
            gasolina.set(gasolina.get()-1)
            

               
                
            if(gasolina.get() <= 0):
                gasolina.set(0)
                gasolinaLbl = Label(ventana,text="PERDISTE",bg = "red", fg= "white", font = ("Elephant", 40)).place(x=100,y=150)
                botonNiveles = Button(ventana, text= "<< Volver",command=jugadores_a).place(x=350,y=450)
                return False
            if(c.coords(TdA)[1]>1000):
                c.coords(TdA,random.randint(295,324),-2000)

            if(velocidad.get() == 100):
                velocidad.set(100)
            else:
                velocidad.set(velocidad.get()+1)

            if(c.coords(MdA)[1]>1000):
                c.coords(MdA,random.randint(295,324),-1500)
                

    c.after(100,carretera)            
    c.bind_all('<Key>',carroPrincipal)
    c.mainloop()
    
def level2():
    global entradaJugador1, w, direccion, m, gasolina
    ventana.geometry("650x500")
    presiono = False
    x = None
    i = 0
    j = 0
    c = Canvas(ventana,width=1500,height=500, bg = "Black")
    c.place(x=0,y=0)
    backGround = PhotoImage(file="carretera finalpre2.png")
    f = c.create_image(270,0,image=backGround)    
    carro1 = PhotoImage(file="carro.png")
    n = c.create_image(273,400,image=carro1)    
    pygame.mixer.music.stop()
    jugadorPantalla1= Label(ventana, text= "JUGADOR 1: \n \n" + entradaJugador1.get(),bg = "black", fg= "white", highlightbackground= "red", font = ("Bodoni MT Black", 11)).place(x=530,y=20)    
    minivan= PhotoImage(file="minivan.png")
    m = c.create_image(random.randint(200,324),0,image=minivan)    
    runner = PhotoImage(file="runner.png")    
    w = c.create_image(random.randint(200,290),-50,image=runner)
    p = c.create_image(random.randint(295,324),-300, image = runner)
    explosion = PhotoImage(file="explosion.png")
    fighter = PhotoImage(file="Fighter.png")
    z = c.create_image(random.randint(200,324),-2800,image=fighter)
    gasolina = IntVar()
    gasolina.set(5000)
    velocidad = IntVar()
    gasLbL= Label(ventana,textvariable=gasolina,bg = "black", fg= "white", font = ("Bodoni MT Black", 11)).place(x=555,y=150)
    gasolinaLbl = Label(ventana,text="GASOLINA: \n",bg = "black", fg= "white", font = ("Bodoni MT Black", 10)).place(x=540,y=100) 
    velLbl = Label(ventana,textvariable=velocidad,bg = "black", fg= "white", font = ("Bodoni MT Black", 11)).place(x=555,y=300)
    velocidadLbl = Label(ventana,text="VELOCIDAD: \n",bg = "black", fg= "white", font = ("Bodoni MT Black", 10)).place(x=540,y=250) 
    tda = PhotoImage(file="Tanque de aceite.png")
    TdA = c.create_image(random.randint(200,324),-3000,image=tda)
    mda = PhotoImage(file="Mancha de aceite.png")
    MdA = c.create_image(random.randint(200,324),10,image=mda)
    pygame.mixer.music.load("Car Driving Sound Effect.mp3")
    pygame.mixer.music.play(3)
    

    def carroPrincipal(event):

        global x,i,j,u,p
        tecla = repr(event.char)
        
        if(tecla == "'d'" or tecla == "'D'"):
            if(c.coords(n)[0] <= 340):
                c.move(n,26,0)
                c.update()
            else:
                c.move(1,0,0)                          
                
        if(tecla == "'a'" or tecla == "'A'"):
            if(c.coords(n)[0] >= 200):
                c.move(n, -26 ,0)
                c.update()
            else:
                c.move(1,0,0)
               

    def carretera():
        """
        movimiento de la carretera, de la minivan, del runner, fighter y colisiones
        f= fondo
        m = minivan
        w = runner 1
        p = runner 2

        """
        global gasolina
        for i in range(0,100000):            
            colisionCarro1 = c.find_overlapping(c.coords(n)[0]-7,c.coords(n)[1]-30,c.coords(n)[0]+7,c.coords(n)[1]+30)            
            colisionTdA= c.find_overlapping(c.coords(TdA)[0]-7,c.coords(TdA)[1]-30,c.coords(TdA)[0]+7,c.coords(TdA)[1]+30)
            ##Carretera y minivan
            if(c.coords(f)[1] < 27000): 
                c.move(f,0,1.5)
                c.move(m,0,1.1)
                c.move(w,0,1)
                c.move(p,0,1)
                c.move(z,0,1)
                c.move(TdA,0,1)
                c.move(MdA,0,1.5)
                c.update()
                
            else:
                c.move(f,0,0)
                ganadorLabel = Label(ventana,text="GANASTE",bg = "green", fg= "white", font = ("Elephant", 40)).place(x=100,y=150)
                botonNiveles = Button(ventana, text= "Siguiente >>",command=level3).place(x=350,y=450)
                return False
            if(c.coords(m)[1] > 550):
                c.coords(m,random.randint(200,324),-800)
               
            ##colision, gasolina y mancha

            if(m in colisionCarro1 or w in colisionCarro1 or p in colisionCarro1 or z in colisionCarro1):
                c.move(n,1,0)
                c.move(f,0,1)
                gasolina.set(gasolina.get()-10)
                velocidad.set(velocidad.get()-10)
                               
            if(TdA in colisionCarro1):
                gasolina.set(gasolina.get()+50)

            if(MdA in colisionCarro1):
                c.move(n,1,0)
                c.move(f,0,1)
                gasolina.set(gasolina.get()-10)
                velocidad.set(velocidad.get()-10)                
                
 
                
            ##Runner

            if(c.coords(w)[0] > 190 and c.coords(w)[0]<290):
                if(c.coords(w)[1] >= 250):                               
                    c.move(w,1,0)
                    c.update()
            if(c.coords(p)[0] > 260 and c.coords(p)[0]<324):
                if(c.coords(p)[1] >= 250):                               
                    c.move(p,-1,0)
                    c.update()

            if(c.coords(w)[1]>600):
                c.coords(w,random.randint(200,290),-3000)
            if(c.coords(p)[1]>600):
                c.coords(p,random.randint(295,324),-1500)

            ##Fighter
            if(c.coords(z)[0]<c.coords(n)[0]):
                c.move(z,0.08,0)
            if(c.coords(z)[0]>c.coords(n)[0]):
                c.move(z,-0.08,0)

            if(c.coords(z)[1]>600):
                c.coords(z,random.randint(295,324),-700)

            ##gasolina
            gasolina.set(gasolina.get()-1)
            

               
                
            if(gasolina.get() <= 0):
                gasolina.set(0)
                gasolinaLbl = Label(ventana,text="PERDISTE",bg = "red", fg= "white", font = ("Elephant", 40)).place(x=100,y=150)
                botonNiveles = Button(ventana, text= "<< Volver",command=jugadores_a).place(x=350,y=450)
                return False
            if(c.coords(TdA)[1]>1000):
                c.coords(TdA,random.randint(295,324),-1000)

            if(velocidad.get() == 100):
                velocidad.set(100)
            else:
                velocidad.set(velocidad.get()+1)

            if(c.coords(MdA)[1]>1000):
                c.coords(MdA,random.randint(295,324),-1500)          

    c.after(100,carretera)            
    c.bind_all('<Key>',carroPrincipal)
    c.mainloop()

def level3():
    global entradaJugador1, w, direccion, m, gasolina
    ventana.geometry("650x500")
    presiono = False
    x = None
    i = 0
    j = 0
    c = Canvas(ventana,width=1500,height=500, bg = "Black")
    c.place(x=0,y=0)
    backGround = PhotoImage(file="carretera finalpre2.png")
    f = c.create_image(270,0,image=backGround)    
    carro1 = PhotoImage(file="carro.png")
    n = c.create_image(273,400,image=carro1)    
    pygame.mixer.music.stop()
    jugadorPantalla1= Label(ventana, text= "JUGADOR 1: \n \n" + entradaJugador1.get(),bg = "black", fg= "white", highlightbackground= "red", font = ("Bodoni MT Black", 11)).place(x=530,y=20)    
    minivan= PhotoImage(file="minivan.png")
    m = c.create_image(random.randint(200,324),0,image=minivan)    
    runner = PhotoImage(file="runner.png")    
    w = c.create_image(random.randint(200,290),-50,image=runner)
    p = c.create_image(random.randint(295,324),-300, image = runner)
    explosion = PhotoImage(file="explosion.png")
    fighter = PhotoImage(file="Fighter.png")
    z = c.create_image(random.randint(200,324),-2800,image=fighter)
    gasolina = IntVar()
    gasolina.set(5000)
    velocidad = IntVar()
    gasLbL= Label(ventana,textvariable=gasolina,bg = "black", fg= "white", font = ("Bodoni MT Black", 11)).place(x=555,y=150)
    gasolinaLbl = Label(ventana,text="GASOLINA: \n",bg = "black", fg= "white", font = ("Bodoni MT Black", 10)).place(x=540,y=100) 
    velLbl = Label(ventana,textvariable=velocidad,bg = "black", fg= "white", font = ("Bodoni MT Black", 11)).place(x=555,y=300)
    velocidadLbl = Label(ventana,text="VELOCIDAD: \n",bg = "black", fg= "white", font = ("Bodoni MT Black", 10)).place(x=540,y=250) 
    tda = PhotoImage(file="Tanque de aceite.png")
    TdA = c.create_image(random.randint(200,324),-3000,image=tda)
    mda = PhotoImage(file="Mancha de aceite.png")
    MdA = c.create_image(random.randint(200,324),10,image=mda)
    pygame.mixer.music.load("Car Driving Sound Effect.mp3")
    pygame.mixer.music.play(3)
    

    def carroPrincipal(event):

        global x,i,j,u,p
        tecla = repr(event.char)
        
        if(tecla == "'d'" or tecla == "'D'"):
            if(c.coords(n)[0] <= 340):
                c.move(n,26,0)
                c.update()
            else:
                c.move(1,0,0)                          
                
        if(tecla == "'a'" or tecla == "'A'"):
            if(c.coords(n)[0] >= 200):
                c.move(n, -26 ,0)
                c.update()
            else:
                c.move(1,0,0)
               

    def carretera():
        """
        movimiento de la carretera, de la minivan, del runner, fighter y colisiones
        f= fondo
        m = minivan
        w = runner 1
        p = runner 2

        """
        global gasolina
        for i in range(0,100000):            
            colisionCarro1 = c.find_overlapping(c.coords(n)[0]-7,c.coords(n)[1]-30,c.coords(n)[0]+7,c.coords(n)[1]+30)            
            colisionTdA= c.find_overlapping(c.coords(TdA)[0]-7,c.coords(TdA)[1]-30,c.coords(TdA)[0]+7,c.coords(TdA)[1]+30)
            ##Carretera y minivan
            if(c.coords(f)[1] < 27000): 
                c.move(f,0,1.5)
                c.move(m,0,1.3)
                c.move(w,0,1.3)
                c.move(p,0,1.3)
                c.move(z,0,1.3)
                c.move(TdA,0,1)
                c.move(MdA,0,1.5)
                c.update()
                
            else:
                c.move(f,0,0)
                ganadorLabel = Label(ventana,text="GANASTE",bg = "green", fg= "white", font = ("Elephant", 40)).place(x=100,y=150)
                botonNiveles = Button(ventana, text= "Siguiente >>",command=level4).place(x=350,y=450)
                return False
            if(c.coords(m)[1] > 550):
                c.coords(m,random.randint(200,324),-800)
               
            ##colision, gasolina y mancha

            if(m in colisionCarro1 or w in colisionCarro1 or p in colisionCarro1 or z in colisionCarro1):
                c.move(n,1,0)
                c.move(f,0,1)
                gasolina.set(gasolina.get()-10)
                velocidad.set(velocidad.get()-10)
                               
            if(TdA in colisionCarro1):
                gasolina.set(gasolina.get()+50)

            if(MdA in colisionCarro1):
                c.move(n,1,0)
                c.move(f,0,1)
                gasolina.set(gasolina.get()-10)
                velocidad.set(velocidad.get()-10)                
                
 
                
            ##Runner

            if(c.coords(w)[0] > 190 and c.coords(w)[0]<290):
                if(c.coords(w)[1] >= 250):                               
                    c.move(w,1,0)
                    c.update()
            if(c.coords(p)[0] > 260 and c.coords(p)[0]<324):
                if(c.coords(p)[1] >= 250):                               
                    c.move(p,-1,0)
                    c.update()

            if(c.coords(w)[1]>600):
                c.coords(w,random.randint(200,290),-3000)
            if(c.coords(p)[1]>600):
                c.coords(p,random.randint(295,324),-1500)

            ##Fighter
            if(c.coords(z)[0]<c.coords(n)[0]):
                c.move(z,0.08,0)
            if(c.coords(z)[0]>c.coords(n)[0]):
                c.move(z,-0.08,0)

            if(c.coords(z)[1]>600):
                c.coords(z,random.randint(295,324),-700)

            ##gasolina
            gasolina.set(gasolina.get()-1)
            

               
                
            if(gasolina.get() <= 0):
                gasolina.set(0)
                gasolinaLbl = Label(ventana,text="PERDISTE",bg = "red", fg= "white", font = ("Elephant", 40)).place(x=100,y=150)
                botonNiveles = Button(ventana, text= "<< Volver",command=jugadores_a).place(x=350,y=450)
                return False
            if(c.coords(TdA)[1]>1000):
                c.coords(TdA,random.randint(295,324),-1000)

            if(velocidad.get() == 100):
                velocidad.set(100)
            else:
                velocidad.set(velocidad.get()+1)

            if(c.coords(MdA)[1]>1000):
                c.coords(MdA,random.randint(295,324),-1500)


    c.after(100,carretera)            
    c.bind_all('<Key>',carroPrincipal)
    c.mainloop()

def level4():
    global entradaJugador1, w, direccion, m, gasolina
    ventana.geometry("650x500")
    presiono = False
    x = None
    i = 0
    j = 0
    c = Canvas(ventana,width=1500,height=500, bg = "Black")
    c.place(x=0,y=0)
    backGround = PhotoImage(file="carretera finalpre2.png")
    f = c.create_image(270,0,image=backGround)    
    carro1 = PhotoImage(file="carro.png")
    n = c.create_image(273,400,image=carro1)    
    pygame.mixer.music.stop()
    jugadorPantalla1= Label(ventana, text= "JUGADOR 1: \n \n" + entradaJugador1.get(),bg = "black", fg= "white", highlightbackground= "red", font = ("Bodoni MT Black", 11)).place(x=530,y=20)    
    minivan= PhotoImage(file="minivan.png")
    m = c.create_image(random.randint(200,324),0,image=minivan)    
    runner = PhotoImage(file="runner.png")    
    w = c.create_image(random.randint(200,290),-50,image=runner)
    p = c.create_image(random.randint(295,324),-300, image = runner)
    explosion = PhotoImage(file="explosion.png")
    fighter = PhotoImage(file="Fighter.png")
    z = c.create_image(random.randint(200,324),-2800,image=fighter)
    gasolina = IntVar()
    gasolina.set(5000)
    velocidad = IntVar()
    gasLbL= Label(ventana,textvariable=gasolina,bg = "black", fg= "white", font = ("Bodoni MT Black", 11)).place(x=555,y=150)
    gasolinaLbl = Label(ventana,text="GASOLINA: \n",bg = "black", fg= "white", font = ("Bodoni MT Black", 10)).place(x=540,y=100) 
    velLbl = Label(ventana,textvariable=velocidad,bg = "black", fg= "white", font = ("Bodoni MT Black", 11)).place(x=555,y=300)
    velocidadLbl = Label(ventana,text="VELOCIDAD: \n",bg = "black", fg= "white", font = ("Bodoni MT Black", 10)).place(x=540,y=250) 
    tda = PhotoImage(file="Tanque de aceite.png")
    TdA = c.create_image(random.randint(200,324),-3000,image=tda)
    mda = PhotoImage(file="Mancha de aceite.png")
    MdA = c.create_image(random.randint(200,324),10,image=mda)
    pygame.mixer.music.load("Car Driving Sound Effect.mp3")
    pygame.mixer.music.play(3)
    

    def carroPrincipal(event):

        global x,i,j,u,p
        tecla = repr(event.char)
        
        if(tecla == "'d'" or tecla == "'D'"):
            if(c.coords(n)[0] <= 340):
                c.move(n,26,0)
                c.update()
            else:
                c.move(1,0,0)                          
                
        if(tecla == "'a'" or tecla == "'A'"):
            if(c.coords(n)[0] >= 200):
                c.move(n, -26 ,0)
                c.update()
            else:
                c.move(1,0,0)
               

    def carretera():
        """
        movimiento de la carretera, de la minivan, del runner, fighter y colisiones
        f= fondo
        m = minivan
        w = runner 1
        p = runner 2

        """
        global gasolina
        for i in range(0,100000):            
            colisionCarro1 = c.find_overlapping(c.coords(n)[0]-7,c.coords(n)[1]-30,c.coords(n)[0]+7,c.coords(n)[1]+30)            
            colisionTdA= c.find_overlapping(c.coords(TdA)[0]-7,c.coords(TdA)[1]-30,c.coords(TdA)[0]+7,c.coords(TdA)[1]+30)
            ##Carretera y minivan
            if(c.coords(f)[1] < 27000): 
                c.move(f,0,1.5)
                c.move(m,0,1.5)
                c.move(w,0,1.5)
                c.move(p,0,1.5)
                c.move(z,0,1.5)
                c.move(TdA,0,1)
                c.move(MdA,0,1.5)
                c.update()
                
            else:
                c.move(f,0,0)
                ganadorLabel = Label(ventana,text="GANASTE",bg = "green", fg= "white", font = ("Elephant", 40)).place(x=100,y=150)
                botonNiveles = Button(ventana, text= "Siguiente >>",command=level5).place(x=350,y=450)
                return False
            if(c.coords(m)[1] > 550):
                c.coords(m,random.randint(200,324),-800)
               
            ##colision, gasolina y mancha

            if(m in colisionCarro1 or w in colisionCarro1 or p in colisionCarro1 or z in colisionCarro1):
                c.move(n,1,0)
                c.move(f,0,1)
                gasolina.set(gasolina.get()-10)
                velocidad.set(velocidad.get()-10)
                               
            if(TdA in colisionCarro1):
                gasolina.set(gasolina.get()+50)

            if(MdA in colisionCarro1):
                c.move(n,1,0)
                c.move(f,0,1)
                gasolina.set(gasolina.get()-10)
                velocidad.set(velocidad.get()-10)                
                
 
                
            ##Runner

            if(c.coords(w)[0] > 190 and c.coords(w)[0]<290):
                if(c.coords(w)[1] >= 250):                               
                    c.move(w,1,0)
                    c.update()
            if(c.coords(p)[0] > 260 and c.coords(p)[0]<324):
                if(c.coords(p)[1] >= 250):                               
                    c.move(p,-1,0)
                    c.update()

            if(c.coords(w)[1]>600):
                c.coords(w,random.randint(200,290),-3000)
            if(c.coords(p)[1]>600):
                c.coords(p,random.randint(295,324),-1500)

            ##Fighter
            if(c.coords(z)[0]<c.coords(n)[0]):
                c.move(z,0.08,0)
            if(c.coords(z)[0]>c.coords(n)[0]):
                c.move(z,-0.08,0)

            if(c.coords(z)[1]>600):
                c.coords(z,random.randint(295,324),-700)

            ##gasolina
            gasolina.set(gasolina.get()-1)
            

               
                
            if(gasolina.get() <= 0):
                gasolina.set(0)
                gasolinaLbl = Label(ventana,text="PERDISTE",bg = "red", fg= "white", font = ("Elephant", 40)).place(x=100,y=150)
                botonNiveles = Button(ventana, text= "<< Volver",command=jugadores_a).place(x=350,y=450)
                return False
                
            if(c.coords(TdA)[1]>1000):
                c.coords(TdA,random.randint(295,324),-1000)

            if(velocidad.get() == 100):
                velocidad.set(100)
            else:
                velocidad.set(velocidad.get()+1)

            if(c.coords(MdA)[1]>1000):
                c.coords(MdA,random.randint(295,324),-1500)
                

    c.after(100,carretera)            
    c.bind_all('<Key>',carroPrincipal)
    c.mainloop()

def level5():
    global entradaJugador1, w, direccion, m, gasolina
    ventana.geometry("650x500")
    presiono = False
    x = None
    i = 0
    j = 0
    c = Canvas(ventana,width=1500,height=500, bg = "Black")
    c.place(x=0,y=0)
    backGround = PhotoImage(file="carretera finalpre2.png")
    f = c.create_image(270,0,image=backGround)    
    carro1 = PhotoImage(file="carro.png")
    n = c.create_image(273,400,image=carro1)    
    pygame.mixer.music.stop()
    jugadorPantalla1= Label(ventana, text= "JUGADOR 1: \n \n" + entradaJugador1.get(),bg = "black", fg= "white", highlightbackground= "red", font = ("Bodoni MT Black", 11)).place(x=530,y=20)    
    minivan= PhotoImage(file="minivan.png")
    m = c.create_image(random.randint(200,324),0,image=minivan)    
    runner = PhotoImage(file="runner.png")    
    w = c.create_image(random.randint(200,290),-50,image=runner)
    p = c.create_image(random.randint(295,324),-300, image = runner)
    explosion = PhotoImage(file="explosion.png")
    fighter = PhotoImage(file="Fighter.png")
    z = c.create_image(random.randint(200,324),-2800,image=fighter)
    gasolina = IntVar()
    gasolina.set(5000)
    velocidad = IntVar()
    gasLbL= Label(ventana,textvariable=gasolina,bg = "black", fg= "white", font = ("Bodoni MT Black", 11)).place(x=555,y=150)
    gasolinaLbl = Label(ventana,text="GASOLINA: \n",bg = "black", fg= "white", font = ("Bodoni MT Black", 10)).place(x=540,y=100) 
    velLbl = Label(ventana,textvariable=velocidad,bg = "black", fg= "white", font = ("Bodoni MT Black", 11)).place(x=555,y=300)
    velocidadLbl = Label(ventana,text="VELOCIDAD: \n",bg = "black", fg= "white", font = ("Bodoni MT Black", 10)).place(x=540,y=250) 
    tda = PhotoImage(file="Tanque de aceite.png")
    TdA = c.create_image(random.randint(200,324),-3000,image=tda)
    mda = PhotoImage(file="Mancha de aceite.png")
    MdA = c.create_image(random.randint(200,324),10,image=mda)
    pygame.mixer.music.load("Car Driving Sound Effect.mp3")
    pygame.mixer.music.play(3)
    

    def carroPrincipal(event):

        global x,i,j,u,p
        tecla = repr(event.char)
        
        if(tecla == "'d'" or tecla == "'D'"):
            if(c.coords(n)[0] <= 340):
                c.move(n,26,0)
                c.update()
            else:
                c.move(1,0,0)                          
                
        if(tecla == "'a'" or tecla == "'A'"):
            if(c.coords(n)[0] >= 200):
                c.move(n, -26 ,0)
                c.update()
            else:
                c.move(1,0,0)
               

    def carretera():
        """
        movimiento de la carretera, de la minivan, del runner, fighter y colisiones
        f= fondo
        m = minivan
        w = runner 1
        p = runner 2

        """
        global gasolina
        for i in range(0,100000):            
            colisionCarro1 = c.find_overlapping(c.coords(n)[0]-7,c.coords(n)[1]-30,c.coords(n)[0]+7,c.coords(n)[1]+30)            
            colisionTdA= c.find_overlapping(c.coords(TdA)[0]-7,c.coords(TdA)[1]-30,c.coords(TdA)[0]+7,c.coords(TdA)[1]+30)
            ##Carretera y minivan
            if(c.coords(f)[1] < 27000): 
                c.move(f,0,1.5)
                c.move(m,0,2)
                c.move(w,0,2)
                c.move(p,0,2)
                c.move(z,0,2)
                c.move(TdA,0,1)
                c.move(MdA,0,1.5)
                c.update()
                
            else:
                c.move(f,0,0)
                ganadorLabel = Label(ventana,text="GAME OVER",bg = "green", fg= "white", font = ("Elephant", 40)).place(x=100,y=150)
                botonNiveles = Button(ventana, text= "<< Volver",command=inicio).place(x=350,y=450)
                return False
            if(c.coords(m)[1] > 550):
                c.coords(m,random.randint(200,324),-800)
               
            ##colision, gasolina y mancha

            if(m in colisionCarro1 or w in colisionCarro1 or p in colisionCarro1 or z in colisionCarro1):
                c.move(n,1,0)
                c.move(f,0,1)
                gasolina.set(gasolina.get()-10)
                velocidad.set(velocidad.get()-10)
                               
            if(TdA in colisionCarro1):
                gasolina.set(gasolina.get()+50)

            if(MdA in colisionCarro1):
                c.move(n,1,0)
                c.move(f,0,1)
                gasolina.set(gasolina.get()-10)
                velocidad.set(velocidad.get()-10)                
                
 
                
            ##Runner

            if(c.coords(w)[0] > 190 and c.coords(w)[0]<290):
                if(c.coords(w)[1] >= 250):                               
                    c.move(w,1,0)
                    c.update()
            if(c.coords(p)[0] > 260 and c.coords(p)[0]<324):
                if(c.coords(p)[1] >= 250):                               
                    c.move(p,-1,0)
                    c.update()

            if(c.coords(w)[1]>600):
                c.coords(w,random.randint(200,290),-3000)
            if(c.coords(p)[1]>600):
                c.coords(p,random.randint(295,324),-1500)

            ##Fighter
            if(c.coords(z)[0]<c.coords(n)[0]):
                c.move(z,0.08,0)
            if(c.coords(z)[0]>c.coords(n)[0]):
                c.move(z,-0.08,0)

            if(c.coords(z)[1]>600):
                c.coords(z,random.randint(295,324),-700)

            ##gasolina
            gasolina.set(gasolina.get()-1)
 
                
            if(gasolina.get() <= 0):
                gasolina.set(0)
                gasolinaLbl = Label(ventana,text="PERDISTE",bg = "red", fg= "white", font = ("Elephant", 40)).place(x=100,y=150)
                botonNiveles = Button(ventana, text= "<< Volver",command=jugadores).place(x=350,y=450)
                return False
            if(c.coords(TdA)[1]>1000):
                c.coords(TdA,random.randint(295,324),-1000)

            if(velocidad.get() == 100):
                velocidad.set(100)
            else:
                velocidad.set(velocidad.get()+1)

            if(c.coords(MdA)[1]>1000):
                c.coords(MdA,random.randint(295,324),-1500)

    c.after(100,carretera)            
    c.bind_all('<Key>',carroPrincipal)
    c.mainloop()  
    
##funcion que me abre una nueva ventana con las instrucciones
def instrucciones():
    ventana1 = Tk()
    ventana1.title("INSTRUCCIONES")
    ventana1.geometry("500x500")
    etiqueta1 = Label(ventana1, text="\n \n \n INSTRUCCIONES: \n \n \n Usar el teclado para mover el automóvil, evitando así otros autos\n y otro tipo de obstáculos. \n \n El primer automóvil se mueve con las teclas a y d \n(Siendo 'a' para moverse hacia la izquierda y 'd' hacia la derecha)\n y el segundo se mueve con las teclas <- y ->.")
    etiqueta1.pack()
    button = Button(ventana1, text="Aceptar",command=ventana1.withdraw).place(x=420,y=450)

## función que me devuelve al menú principal
def inicio():
    
    imagen = PhotoImage(file="fondo1.gif")
    lblImagen = Label(ventana,image=imagen).place(x=0,y=0)
    logotipo = PhotoImage(file="logo.png")
    etiqueta = Label(ventana,image=logotipo).place(x=160,y=100)
    botonJugar = PhotoImage(file="button.png")
    boton = Button(ventana,image=botonJugar,command=jugadores).place(x=50,y=300)
    botonInstrucciones = PhotoImage(file="INSTRUCCIONES.png")
    boton1 = Button(ventana,image=botonInstrucciones,command=instrucciones).place(x=50,y=370)
    botonSalir = PhotoImage(file="ABANDONAR.png")
    boton2 = Button(ventana,image=botonSalir,command=ventana.withdraw).place(x=50,y=425)
    ventana.mainloop()

##Función que me lleva al menú de selección de nivel

def select_lvl():
    global entradaJugador1, entradaJugador2
    
    lvlselectimg = PhotoImage(file="select lvl.gif")
    lblselect = Label(ventana, image=lvlselectimg).place(x=0,y=0)
    btnlvl1 = PhotoImage(file="nivel 1.png")
    imglvl1 = Button(ventana, image=btnlvl1, command = level1).place(x=50, y= 100)
    btnlvl2 = PhotoImage(file="nivel 2.png")
    imglvl2 = Button(ventana, image=btnlvl2, command = level2).place(x=50, y= 180)
    btnlvl3 = PhotoImage(file="nivel 3.png")
    imglvl3 = Button(ventana, image=btnlvl3, command = level3).place(x=50, y= 260)
    btnlvl4 = PhotoImage(file="nivel 4.png")
    imglvl4 = Button(ventana, image=btnlvl4, command = level4).place(x=50, y= 340)
    btnlvl5 = PhotoImage(file="nivel 5.png")
    imglvl5 = Button(ventana, image=btnlvl5, command = level5).place(x=50, y= 420)
    jugadorPantalla1= Label(ventana, text= "JUGADOR 1:  " + entradaJugador1.get(), bg = "black", fg = "white",width=25, font = ("Bodoni MT Black", 11)).place(x=210,y=30)
    buttonBack = Button(ventana, text="<< Atrás",command=inicio).place(x=350,y=450)
    ventana.mainloop()


##función para crear la pantalla de selección de niveles

def jugadores():
    global entradaJugador1, entradaJugador2

    def validacionJugadores():
        if(entradaJugador1.get() != ""):
            select_lvl()
        else:
            return False
        
    ventana.geometry("500x500")
    imagen1 = PhotoImage(file="nombres jugadores.gif")
    lblImagen1 = Label(ventana,image=imagen1).place(x=0,y=0)
    playersNames = PhotoImage(file="jugadores.png")
    lblplayers = Label(ventana,image=playersNames).place(x=50, y= 100)
    imgjugador1 = PhotoImage(file="jugador 1.png")
    lbljugador1 = Label (ventana,image=imgjugador1).place(x=50, y=200)
    buttonBack = Button(ventana, text="<< Atrás",command=inicio).place(x=350,y=450) 
    buttonSelect = Button(ventana, text="Aceptar",command=validacionJugadores).place(x=420,y=450)            
    entradaJugador1=StringVar()
    jugador_1 = Entry (ventana, textvariable=entradaJugador1).place(x=200,y=210)
    ventana.mainloop()

def jugadores_a():
    global entradaJugador1, entradaJugador2

    def validacionJugadores():
        if(entradaJugador1.get() != ""):
            select_lvl()
        else:
            return False
        
    ventana.geometry("500x500")
    imagen1 = PhotoImage(file="nombres jugadores.gif")
    lblImagen1 = Label(ventana,image=imagen1).place(x=0,y=0)
    playersNames = PhotoImage(file="jugadores.png")
    lblplayers = Label(ventana,image=playersNames).place(x=50, y= 100)
    imgjugador1 = PhotoImage(file="jugador 1.png")
    lbljugador1 = Label (ventana,image=imgjugador1).place(x=50, y=200)
    buttonBack = Button(ventana, text="<< Atrás",command=inicio).place(x=350,y=450) 
    buttonSelect = Button(ventana, text="Aceptar",command=validacionJugadores).place(x=420,y=450)            
    entradaJugador1=StringVar()
    jugador_1 = Entry (ventana, textvariable=entradaJugador1).place(x=200,y=210)
    ventana.mainloop()
    pygame.mixer.music.stop()

    
##crear una ventana nueva, darle un nombre y las dimensiones
pygame.init()
ventana = Tk()
ventana.title("ROAD FIGHTER")
ventana.geometry("500x500")
ventana.resizable(0,0)
pygame.mixer.music.load("When the Levee Breaks- Led Zeppelin.mp3")
pygame.mixer.music.play(2)

presiono = False
x = None
i = 0
j = 0
u = 0

##Imagen de la ventana

imagen = PhotoImage(file="fondo1.gif")
lblImagen = Label(ventana,image=imagen).place(x=0,y=0)
##Creo una etiqueta en la ventana creada y la posiciono
logotipo = PhotoImage(file="logo.png")
etiqueta = Label(ventana,image=logotipo).place(x=160,y=100)
##Creo botón "jugar"
botonJugar = PhotoImage(file="button.png")
boton = Button(ventana,image=botonJugar,command=jugadores).place(x=50,y=300)
##creo botón de instrucciones
botonInstrucciones = PhotoImage(file="INSTRUCCIONES.png")
boton1 = Button(ventana,image=botonInstrucciones,command=instrucciones).place(x=50,y=370)
##creo botón "abandonar"
botonSalir = PhotoImage(file="ABANDONAR.png")
boton2 = Button(ventana,image=botonSalir,command=ventana.withdraw).place(x=50,y=425)
ventana.mainloop()
##Gasolina
