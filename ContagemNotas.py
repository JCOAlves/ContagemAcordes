# sistema de contagem de respostas do ENEM

def Contagem(ano):
    blocoAssunto = { 
        "nome": "", 
        "ano": ano,
        "respostas": { "A": 0, "B": 0, "C": 0, "D": 0, "E": 0 },
        "quantidadeRespostas": 0
    }

    lista = []
    listaNomes = ["Linguagens", "Humanas", "Natureza", "Matematica"]

    for x in listaNomes:
        blocoAssunto["respostas"]["A"] = 0
        blocoAssunto["respostas"]["B"] = 0
        blocoAssunto["respostas"]["C"] = 0
        blocoAssunto["respostas"]["D"] = 0
        blocoAssunto["respostas"]["E"] = 0
        blocoAssunto["quantidadeRespostas"] = 0
        blocoAssunto["nome"] = x
        print(blocoAssunto["nome"])

        Respostas = input("Liste de respostas, separdas por virgula: ")
        if Respostas == " " or Respostas == "":
            print("Campo vazio. Resgistro invalido. Digite novamente.")
            Respostas = input("Liste os acordes, separdos por virgula: ")

        #Transforma a string em lista
        Respostas = Respostas.split(" ")
        
        for z in Respostas:
            if z in blocoAssunto["respostas"]:
                blocoAssunto["respostas"][f"{z}"] += 1
                blocoAssunto["quantidadeRespostas"] += 1
        lista.append(blocoAssunto)
        
        print(f"> Lista complimento das músicas: {blocoAssunto["quantidadeRespostas"]}") 

    return lista
    

listaRespostas = []
sistema = True

print("---------------------------------\n| Sistema de Contagem de Acorde |\n---------------------------------")
while sistema:
    print("- Tecle 1 para registrar respostas\n- Tecle 2 para visualizar registros\n- Tecle F para finalizar sistema")
    usuario = input("> ")
    match usuario.lower():
        case "1":
            ano = int(input("Ano de edição do ENEM: "))
            registro = Contagem(ano)
            listaRespostas.append(registro)

        case "f":
            sistema = False
            print("| Sistema de contagem finalizado |")
            print(listaRespostas)

        case _:
            print("Resposta invalida. Tente novamente.")
            print(" ")

cont = []
