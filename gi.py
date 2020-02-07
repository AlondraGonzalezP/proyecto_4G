#Aqui se define las bibliotecas que se usaran.
from tkinter import *
from tkinter import messagebox
from time import sleep 
from tkinter import ttk
##Conexion a Base de Datos
#import pymysql
##cursor=conn.cursor()
visual= Tk()

#Se define los datos de nuestra pantalla.
visual.resizable(1,1)
visual.title("Juego de gato")
visual.geometry("900x550")
visual.config(bg="light green")
visual.config(cursor="spraycan")
#Con cual turno daremos comienzo y las posiciones.
str_turno=StringVar()
str_turno.set("Tae")
J1=StringVar()
J1.set("j1")
J2=StringVar()
J2.set("j2")
J3=StringVar()
J3.set("j3")
J4=StringVar()
J4.set("j4")
J5=StringVar()
J5.set("j5")
J6=StringVar()
J6.set("j6")
J7=StringVar()
J7.set("j7")
J8=StringVar()
J8.set("j8")
J9=StringVar()
J9.set("j9")
#Nuestro empate y contadores.
Justempate=StringVar()
Justempate.set("9")
numero=StringVar()
numero.set("1")

GanarJk=StringVar()
GanarJk.set("0")

GanarTT=StringVar()
GanarTT.set("0")
#Imagenes que usaremos.
image3=PhotoImage(file="image31.gif")
Kook=PhotoImage(file="image1.png")
Tae=PhotoImage(file="image2.png")
f=PhotoImage(file="f.png")

def Nuevaventana():
   Ventana2=Tk()
   Ventana2.withdraw()
   visual=Toplevel()
   visual.geometry("550x400")
   visual.config(background="SteelBlue3")

#etiquetas de la nueva ventana 
   eti7=Label(visual,bg="thistle1",text="ID del usuario",font="Helvetica 18 bold",width=10).place(x=20, y=20)
   eti8=Label(visual,bg="thistle1",text="Nombre",font="Helvetica 18 bold",width=9).place(x=20, y=85)
   eti9=Label(visual,bg="thistle1",text="Puntos",font="Helvetica 18 bold",width=9).place(x=20, y=150)
#Cajas de texto de la nueva ventana 
   etiquetaIDusuario=Entry(visual,font="Helvetica 13 bold",width=9).place(x=220, y=25)
   etiquetaNombre=Entry(visual,font="Helvetica 13 bold",width=9).place(x=220, y=90)
   etiquetaPuntos=Entry(visual,font="Helvetica 13 bold",width=9).place(x=220, y=155)

   Ventana2.mainloop()

