import tkinter as tk

# Cria a janela principal
window = tk.Tk()
window.title("Minha Janela")
window.geometry("700x300")
window.configure(bg="lightblue")

# Função que exibe o texto digitado
def mostrar_texto():
    data = entry.get()
    greeting.config(text=data)

# Campo de entrada de texto
entry = tk.Entry(window, width=50)
entry.pack(pady=20)

# Botão para atualizar o texto
button = tk.Button(window, text="Mostrar texto", command=mostrar_texto)
button.pack(pady=10)

# Label que exibirá o texto
greeting = tk.Label(window, text="", bg="lightblue", font=("Arial", 16))
greeting.pack()

# Inicia o loop da interface
window.mainloop()
