from estudante import *

e = Estudante("asa", 42617890)
estiverErrado = True
cont = 0
while cont < 3:
    try:
        e.registraNota(float(input("Informe a nota do próximo certificado: ")))
        cont += 1
    except ValueError:
        print("Erro. Informe um número entre 0 a 10.")
    except ErroQtdCertificados:
        print("Não é possível registrar uma quarta nota.")
        break
    except ErroNumMatricula:
         pass
e.printe()
print(e.computaMedia())