#Se definen las posibles formas de ganar, dependiendo de nuestras posiciones.
def ganar():
    if (J1.get()==J2.get() and J1.get()==J3.get()):
        if J1.get()=="Kook":
          messagebox.showinfo(message= "Jungkookie", title="Winner")
          GanarJk.set(int(GanarJk.get())+int(numero.get()))
          Jugada()
          WinnerJk()
        elif J1.get()=="Tae":
          messagebox.showinfo(message= "Tae", title="Winner")
          GanarTT.set(int(GanarTT.get())+int(numero.get()))
          Jugada()
          WinnerTT()
    elif (J4.get()==J5.get() and J4.get()==J6.get()):
          if J4.get()=="Kook":
             messagebox.showinfo(message= "Jungkookie", title="Winner")
             GanarJk.set(int(GanarJk.get())+int(numero.get()))
             Jugada()
             WinnerJk()
          elif J4.get()=="Tae":
               messagebox.showinfo(message= "Tae", title="Winner")
               GanarTT.set(int(GanarTT.get())+int(numero.get()))
               Jugada()
               WinnerTT()
    elif (J7.get()==J8.get() and J7.get()==J9.get()):
          if J7.get()=="Kook":
             messagebox.showinfo(message= "Jungkookie", title="Winner")
             GanarJk.set(int(GanarJk.get())+int(numero.get()))
             Jugada()
             WinnerJk()
          elif J7.get()=="Tae":
              messagebox.showinfo(message= "Tae", title="Winner")
              GanarTT.set(int(GanarTT.get())+int(numero.get()))
              Jugada()
              WinnerTT()
    elif (J1.get()==J4.get() and J1.get()==J7.get()):
          if J1.get()=="Kook":
             messagebox.showinfo(message= "Jungkookie", title="Winner")
             GanarJk.set(int(GanarJk.get())+int(numero.get()))
             Jugada()
             WinnerJk()
          elif J1.get()=="Tae":
              messagebox.showinfo(message= "Tae", title="Winner")
              GanarTT.set(int(GanarTT.get())+int(numero.get()))
              Jugada()
              WinnerTT()
    elif (J2.get()==J5.get() and J2.get()==J8.get()):
          if J2.get()=="Kook":
             messagebox.showinfo(message= "Jungkookie", title="Winner")
             GanarJk.set(int(GanarJk.get())+int(numero.get()))
             Jugada()
             WinnerJk()
          elif J2.get()=="Tae":
              messagebox.showinfo(message= "Tae", title="Winner")
              GanarTT.set(int(GanarTT.get())+int(numero.get()))
              Jugada()
              WinnerTT()
    elif (J3.get()==J6.get() and J3.get()==J9.get()):
          if J3.get()=="Kook":
             messagebox.showinfo(message= "Jungkookie", title="Winner")
             GanarJk.set(int(GanarJk.get())+int(numero.get()))
             Jugada()
             WinnerJk()
          elif J3.get()=="Tae":
              messagebox.showinfo(message= "Tae", title="Winner")
              GanarTT.set(int(GanarTT.get())+int(numero.get()))
              Jugada()
              WinnerTT()
    elif (J1.get()==J5.get() and J1.get()==J9.get()):
          if J1.get()=="Kook":
             messagebox.showinfo(message= "Jungkookie", title="Winner")
             GanarJk.set(int(GanarJk.get())+int(numero.get()))
             Jugada()
             WinnerJk()
          elif J1.get()=="Tae":
              messagebox.showinfo(message= "Tae", title="Winner")
              GanarTT.set(int(GanarTT.get())+int(numero.get()))
              Jugada()
              WinnerTT()
    elif (J3.get()==J5.get() and J3.get()==J7.get()):
          if J3.get()=="Kook":
            messagebox.showinfo(message= "Jungkookie", title="Winner")
            GanarJk.set(int(GanarJk.get())+int(numero.get()))
            Jugada()
            WinnerJk()
          elif J3.get()=="Tae":
              messagebox.showinfo(message= "Tae", title="Winner")
              GanarTT.set(int(GanarTT.get())+int(numero.get()))
              Jugada()
              WinnerTT()
    elif Justempate.get()=="0":
        messagebox.showinfo(message="Es un empate", title="Empate :>")
        Jugada()
        WinnerEmpate()
#Se define que sucederá con los botones segun nuestras imagenes, turno y empate.

def posicion1():
    Justempate.set(int(Justempate.get())-int(numero.get()))
    if str_turno.get()=="Kook":
        J1.set("Kook")
        str_turno.set("Tae")
        boton1.config(image=Kook,state=DISABLED)
    else:
        str_turno.set("Kook")
        J1.set("Tae")
        boton1.config(image=Tae,state=DISABLED)
    ganar()

def posicion2():
    Justempate.set(int(Justempate.get())-int(numero.get()))
    if str_turno.get()=="Kook":
        J2.set("Kook")
        str_turno.set("Tae")
        boton2.config(image=Kook,state=DISABLED)
    else:
        str_turno.set("Kook")
        J2.set("Tae")
        boton2.config(image=Tae,state=DISABLED)
    ganar()

def posicion3():
    Justempate.set(int(Justempate.get())-int(numero.get()))
    if str_turno.get()=="Kook":
        J3.set("Kook")
        str_turno.set("Tae")
        boton3.config(image=Kook,state=DISABLED)
    else:
        str_turno.set("Kook")
        J3.set("Tae")
        boton3.config(image=Tae,state=DISABLED)
    ganar()

def posicion4():
    Justempate.set(int(Justempate.get())-int(numero.get()))
    if str_turno.get()=="Kook":
        J4.set("Kook")
        str_turno.set("Tae")
        boton4.config(image=Kook,state=DISABLED)
    else:
        str_turno.set("Kook")
        J4.set("Tae")
        boton4.config(image=Tae,state=DISABLED)
    ganar()

def posicion5():
    Justempate.set(int(Justempate.get())-int(numero.get()))
    if str_turno.get()=="Kook":
        J5.set("Kook")
        str_turno.set("Tae")
        boton5.config(image=Kook,state=DISABLED)
    else:
        str_turno.set("Kook")
        J5.set("Tae")
        boton5.config(image=Tae,state=DISABLED)
    ganar()

