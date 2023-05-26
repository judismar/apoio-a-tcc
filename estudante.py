from re import search

class Estudante:
    def __init__(self, nome, matricula):
        if search("^[a-z]*$", nome) == None:
             raise ValueError
              
        self._nome = nome
        if  type(matricula) != int:
              raise ValueError
        else:
             self._mat = 'm' + str(matricula)
             if len(self._mat) != 9:
                raise ErroNumMatricula
        self._cert = [None]*3
        self._contCertificado = 0   
    
    #No máximo 3; senão, dá erro.
    def registraNota(self, nota):
        if self._contCertificado > 2:
            raise ErroQtdCertificados
        if nota < 0 or nota > 10:
            raise ValueError
        self._cert[self._contCertificado] = nota
        self._contCertificado += 1

    def computaMedia(self):
        if self._contCertificado != 3:
            print("Erro. Faltam certificados")
            return 0
        soma = 0
        for nota in self._cert:
            soma += nota
        return soma/3.0

    def printe(self):
        print("Nome:", self._nome)
        print("Matrícula:", self._mat)
        print(self._cert)

class ErroQtdCertificados(OverflowError):
	pass
class ErroNumMatricula(OverflowError):
	pass
