turno = input("Digite seu turno (M - Matutino, V - Vespertino, N - Noturno")

turno = turno.upper()

match turno:
    case "M":
        print("Bom dia")
    case "V":
        print("Boa noite")
    case "N":
        print("Bom noite")
    case _:
        print("Valor inválido")
        