def posicion6():
    Justempate.set(int(Justempate.get())-int(numero.get()))
    if str_turno.get()=="Kook":
        J6.set("Kook")
        str_turno.set("Tae")
        boton6.config(image=Kook,state=DISABLED)
    else:
        str_turno.set("Kook")
        J6.set("Tae")
        boton6.config(image=Tae,state=DISABLED)
    ganar()

def posicion7():
    Justempate.set(int(Justempate.get())-int(numero.get()))
    if str_turno.get()=="Kook":
        J7.set("Kook")
        str_turno.set("Tae")
        boton7.config(image=Kook,state=DISABLED)
    else:
        str_turno.set("Kook")
        J7.set("Tae")
        boton7.config(image=Tae,state=DISABLED)
    ganar()

def posicion8():
    Justempate.set(int(Justempate.get())-int(numero.get()))
    if str_turno.get()=="Kook":
        J8.set("Kook")
        str_turno.set("Tae")
        boton8.config(image=Kook,state=DISABLED)
    else:
        str_turno.set("Kook")
        J8.set("Tae")
        boton8.config(image=Tae,state=DISABLED)
    ganar()

def posicion9():
    Justempate.set(int(Justempate.get())-int(numero.get()))
    if str_turno.get()=="Kook":
        J9.set("Kook")
        str_turno.set("Tae")
        boton9.config(image=Kook,state=DISABLED)
    else:
        str_turno.set("Kook")
        J9.set("Tae")
        boton9.config(image=Tae,state=DISABLED)
    ganar()

def nombre1(event):
    combo1.config(state=DISABLED)

def nombre2(event):
    combo2.config(state=DISABLED)
    boton1.config(state=NORMAL)
    boton2.config(state=NORMAL)
    boton3.config(state=NORMAL)
    boton4.config(state=NORMAL)
    boton5.config(state=NORMAL)
    boton6.config(state=NORMAL)
    boton7.config(state=NORMAL)
    boton8.config(state=NORMAL)
    boton9.config(state=NORMAL)

#Se define que despues del gane, el boton se configure a desabilitado y se cambie nuestra imagen de personaje a nuestra imagen base.

def Jugada():
    boton1.config(state=DISABLED,image=image3)
    boton2.config(state=DISABLED,image=image3)
    boton3.config(state=DISABLED,image=image3)
    boton4.config(state=DISABLED,image=image3)
    boton5.config(state=DISABLED,image=image3)
    boton6.config(state=DISABLED,image=image3)
    boton7.config(state=DISABLED,image=image3)
    boton8.config(state=DISABLED,image=image3)
    boton9.config(state=DISABLED,image=image3)
#Se define que la imagen base vuelva a habilitarse y que todo vuelva como a un inicio fue, como nuestro contador a 0.
def Reinicia():
    boton1.config(image=image3,state=NORMAL)
    boton2.config(image=image3,state=NORMAL)
    boton3.config(image=image3,state=NORMAL)
    boton4.config(image=image3,state=NORMAL)
    boton5.config(image=image3,state=NORMAL)
    boton6.config(image=image3,state=NORMAL)
    boton7.config(image=image3,state=NORMAL)
    boton8.config(image=image3,state=NORMAL)
    boton9.config(image=image3,state=NORMAL)
    str_turno.set("Tae")
    GanarTT.set("0")
    GanarJk.set("0")
    J1.set("1")
    J2.set("2")
    J3.set("3")
    J4.set("4")
    J5.set("5")
    J6.set("6")
    J7.set("7")
    J8.set("8")
    J9.set("9")
    Justempate.set("9")
    combo1.config(state=NORMAL)
    combo2.config(state=NORMAL)
    combo1.set("")
    combo2.set("")

#Igual la imagen base vuelve habilitarse y se continua con lo que fue en un incio, sin modificar el contador.    

def Continua():
    boton1.config(image=image3,state=NORMAL)
    boton2.config(image=image3,state=NORMAL)
    boton3.config(image=image3,state=NORMAL)
    boton4.config(image=image3,state=NORMAL)
    boton5.config(image=image3,state=NORMAL)
    boton6.config(image=image3,state=NORMAL)
    boton7.config(image=image3,state=NORMAL)
    boton8.config(image=image3,state=NORMAL)
    boton9.config(image=image3,state=NORMAL)
    str_turno.set("Tae")
    J1.set("1")
    J2.set("2")
    J3.set("3")
    J4.set("4")
    J5.set("5")
    J6.set("6")
    J7.set("7")
    J8.set("8")
    J9.set("9")
    Justempate.set("9")

    
