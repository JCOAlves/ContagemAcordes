#Função de contagem de acordes em músicas
def Acordes():
    #Dicionario que vai armazenas a contagem
    dici = { "genero": "", "acordes": {} } 

    #Nome do gênero músical que vai ser contado
    GeneroMusical = input("Qual o genêro musical: ")
    dici["genero"] = GeneroMusical

    #Quantidade de contagens
    Vezes = input("Quantidade de registros: ")
    if Vezes == "" or Vezes == " ":
        print("Campo vazio. Resposta invalida. Digite novamente.")
        Vezes = input("Quantidade de registros: ")

    #Lista que vai armazenar a quantidade de acordes em cada música
    lista_complimento = []

    #Loop que vai se repetir o número de Vezes
    for x in range(0, int(Vezes)):
        #Lista de acordes em cada música
        Acordes = input("Liste os acordes, separdos por virgula: ")
        if Acordes == " " or Acordes == "":
            print("Campo vazio. Resgistro invalido. Digite novamente.")
            Acordes = input("Liste os acordes, separdos por virgula: ")

        #Transforma a string em lista
        Acordes = Acordes.replace(" ", "")
        Acordes = Acordes.split(",")

        lista_complimento.append(len(Acordes))

        #Loop que pecorre a lista Acordes
        for acorde in Acordes:
            #Se o acorde não estiver em dici, se cria uma chave do acorde com valor 1
            if not acorde in dici["acordes"]:
                dici["acordes"][acorde] = 1

            #Se o acorde estiver em dici, o valor da chave do acorde é incrementa o valor da chave e 1
            elif acorde in dici["acordes"]:
                dici["acordes"][acorde] = 1 + dici["acordes"][acorde]

    #A função retorna a lista de acordes em cada música e a contagem de acordes
    print(f"> Lista complimento das músicas: {str(lista_complimento)}") 
    return dici

def VisualizaRegistro(dici):
    print(f"- | {dici["genero"]} | -")
    print("-------------------------\n| Nº  Acordes | Acordes |\n-------------------------")

    for chave, valor in dici["acordes"].items():
        print(f"| {chave} | {valor} |")

    print("-------------------------")

lista_acordes = []
sistema = True

print("---------------------------------\n| Sistema de Contagem de Acorde |\n---------------------------------")
while sistema:
    print("- Tecle 1 para registrar acordes\n- Tecle 2 para visualizar registros\n- Tecle F para finalizar sistema")
    usuario = input("> ")
    match usuario.lower():
        case "1":
            registro = Acordes()
            lista_acordes.append(registro)
            print("Acordes registrados!")
            VisualizaRegistro(registro)
            print(" ")

        case "2":
            for id in range(0, len(lista_acordes)):
                print(f"{id+1} - {lista_acordes[id]["genero"]}")
            print("Tecle T para ver todos os registros")

            Resposta = input("Número do Registro: ")
            if Resposta.lower() == "t":
                for reg in lista_acordes:
                    print(" ")
                    VisualizaRegistro(reg)
            else:
                print(" ")
                VisualizaRegistro(lista_acordes[(int(Resposta)-1)])
            print(" ")

        case "f":
            sistema = False
            print("| Sistema de contagem finalizado |")
            print(lista_acordes)

        case _:
            print("Resposta invalida. Tente novamente.")
            print(" ")
