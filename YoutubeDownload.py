import os
from tkinter import *
from tkinter import messagebox
from pytube import YouTube, exceptions


app = Tk()  # Inicia o programa
app.title("Youtube Downloader")  # Título do programa.
app.geometry("600x400")  # Dimensão do programa.

# app.configure(background="#334")  # Configurações de cor.


# <------------------- Criando os componentes do programa.------------------->

# LOGO
lblLogo = Label(app, text="Youtube Downloader",
                background="red", foreground="white", font="Arial")
lblLogo.pack(fill=X)


# Pega a URL
lblUrl = Label(app, text="Insira o link:", font="Arial")
lblUrl.place(x=10, y=80, width=150, height=30)

url = Entry(app)
url.place(x=170, y=80, width=400, height=30)
url.focus()


# Escolha do formato (Vídeo ou Áudio)
lblFormat = Label(app, text="Formato: ", font="Arial")
lblFormat.pack(fill=X, expand=TRUE)
lblFormat.place(
    x=10, y=120, width=150, height=50)

listaFormato = ["Vídeo", "Áudio"]
varFormato = StringVar()
varFormato.set(listaFormato[0])

opMenu = OptionMenu(app, varFormato, *listaFormato)
opMenu.pack(fill=X, expand=TRUE)
opMenu.place(x=170, y=120, width=150,  height=50)


# < ------------------ Função ao clicar em "BAIXAR" -------------------------->


def baixar():
    varForm = varFormato.get()  # Associando variável à escolha.
    link = url.get()  # Associando variável à URL

    try:
        yt = YouTube(link)  # Associando variável à url

    except exceptions.RegexMatchError:
        # Tratamente de erro do link
        messagebox.showerror(title="ERRO DE LINK!",
                             message="Verifique o link e tente novamente!").center()
    except exceptions.VideoUnavailable:
        messagebox.showerror(title="LINK INACESSÍVEL!",
                             message="Verifique o link e tente novamente!").center()

    else:
        if varForm == listaFormato[0]:  # Vídeo
            ys = yt.streams.get_highest_resolution()
            ys.download()

        else:  # Áudio
            ys = yt.streams.get_audio_only()
            ys.download()

        msg = f"O arquivo foi salvo em: {os.getcwd()}"

        messagebox.showinfo(title="Download Concluído!", message=msg)


# < ------------------------------------------------------------------>
Button(app, text="Baixar Arquivo", font="Arial",  activebackground="#c4302b", activeforeground="white", background="#333", foreground="white", borderwidth=8,  command=baixar).place(
    x=200, y=250, width=200, height=50)


app.mainloop()