#Se define que cuando gane Jk, se muestren las siguientes imagenes formando un gif, ademas de su duracion.

def WinnerJk():
    vec_gif=[PhotoImage(file="./Kook/0.gif")]
    vec_gif.append(PhotoImage(file="./Kook/1.gif"))
    vec_gif.append(PhotoImage(file="./Kook/2.gif"))
    vec_gif.append(PhotoImage(file="./Kook/3.gif"))
    vec_gif.append(PhotoImage(file="./Kook/4.gif"))
    vec_gif.append(PhotoImage(file="./Kook/5.gif"))
    vec_gif.append(PhotoImage(file="./Kook/6.gif"))
    vec_gif.append(PhotoImage(file="./Kook/7.gif"))
    vec_gif.append(PhotoImage(file="./Kook/8.gif"))
    vec_gif.append(PhotoImage(file="./Kook/9.gif"))
    vec_gif.append(PhotoImage(file="./Kook/10.gif"))
    vec_gif.append(PhotoImage(file="./Kook/11.gif"))
    vec_gif.append(PhotoImage(file="./Kook/12.gif"))
    vec_gif.append(PhotoImage(file="./Kook/13.gif"))
    vec_gif.append(PhotoImage(file="./Kook/14.gif"))
    vec_gif.append(PhotoImage(file="./Kook/15.gif"))
    vec_gif.append(PhotoImage(file="./Kook/16.gif"))
    vec_gif.append(PhotoImage(file="./Kook/17.gif"))
    vec_gif.append(PhotoImage(file="./Kook/18.gif"))
    vec_gif.append(PhotoImage(file="./Kook/19.gif"))
    vec_gif.append(PhotoImage(file="./Kook/20.gif"))
    vec_gif.append(PhotoImage(file="./Kook/21.gif"))
    vec_gif.append(PhotoImage(file="./Kook/22.gif"))
    vec_gif.append(PhotoImage(file="./Kook/23.gif"))
    vec_gif.append(PhotoImage(file="./Kook/24.gif"))
    vec_gif.append(PhotoImage(file="./Kook/25.gif"))
    vec_gif.append(PhotoImage(file="./Kook/26.gif"))
    vec_gif.append(PhotoImage(file="./Kook/27.gif"))
    vec_gif.append(PhotoImage(file="./Kook/28.gif"))
    vec_gif.append(PhotoImage(file="./Kook/29.gif"))
    vec_gif.append(PhotoImage(file="./Kook/30.gif"))
    vec_gif.append(PhotoImage(file="./Kook/31.gif"))
    vec_gif.append(PhotoImage(file="./Kook/32.gif"))
    vec_gif.append(PhotoImage(file="./Kook/33.gif"))
    vec_gif.append(PhotoImage(file="./Kook/34.gif"))
    vec_gif.append(PhotoImage(file="./Kook/35.gif"))
    vec_gif.append(PhotoImage(file="./Kook/36.gif"))
    vec_gif.append(PhotoImage(file="./Kook/37.gif"))
    vec_gif.append(PhotoImage(file="./Kook/38.gif"))
    vec_gif.append(PhotoImage(file="./Kook/39.gif"))
    vec_gif.append(PhotoImage(file="./Kook/40.gif"))
    vec_gif.append(PhotoImage(file="./Kook/41.gif"))
    vec_gif.append(PhotoImage(file="./Kook/42.gif"))
    vec_gif.append(PhotoImage(file="./Kook/43.gif"))
    vec_gif.append(PhotoImage(file="./Kook/44.gif"))

    for i in range(0,44):
        eti.config(image=vec_gif[i])
        visual.update()
        sleep(0.1)
    eti.config(image=f)
    visual.update()
