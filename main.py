
# ============================================
# Sistema de Cadastro e Login no Terminal
# Feito por Daniel Novaes Santos
# ============================================

def senha_curta(senha): # Criação da função que recebe a senha com o parametro nomeado >senha<
    return len(senha) <= 7 # Função que lê a senha e retorna pra uso  se elas estiver maior ou igual a 7
    
def tem_letra(senha): # Criação da função que avalia se a senha tem letra
    for caractere in senha: # For que percorre cada caracter da senha 
        if caractere.isalpha(): # if ultilizando a variavel caractere e o método >str.isalpha()< para ver se a senha tem "espaços"
            return True 
    return False
        
def tem_numero(senha): # Função que verifica se a senha tem numeros
    for numero in senha: # For percorrendo a senha com a variavel numero 
        if numero.isdigit(): # if ultilizando o método >isdigit()< para ver se a senha contem números
            return True
    return False

# ===== TELA DE CADASTRO =====
def tela_de_cadastro(): # Função que imprime um pequeno menu decorativo na tela
    print("=" * 40)
    print("            CADASTRO DE USUÁRIO")
    print("=" * 40)

    usuario = input("Digite seu nome: ") # pede o usuario
        
    while True: # while que pede a senha se ela não se aplicar as metricas ideais
        senha = input(
            "Digite uma senha que contenha no minimo 8 caracteres, numeros e letras: "
                                )

        if senha_curta(senha): # Uso dentro de um if a função <senha_curta()> que se veridica imprime uma mensagem na tela
            print("Erro: senha curta demais.")
            continue

        if not tem_letra(senha): # Uso da função <tem_letra()> para verificar se tem letras na senha e se obter imprimindo uma mensagem na tela
            print("Erro: a senha precisa conter pelo menos uma letra.")
            continue

        if not tem_numero(senha): # Uso da função <tem_numero()> para verificar se tem digitos na senha e se obter imprimindo uma mensagem na tela
            print("Erro: a senha precia conter pelo menos um numero.")
            continue

        print("Senha valida, cadastro concluído.") # imprime na tela caso a senha for preenchia corretamente
        return usuario, senha # retorna os valores de usuario e senha
            
# ===== LOGIN =====
def tela_de_login(usuario_cadastrado, senha_cadastrada): # Função que imprime na tela decorativa pra login
    print("=" * 40)
    print("              LOGIN")
    print("=" * 40)

    tentativas = 0 # Variavel acumuladora de tentativas

    while tentativas < 3: # while loop com a variavel acumuladora com limite que roda até 3 vezes
        usuario = input("Usuario: ")
        senha = input("Senha: ")

        login_correto = (
            usuario == usuario_cadastrado
            and senha == senha_cadastrada
            ) # Variavel que confere se o usuario e a senha são iguais

        if login_correto: # Se a variavel login_correto for True então é imprimida a confirmação de login realizado 
            print("Login realizado com sucesso.")
            return
        else: # Se o usuario ou senha estiverem incorretos o else adiciona mais um valor ao contador e imprime que o usuario ou senha estão incorretos
            tentativas += 1
            print("Usuario ou senha incorretos.")
        
    if tentativas == 3: # if que contem o contador que se chegar a 3 imprime que as tentativas foram excedidas
        print("Tentativas excedidas, acesso bloqueado.")

usuario, senha = tela_de_cadastro()
tela_de_login(usuario, senha)
