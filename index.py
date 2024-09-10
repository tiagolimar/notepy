import tkinter as tk
from tkinter import filedialog, messagebox


def carregar_arquivo():
    """Função para carregar o conteúdo de um arquivo de texto."""
    caminho_arquivo = filedialog.askopenfilename(
        filetypes=[("Arquivos de Texto", "*.txt"), ("Todos os Arquivos", "*.*")]
    )
    if caminho_arquivo:
        try:
            with open(caminho_arquivo, 'r', encoding='utf-8') as file:
                texto.delete(1.0, tk.END)  # Limpa o conteúdo do widget de texto
                texto.insert(tk.END, file.read())
            app.caminho_arquivo = caminho_arquivo  # Salva o caminho do arquivo para salvar depois
        except Exception as e:
            messagebox.showerror("Erro", f"Não foi possível abrir o arquivo: {e}")


def salvar_arquivo():
    """Função para salvar o conteúdo do editor de texto no arquivo carregado."""
    if hasattr(app, 'caminho_arquivo') and app.caminho_arquivo:
        try:
            with open(app.caminho_arquivo, 'w', encoding='utf-8') as file:
                file.write(texto.get(1.0, tk.END))  # Salva o conteúdo do widget de texto
            messagebox.showinfo("Sucesso", "Arquivo salvo com sucesso.")
        except Exception as e:
            messagebox.showerror("Erro", f"Não foi possível salvar o arquivo: {e}")
    else:
        messagebox.showwarning("Aviso", "Nenhum arquivo carregado para salvar.")


def cancelar():
    """Função para limpar o editor de texto."""
    texto.delete(1.0, tk.END)  # Limpa o conteúdo do widget de texto


# Configuração da janela principal
app = tk.Tk()
app.title("Editor de Texto Simples")
app.geometry("600x400")

# Botão para carregar arquivo
btn_carregar = tk.Button(app, text="Carregar Arquivo", command=carregar_arquivo)
btn_carregar.pack(pady=10)

# Widget de texto para exibição e edição do conteúdo
texto = tk.Text(app, wrap=tk.WORD)
texto.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

# Frame para os botões de Salvar e Cancelar
frame_botoes = tk.Frame(app)
frame_botoes.pack(pady=10)

# Botão de salvar
btn_salvar = tk.Button(frame_botoes, text="Salvar", command=salvar_arquivo)
btn_salvar.grid(row=0, column=0, padx=5)

# Botão de cancelar
btn_cancelar = tk.Button(frame_botoes, text="Cancelar", command=cancelar)
btn_cancelar.grid(row=0, column=1, padx=5)

# Inicia a aplicação
app.mainloop()