#Se define que cuando gane Tae, se muestren las siguientes imagenes formando un gif, ademas de su duracion.
def WinnerTT():
  vec_gif=[PhotoImage(file="./Tae/tae1.gif")]
  vec_gif.append(PhotoImage(file="./Tae/tae2.gif"))
  vec_gif.append(PhotoImage(file="./Tae/tae3.gif"))
  vec_gif.append(PhotoImage(file="./Tae/tae4.gif"))
  vec_gif.append(PhotoImage(file="./Tae/tae5.gif"))
  vec_gif.append(PhotoImage(file="./Tae/tae6.gif"))
  vec_gif.append(PhotoImage(file="./Tae/tae7.gif"))
  vec_gif.append(PhotoImage(file="./Tae/tae8.gif"))
  vec_gif.append(PhotoImage(file="./Tae/tae9.gif"))
  vec_gif.append(PhotoImage(file="./Tae/tae10.gif"))
  vec_gif.append(PhotoImage(file="./Tae/tae11.gif"))
  vec_gif.append(PhotoImage(file="./Tae/tae12.gif"))
  vec_gif.append(PhotoImage(file="./Tae/tae13.gif"))
  vec_gif.append(PhotoImage(file="./Tae/tae14.gif"))
  vec_gif.append(PhotoImage(file="./Tae/tae15.gif"))
  vec_gif.append(PhotoImage(file="./Tae/tae16.gif"))
  vec_gif.append(PhotoImage(file="./Tae/tae17.gif"))
  vec_gif.append(PhotoImage(file="./Tae/tae18.gif"))
  vec_gif.append(PhotoImage(file="./Tae/tae19.gif"))
  vec_gif.append(PhotoImage(file="./Tae/tae20.gif"))
  vec_gif.append(PhotoImage(file="./Tae/tae21.gif"))
  vec_gif.append(PhotoImage(file="./Tae/tae22.gif"))
  vec_gif.append(PhotoImage(file="./Tae/tae23.gif"))
  vec_gif.append(PhotoImage(file="./Tae/tae24.gif"))
  vec_gif.append(PhotoImage(file="./Tae/tae25.gif"))
  vec_gif.append(PhotoImage(file="./Tae/tae26.gif"))
  vec_gif.append(PhotoImage(file="./Tae/tae27.gif"))
  vec_gif.append(PhotoImage(file="./Tae/tae28.gif"))
  vec_gif.append(PhotoImage(file="./Tae/tae29.gif"))
  vec_gif.append(PhotoImage(file="./Tae/tae30.gif"))
  vec_gif.append(PhotoImage(file="./Tae/tae31.gif"))
  vec_gif.append(PhotoImage(file="./Tae/tae32.gif"))
  vec_gif.append(PhotoImage(file="./Tae/tae33.gif"))
  vec_gif.append(PhotoImage(file="./Tae/tae34.gif"))
  vec_gif.append(PhotoImage(file="./Tae/tae35.gif"))
  vec_gif.append(PhotoImage(file="./Tae/tae36.gif"))
  vec_gif.append(PhotoImage(file="./Tae/tae37.gif"))
  vec_gif.append(PhotoImage(file="./Tae/tae38.gif"))

  for i in range(0,38):
      eti.config(image=vec_gif[i])
      visual.update()
      sleep(0.1)
  eti.config(image=f)
  visual.update()
#Se define que cuando queden empatados, se muestren las siguientes imagenes formando un gif, ademas de su duracion.
def WinnerEmpate():
  vec_gif=[PhotoImage(file="./Taekook/frame-01.gif")]
  vec_gif.append(PhotoImage(file="./Taekook/frame-02.gif"))
  vec_gif.append(PhotoImage(file="./Taekook/frame-03.gif"))
  vec_gif.append(PhotoImage(file="./Taekook/frame-04.gif"))
  vec_gif.append(PhotoImage(file="./Taekook/frame-05.gif"))
  vec_gif.append(PhotoImage(file="./Taekook/frame-06.gif"))
  vec_gif.append(PhotoImage(file="./Taekook/frame-07.gif"))
  vec_gif.append(PhotoImage(file="./Taekook/frame-08.gif"))
  vec_gif.append(PhotoImage(file="./Taekook/frame-09.gif"))
  vec_gif.append(PhotoImage(file="./Taekook/frame-10.gif"))
  vec_gif.append(PhotoImage(file="./Taekook/frame-11.gif"))
  vec_gif.append(PhotoImage(file="./Taekook/frame-12.gif"))
  vec_gif.append(PhotoImage(file="./Taekook/frame-13.gif"))
  vec_gif.append(PhotoImage(file="./Taekook/frame-14.gif"))
  vec_gif.append(PhotoImage(file="./Taekook/frame-15.gif"))
  vec_gif.append(PhotoImage(file="./Taekook/frame-16.gif"))
  vec_gif.append(PhotoImage(file="./Taekook/frame-17.gif"))
  vec_gif.append(PhotoImage(file="./Taekook/frame-18.gif"))
  vec_gif.append(PhotoImage(file="./Taekook/frame-19.gif"))
  vec_gif.append(PhotoImage(file="./Taekook/frame-20.gif"))
  vec_gif.append(PhotoImage(file="./Taekook/frame-21.gif"))
  vec_gif.append(PhotoImage(file="./Taekook/frame-22.gif"))
  vec_gif.append(PhotoImage(file="./Taekook/frame-23.gif"))
  vec_gif.append(PhotoImage(file="./Taekook/frame-24.gif"))
  vec_gif.append(PhotoImage(file="./Taekook/frame-25.gif"))

  for i in range(0,25):
      eti.config(image=vec_gif[i])
      visual.update()
      sleep(.1)
  eti.config(image=f)
  visual.update()


