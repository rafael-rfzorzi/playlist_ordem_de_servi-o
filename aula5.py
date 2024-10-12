from tkinter import *
import customtkinter
from Funcionalidades import Functions

window_one = Tk()
class PrimaryWindow(Functions):
    def __init__(self):
        customtkinter.set_appearance_mode("Dark")
        customtkinter.set_default_color_theme("dark-blue")
        self.login_screen()
    def login_screen(self):
        self.window_one = window_one
        self.window_one.title("Login - Glac")
        self.window_one.geometry("700x500+250+150")
        self.window_one.configure(background='#456E96')
        self.window_one.resizable(False, False)

        self.frame_login()

        self.window_one.mainloop()
    def frame_login(self):
        # Label data
        self.descrData2 = customtkinter.CTkFrame(self.window_one)
        self.descrData2.pack(pady=30, padx=30, fill="both", expand=True)

        # Label data
        self.descrData3 = customtkinter.CTkLabel(self.descrData2, text="GlacX", font=("Roboto", 40, "bold"))
        self.descrData3.place(relx=0.25, rely=0.05, relwidth=0.5, relheight=0.1)

        # Label data
        self.descrData3 = customtkinter.CTkLabel(self.descrData2, text="Login", font=("Roboto", 24))
        self.descrData3.place(relx=0.25, rely=0.25, relwidth=0.5, relheight=0.1)

        # Label data
        self.descrData3 = customtkinter.CTkLabel(self.descrData2, text="RfZorzi")
        self.descrData3.place(relx=0.35, rely=0.95, relwidth=0.3, relheight=0.05)

        # entrys
        self.insert_user = customtkinter.CTkEntry(self.descrData2, placeholder_text="Insira o e-mail cadastrado",
                                                  border_color="#2cb67d")
        self.insert_user.place(relx=0.35, rely=0.37, relwidth=0.3, relheight=0.06)
        # entrys
        self.insert_senha = customtkinter.CTkEntry(self.descrData2, placeholder_text="Insira sua senha", show="*",
                                                   border_color="#2cb67d")
        self.insert_senha.place(relx=0.35, rely=0.44, relwidth=0.3, relheight=0.06)

        # Botoes
        self.loginBot = customtkinter.CTkButton(self.descrData2, text='Login',
                                                border_color="#7f5af0",
                                                corner_radius=12, border_width=2, command=self.autentica_login,)
        self.loginBot.place(relx=0.35, rely=0.51, relwidth=0.3, relheight=0.08)

        # Label data
        self.descrData3 = customtkinter.CTkLabel(self.descrData2,
                                                 text="Ainda não é cadastrado? Avalie gratuitamente!! ")
        self.descrData3.place(relx=0.25, rely=0.65, relwidth=0.5, relheight=0.05)

        # Botoes
        self.avaliar = customtkinter.CTkButton(self.descrData2, text='cadastre-se', command=self.tela_cadastro)
        self.avaliar.place(relx=0.35, rely=0.71, relwidth=0.3, relheight=0.06)
        #self.verifica_atualizacao()
    def tela_cadastro(self):
        self.clear_screen_login()
        # Label data
        self.descrData2 = customtkinter.CTkFrame(self.window_one)
        self.descrData2.pack(pady=30, padx=30, fill="both", expand=True)

        # Label data
        self.descrData3 = customtkinter.CTkLabel(self.descrData2, text="GlacX", font=("Roboto", 40, "bold"))
        self.descrData3.place(relx=0.25, rely=0.05, relwidth=0.5, relheight=0.1)

        # Label data
        self.descrData3 = customtkinter.CTkLabel(self.descrData2, text="Login", font=("Roboto", 24))
        self.descrData3.place(relx=0.25, rely=0.25, relwidth=0.5, relheight=0.1)

        # Label data
        self.descrData3 = customtkinter.CTkLabel(self.descrData2, text="RfZorzi")
        self.descrData3.place(relx=0.35, rely=0.95, relwidth=0.3, relheight=0.05)

        # entrys
        self.cadastrese_user = customtkinter.CTkEntry(self.descrData2,
                                                      placeholder_text="Insira um e-mail valido para cadastro")
        self.cadastrese_user.place(relx=0.3, rely=0.37, relwidth=0.4, relheight=0.06)
        self.email = self.cadastrese_user.get()

        # entrys
        self.cadastrese_senha = customtkinter.CTkEntry(self.descrData2,
                                                       placeholder_text="Insira uma senha que ira lembrar", show="*")
        self.cadastrese_senha.place(relx=0.3, rely=0.44, relwidth=0.4, relheight=0.06)
        # Botoes
        self.cadastrese = customtkinter.CTkButton(self.descrData2, text='Submeter')#, command=self.submeter_login)
        self.cadastrese.place(relx=0.35, rely=0.51, relwidth=0.3, relheight=0.07)


PrimaryWindow()