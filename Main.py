import csv
import random as rd
import tkinter as tk

# Carregar as perguntas, respostas e assuntos do arquivo CSV
deck = []
caminhoArquivo = 'DeckDoSaber/perguntasRespostas.csv'

with open(caminhoArquivo, 'r') as file:
    file.readline()  # Ignora o cabeçalho
    my_reader = csv.reader(file, delimiter=';')
    for row in my_reader:
        pergunta, resposta, assunto = row[0:]
        deck.append([pergunta, resposta, assunto])

# Função para atualizar o conteúdo da janela com a nova pergunta e resposta
def mostrar_pergunta(janela, pergunta_label, resposta_label, botao_resposta, assunto_label):
    # Sorteia uma pergunta
    num = rd.randint(0, len(deck) - 1)
    pergunta, resposta, assunto = deck[num]

    # Atualiza o texto da pergunta e do assunto
    pergunta_label.config(text=pergunta)
    resposta_label.config(text="")  # Limpa a resposta anterior
    assunto_label.config(text=f"Assunto: {assunto}")  # Exibe o assunto

    # Função para mostrar a resposta
    def mostrar_resposta():
        resposta_label.config(text=resposta)  # Exibe a resposta
        botao_resposta.config(text="Próxima Pergunta")  # Muda o texto do botão para "Próxima Pergunta"
        botao_resposta.config(command=proxima_pergunta)  # Agora o botão vai para a próxima pergunta

    # Função para avançar para a próxima pergunta
    def proxima_pergunta():
        # Limpa a resposta e configura a próxima pergunta
        botao_resposta.config(text="Mostrar Resposta")
        botao_resposta.config(command=mostrar_resposta)  # Volta a função para mostrar a resposta
        mostrar_pergunta(janela, pergunta_label, resposta_label, botao_resposta, assunto_label)

    # Botão para mostrar a resposta
    botao_resposta.config(state=tk.NORMAL, command=mostrar_resposta)

# Cria a janela inicial
janela = tk.Tk()
janela.title("Pergunta do Baralho")
janela.geometry("400x300")

# Frame para centralizar os elementos
frame = tk.Frame(janela)
frame.pack(expand=True)

# Label para exibir o assunto (no topo)
tamanho_fonte = 14
tamanho_espaco = 1000
assunto_label = tk.Label(frame, text="Assunto: ", font=("Arial", tamanho_fonte), wraplength=tamanho_espaco, justify="left")
assunto_label.pack(pady=5)

# Label para exibir a pergunta (no topo)
pergunta_label = tk.Label(frame, text="", font=("Arial", tamanho_fonte), wraplength=tamanho_espaco, justify="left")
pergunta_label.pack(pady=10)

# Label para exibir a resposta (no centro, inicialmente vazia)
resposta_label = tk.Label(frame, text="", font=("Arial", tamanho_fonte + 2), wraplength=tamanho_espaco, height=10, justify="left")
resposta_label.pack(expand=True)

# Botão para mostrar a resposta ou próxima pergunta (fixado na parte inferior)
botao_resposta = tk.Button(frame, text="Mostrar Resposta", state=tk.DISABLED, width=20, height=2)
botao_resposta.pack(pady=20)  # Fixado na parte inferior

# Dá o foco ao botão ao iniciar
botao_resposta.focus()

# Vincula a tecla Enter para ativar o botão
janela.bind("<Return>", lambda event: botao_resposta.invoke())

# Inicia o processo com a primeira pergunta
mostrar_pergunta(janela, pergunta_label, resposta_label, botao_resposta, assunto_label)

# Exibe a janela
janela.mainloop()