#Se forman y personalizan los botones, su posicion, donde estarán y su funcion.

boton1=Button(visual,command=posicion1,bg="black",image=image3,textvariable=J1,state=DISABLED)
boton1.place(x=20, y=20)
boton2=Button(visual,command=posicion2,bg="black",image=image3,textvariable=J2,state=DISABLED)
boton2.place(x=180, y=20)
boton3=Button(visual,command=posicion3,bg="black",image=image3,textvariable=J3,state=DISABLED)
boton3.place(x=340, y=20)
boton4=Button(visual,command=posicion4,bg="black",image=image3,textvariable=J4,state=DISABLED)
boton4.place(x=20, y=180)
boton5=Button(visual,command=posicion5,bg="black",image=image3,textvariable=J5,state=DISABLED)
boton5.place(x=180, y=180)
boton6=Button(visual,command=posicion6,bg="black",image=image3,textvariable=J6,state=DISABLED)
boton6.place(x=340, y=180)
boton7=Button(visual,command=posicion7,bg="black",image=image3,textvariable=J7,state=DISABLED)
boton7.place(x=20, y=340)
boton8=Button(visual,command=posicion8,bg="black",image=image3,textvariable=J8,state=DISABLED)
boton8.place(x=180, y=340)
boton9=Button(visual,command=posicion9,bg="black",image=image3,textvariable=J9,state=DISABLED)
boton9.place(x=340, y=340)
#Se agregan las etiquetas y los botones para continuar y reiniciar 
eti1=Label(visual,text="Sigue:",bg="steel blue",font="Helvetica 18 bold")
eti1.place(x=520,y=20)
eti2=Label(visual,bg="steel blue",font="Helvetica 18 bold",width=6,textvariable=str_turno)
eti2.place(x=520,y=65)
eti5=Label(visual,bg="steel blue",text="0",font="Helvetica 18 bold",width=6,textvariable=GanarTT)
eti5.place(x=650,y=135)
eti6=Label(visual,bg="steel blue",text="0",font="Helvetica 18 bold",width=6,textvariable=GanarJk)
eti6.place(x=650,y=195)
b10=Button(visual,bg="pink",font="Helvetica 18 bold",text="Continua",command=Continua)
b10.place(x=520, y=250)
b11=Button(visual,bg="pink",font="Helvetica 18 bold",text="Reinicia",command=Reinicia)
b11.place(x=520, y=340)
b12=Button(visual,bg="pink",font="Helvetica 18 bold",text="Editar",command=Nuevaventana)
b12.place(x=670, y=250)
## Nombre del primer usuario
#def nombre1(event):
 #combo1.config(state=DISABLED)
## Nombre del segundo usuario
#def nombre2(event):
 #combo2.config(state=DISABLED)

##-------------------------- Procedimiento Principal------------------------------------------------
## Combo de Usuarios
#cursor.execute('select Nom_usuario from usuarios')
#lista=[]
#combo1=ttk.Combobox(visual, font='Helvetica 12 bold', width=10)
#combo1.place(x=520, y = 135)
#combo2=ttk.Combobox(visual, font='Helvetica 12 bold', width=10)
#combo2.place(x=520, y = 195)
#for row in cursor:
 #lista.append(row)
#cursor.close()
#conn.close()
#combo1['values']=lista
#combo2['values']=lista
#combo1.bind("<<ComboboxSelected>>",nombre1)
#combo2.bind("<<ComboboxSelected>>",nombre2)


eti=Label(visual,image=f)
eti.place(x=1,y=1)

visual.mainloop()
