#Script de função de contagem de acordes em músicas
def Acordes():
    dici = { "genero": "", "acordes": {} }

    GeneroMusical = input("Qual o genêro musical: ")
    dici["genero"] = GeneroMusical

    Vezes = input("Quantidade de registros: ")
    if Vezes == "" or Vezes == " ":
        print("Campo vazio. Resposta invalida. Digite novamente.")
        Vezes = input("Quantidade de registros: ")

    lista_complimento = []

    for x in range(0, int(Vezes)):
        Acordes = input("Liste os acordes, separdos por virgula: ")
        if Acordes == " " or Acordes == "":
            print("Campo vazio. Resgistro invalido. Digite novamente.")
            Acordes = input("Liste os acordes, separdos por virgula: ")

        Acordes = Acordes.replace(" ", "")
        Acordes = Acordes.split(",")

        lista_complimento.append(len(Acordes))

        for acorde in Acordes:
            if not acorde in dici["acordes"]:
                dici["acordes"][acorde] = 1
            elif acorde in dici["acordes"]:
                dici["acordes"][acorde] = 1 + dici["acordes"][acorde]

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
