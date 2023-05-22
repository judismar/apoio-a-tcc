from estudante import Estudante

e = Estudante("!2376427", 213455)
estiverErrado = True
cont = 0
while cont < 5:
    try:
        e.registraNota(int(input("\
        Informe a nota do próximo certificado: ")))
        cont += 1
    except ValueError:
        print("Erro. Informe um número entre 0 a 10.")
e.printe()
print(e.computaMedia())
