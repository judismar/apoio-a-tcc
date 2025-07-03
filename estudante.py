class Estudante:
    def __init__(self, nome, matricula):
        if type(nome) != str:
             raise NomeInvalido 
              
        self._nome = nome
        if  type(matricula) != int:
              raise MatriculaInvalida
        else:
             self._mat = 'm' + str(matricula)
             if len(self._mat) != 9:
                raise MatriculaInvalida
        self._cert = [None]*3
        self._contCertificado = 0   
    
    #No máximo 3; senão, dá erro.
    def registraNota(self, nota):
        if self._contCertificado > 2:
            raise ErroQtdCertificados
        if nota < 0 or nota > 10:
            raise NotaInvalida
        self._cert[self._contCertificado] = nota
        self._contCertificado += 1

    def computaMedia(self):
        if self._contCertificado != 3:
            raise ErroQtdCertificados
        soma = 0
        for nota in self._cert:
            soma += nota
        return soma/3.0

    def printe(self):
        print("Nome:", self._nome)
        print("Matrícula:", self._mat)
        print(self._cert)

class ErroDeEstudante(Exception):
    pass

class ErroQtdCertificados(ErroDeEstudante):
	pass
class MatriculaInvalida(ErroDeEstudante):
	pass
class NomeInvalido(ErroDeEstudante):
	pass
class NotaInvalida(ErroDeEstudante):
	pass
