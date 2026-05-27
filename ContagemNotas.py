# sistema de contagem de respostas do ENEM

def Contagem():
    blocoAssunto = { 
        "nome": "", 
        "ano": 0,
        "respostas": { "a": 0, "b": 0, "c": 0, "d": 0, "e": 0 } 
    }

    blocoAssunto["nome"] = input("Bloco de questões do ENEM: ")
    blocoAssunto["ano"] = int(input("Ano de edição do ENEM: "))

    Respostas = input("Liste de respostas, separdas por virgula: ")
    if Respostas == " " or Respostas == "":
        print("Campo vazio. Resgistro invalido. Digite novamente.")
        Respostas = input("Liste os acordes, separdos por virgula: ")

    #Transforma a string em lista
    Respostas = Respostas.lower()
    Respostas = Respostas.replace(" ", "")
    Respostas = Respostas.split(",")

    for x in Respostas:
        if x in blocoAssunto["respostas"]:
            blocoAssunto["respostas"][f"{x}"] += 1
    
    print(f"> Lista complimento das músicas: {len(Respostas)}") 
    return blocoAssunto
    

def VisualizaRegistro(dici):
    print(f"- | {dici["nome"]} | -")
    print("-------------------------\n| Resposta | Quantidade |\n-------------------------")

    for chave, valor in dici["respostas"].items():
        print(f"| {chave} | {valor} |")

    print("-------------------------")

listaRespostas = []
sistema = True

print("---------------------------------\n| Sistema de Contagem de Acorde |\n---------------------------------")
while sistema:
    print("- Tecle 1 para registrar respostas\n- Tecle 2 para visualizar registros\n- Tecle F para finalizar sistema")
    usuario = input("> ")
    match usuario.lower():
        case "1":
            registro = Contagem()
            listaRespostas.append(registro)
            print("Acordes registrados!")
            VisualizaRegistro(registro)
            print(" ")

        case "2":
            for id in range(0, len(listaRespostas)):
                print(f"{id+1} - {listaRespostas[id]["nome"]} : {listaRespostas[id]["ano"]}")
            print("Tecle T para ver todos os registros")

            Resposta = input("Número do Registro: ")
            if Resposta.lower() == "t":
                for reg in listaRespostas:
                    print(" ")
                    VisualizaRegistro(reg)
            else:
                print(" ")
                VisualizaRegistro(listaRespostas[(int(Resposta)-1)])
            print(" ")

        case "f":
            sistema = False
            print("| Sistema de contagem finalizado |")
            print(listaRespostas)

        case _:
            print("Resposta invalida. Tente novamente.")
            print(" ")
