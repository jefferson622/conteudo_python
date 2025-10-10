pergunta1 = float(input("Quanto voce ganha em salario bruto ?: "))
pergunta2 = float(input("Quanto voce ganha em salario por INSS?: "))
pergunta3 = float(input("Quanto voce ganha em salario pelo sindicato?: "))
pergunta4 = float(input("Quanto voce ganha com salario liquido?: "))

imposto_de_renda = 0.11
INSS = 0.08
sindicato = 0.05

resultado1 = ( pergunta1 * 0.24)
print("O quanto voce ganha pelo salario bruto é",resultado1)

resultado2 = (pergunta2 - 0.24)
print("O quanto voce ganha pro INSS é",resultado2)

resultado3 = (pergunta3 + 0.24)
print("O quanto voce ganha pelo sindicato é",resultado3)

resultado4 = (pergunta4 - 0.24)
print("O quanto voce ganha no salario liquido é",resultado4)



