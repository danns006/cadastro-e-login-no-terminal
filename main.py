
# ============================================
# Sistema de Cadastro e Login no Terminal
# Feito por Daniel Novaes Santos
# ============================================

def senha_curta(senha):
    return len(senha) <= 7
    
def tem_letra(senha):
    for caractere in senha:
        if caractere.isalpha():
            return True
    return False
        
def tem_numero(senha):
    for numero in senha:
        if numero.isdigit():
            return True
    return False

# ===== TELA DE CADASTRO =====
def tela_de_cadastro():
    print("=" * 40)
    print("            CADASTRO DE USUÁRIO")
    print("=" * 40)

    usuario = input("Digite seu nome: ")
        
    while True:
        senha = input(
            "Digite uma senha que contenha no minimo 8 caracteres, numeros e letras: "
                                )

        if senha_curta(senha):
            print("Erro: senha curta demais.")
            continue

        if not tem_letra(senha):
            print("Erro: a senha precisa conter pelo menos uma letra.")
            continue

        if not tem_numero(senha):
            print("Erro: a senha precia conter pelo menos um numero.")
            continue

        print("Senha valida, cadastro concluído.")
        return usuario, senha
            
# ===== LOGIN =====
def tela_de_login(usuario_cadastrado, senha_cadastrada):
    print("=" * 40)
    print("              LOGIN")
    print("=" * 40)

    tentativas = 0

    while tentativas < 3:
        usuario = input("Usuario: ")
        senha = input("Senha: ")

        login_correto = (
            usuario == usuario_cadastrado
            and senha == senha_cadastrada
            )

        if login_correto:
            print("Login realizado com sucesso.")
            return
        else:
            tentativas += 1
            print("Usuario ou senha incorretos.")
        
    if tentativas == 3:
        print("Tentativas excedidas, acesso bloqueado.")

usuario, senha = tela_de_cadastro()
tela_de_login(usuario, senha)
