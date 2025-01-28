import customtkinter

# Configurações iniciais do CustomTkinter
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# Criação da janela principal
janela = customtkinter.CTk()
janela.geometry("500x300")
janela.title("Tela de Login")


# Função chamada ao clicar no botão de login
def clique():
    print("Botão de login clicado!")
    # Aqui você pode adicionar lógica para validar o login


# Elementos da interface
texto = customtkinter.CTkLabel(janela, text="Fazer login", font=("Arial", 20))
email = customtkinter.CTkEntry(janela, placeholder_text="E-mail")
senha = customtkinter.CTkEntry(janela, placeholder_text="Senha", show="*")
botao = customtkinter.CTkButton(janela, text="Login", command=clique)

# Posicionando os elementos na janela
texto.pack(padx=10, pady=10)
email.pack(padx=10, pady=10)
senha.pack(padx=10, pady=10)
botao.pack(padx=10, pady=10)

# Iniciando o loop principal
janela.mainloop()
