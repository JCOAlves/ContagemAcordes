#Script de função de contagem de acordes em músicas
def Acordes():
    dici = {
        "genero": "",
        "acordes": {}
    }

    GeneroMusical = input("Qual o genêro musical: ")
    dici["genero"] = GeneroMusical

    Vezes = input("Quantidade de registros: ")
    if Vezes == "" or Vezes == " ":
        print("Campo vazio. Resposta invalida. Digite novamente.")
        Vezes = input("Quantidade de registros: ")

    for x in range(0, int(Vezes)):
        Acordes = input("Liste os acordes, separdos por virgula: ")
        if Acordes == " " or Acordes == "":
            print("Campo vazio. Resgistro invalido. Digite novamente.")
            Acordes = input("Liste os acordes, separdos por virgula: ")

        Acordes = Acordes.replace(" ", "")
        Acordes = Acordes.split(",")

        for acorde in Acordes:
            if not acorde in dici["acordes"]:
                dici["acordes"][acorde] = 1
            elif acorde in dici["acordes"]:
                dici["acordes"][acorde] = 1 + dici["acordes"][acorde]
            
    return dici

lista_acordes = []
sistema = True

print("---------------------------------\n| Sistema de Contagem de Acorde |\n---------------------------------")
while sistema:
    print("- Tecle 1 para registrar acordes\n- Tecle 2 para visualizar registro\n- Tecle F para finalizar sistema")
    usuario = input("> ")
    match usuario.lower():
        case "1":
            registro = Acordes()
            lista_acordes.append(registro)
            print("Acordes registrados!")
            print(registro)
        case "2":
            print(12)
        case "f":
            sistema = False
            print("| Sistema de contagem finalizado |")
        case _:
            print("Resposta invalida. Tente novamente.")
            
    



'''
def VisualizaRegistro(lista):
    for x in lista:
        print(f"- {x["genero"]}")

    for dicio in lista:
        print(f"| {dicio["genero"]} |")
        for chave, valor in dicio["acordes"].items():
            print(f"| {chave} | {valor} |")

#Acordes()

lista = [
    {
        "genero": "Folk",
        "acordes": {"a":1, "b":2, "c":3}
    }
]
VisualizaRegistro(lista)
'''