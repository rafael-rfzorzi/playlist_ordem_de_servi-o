from tkinter import messagebox
import re
import gspread

class Functions():
    def clear_screen_login(self):
        try:
            self.descrData2.destroy()
            self.descrData3.destroy()
            self.loginBot.destroy()
            self.insert_user.destroy()
            self.insert_senha.destroy()
        except:
            self.descrData3.destroy()
            self.cadastrese_user.destroy()
            self.cadastrese_senha.destroy()
            self.cadastrese.destroy()

    def check_email_cad(self):
        self.regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if (re.search(self.regex, self.cadastrese_user.get())):
            self.valida_email_cadastro = 'valido'
            print("Valid Email")
        else:
            self.valida_email_cadastro = 'invalido'
            print("Invalid Email")

    def check_senha_cad(self):
        if self.cadastrese_senha.get() == '':
            self.valida_senha_cadastro = 'vazio'
            print("Senha vazia")
        if self.cadastrese_senha.get() == 'Insira uma senha que ira lembrar':
            self.valida_senha_cadastro = 'vazio'
            print("Senha vazia")
        else:
            self.valida_senha_cadastro = 'ocupado'
            pass
    def check_senha_user(self):
        if self.insert_senha.get() == '':
            self.valida_senha_user = 'vazio'
            print("Senha vazia")
        if self.insert_senha.get() == 'Insira sua senha':
            self.valida_senha_user = 'vazio'
            print("Senha vazia")
        else:
            self.valida_senha_user = 'ocupado'
            pass
    def check_email_user(self):
        self.regex2 = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        # Label data
        if (re.search(self.regex2, self.insert_user.get())):
            self.valida_email_usuario = 'valido'
            print("Valid Email")
        else:
            self.valida_email_usuario = 'invalido'
            print("Invalid Email")
    def autentica_login(self):
        self.check_email_user()
        self.notificador()
        self.dados_login()
        self.check_senha_user()
        if self.valida_email_usuario == 'valido':
            try:
                sh = self.gc.open_by_key(self.planilha_login_code)
                ws = sh.worksheet('Página1')
                user = ws.find(self.insert_user.get(), in_column=1)
                self.linha_senha = int(user.row)
                pswd = ws.find(self.insert_senha.get(), in_row=self.linha_senha)
                print(pswd.value)
                mac_address = str(hex(uuid.getnode()))
                celula_serial = str("D" + str(self.linha_senha))
                pc_serial = ws.acell(celula_serial).value
                licenca = str("A" + str(user.row))
                self.licenciado = ws.acell(licenca).value

                if self.valida_senha_user == 'vazio':
                    print('vazio')
                    messagebox.showinfo('Glac', 'Campo senha não pode ficar vazio.')
                else:
                    pass
                ativo_row = int(user.row)
                ativo_user = ws.col_values(3)[int(ativo_row) - 1]
                try:
                    if user.row == pswd.row:
                        if ativo_user == '1111982':
                            if pc_serial == mac_address:
                                print("login validado com sucesso")
                                self.tela()
                                self.window_one.mainloop()
                            else:
                                messagebox.showinfo('Glac',
                                                    'Você não esta utilizando a maquina na qual o sistema foi instalado,'
                                                    ' entre em contato com o suporte.')
                        if ativo_user == '404':
                            messagebox.showinfo('Glac', 'Usuario bloqueado, entre em contato com o suporte.')
                        if ativo_user == '300':
                            messagebox.showinfo('Glac', 'Usuario cadastrado, aguarde até 24 horas para liberação.')

                    else:
                        messagebox.showinfo('Glac', 'Usuario ou senha incorreta.')
                except:
                    messagebox.showerror('Glac', 'Houve um erro ao tentar conectar, consulte o suporte.')
                    print(ValueError)
            except:
                print(ValueError)
                pass
        else:
            messagebox.showinfo('Glac', 'Insira um e-mail valido')
            pass
    def notificador(self):
        self.dados_login()
        try:
            ws = self.gc.open_by_key(self.planilha_login_code).worksheet('Página2')
            self.notifica = ws.col_values(1)
        except google.auth.exceptions.RefreshError:
            messagebox("Glac", "Erro")
    def dados_login(self):
        self.planilha_login_code = ' '
        self.keyjson = {
            "type": "service_account",
            "project_id": "glacx-oficinas",
            "private_key_id": "",
            "private_key": "-----BEGIN PRIVATE KEY-----\,
                           "client_email": "gserviceaccount.com",
        "client_id": "11",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata.iam.gserviceaccount.com",
        "universe_domain": "googleapis.com"}
        self.gc = gspread.service_account_from_dict(self.keyjson)

    def submeter_login(self):
        self.check_email_cad()
        self.check_senha_cad()
        import smtplib
        self.dados_login()
        gc = gspread.service_account_from_dict(self.keyjson)
        try:
            if self.valida_senha_cadastro == 'vazio':
                messagebox.showinfo('Glac', 'Campo senha não pode ficar vazio.')
            if self.valida_email_cadastro == 'valido':
                if self.valida_senha_cadastro == 'vazio':
                    messagebox.showinfo('Glac', 'Campo senha não pode ficar vazio.')
                else:
                    mac_address = str(hex(uuid.getnode()))
                    sh = gc.open_by_key(self.planilha_login_code)
                    ws = sh.worksheet('Página1').append_row(
                        values=[self.cadastrese_user.get(), self.cadastrese_senha.get(), '1111982', mac_address],
                        table_range='A1:D20000')
                    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                    server.login("seuemail@gmail.com", "nyuyiuyihkjhkjh65665wrxvuw")
                    server.sendmail(from_addr="seuemail@gmail.com",
                                    to_addrs="seuemail@rfzorzi.com; outroemail@gmail.com",
                                    msg=self.cadastrese_user.get())

                    server.quit()
                    messagebox.showinfo('Glac', 'E-mail cadastrado, seu acesso foi liberado.')
                    self.cadastrese_user.delete('0', 'end')
                    self.cadastrese_senha.delete('0', 'end')
                    self.cadastrese_user.destroy()
                    self.cadastrese_senha.destroy()
                    self.cadastrese.destroy()
                    self.window_one.quit()
                    self.login_screen()
