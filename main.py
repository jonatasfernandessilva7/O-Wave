import os
from tkinter import *
from tkinter import filedialog
from tkinter import Label
from tkinter import Button
from tkinter import messagebox
from tkinter import ttk
from pydub import AudioSegment

def selecionar_arquivos():
    arquivos = filedialog.askopenfilenames(
        title="Selecione arquivos .ogg",
        filetypes=[("Arquivos OGG", "*.ogg")]
    )
    if arquivos:
        converter_ogg_para_wav(arquivos)

def converter_ogg_para_wav(lista_arquivos):
    pasta_saida = filedialog.askdirectory(title="Selecione a pasta de destino")

    if not pasta_saida:
        messagebox.showwarning("Aviso", "Nenhuma pasta de destino foi selecionada.")
        return

    for caminho in lista_arquivos:
        try:
            audio = AudioSegment.from_ogg(caminho)
            nome_arquivo = os.path.splitext(os.path.basename(caminho))[0] + ".wav"
            caminho_saida = os.path.join(pasta_saida, nome_arquivo)
            audio.export(caminho_saida, format="wav")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao converter {caminho}:\n{e}")
            return

    messagebox.showinfo("Sucesso", "Conversão concluída com sucesso!")

# Interface Gráfica
janela = Tk()
janela.title("Conversor OGG para WAV")
janela.geometry("400x200")

ttk.Label(janela, text="Conversor de Áudio", font=("Arial", 16)).pack(pady=20)
ttk.Button(janela, text="Selecionar arquivos .ogg", command=selecionar_arquivos, width=30).pack(pady=10)
ttk.Button(janela, text="Sair", command=janela.destroy, width=30).pack(pady=10)

janela.mainloop()
