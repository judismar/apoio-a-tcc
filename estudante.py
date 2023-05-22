class Estudante:
    def __init__(self, nome, matricula):
        self._nome = nome
        self._mat = matricula
        self._cert = [None]*3
        self._contCertificado = 0       

    def registraNota(self, nota):
        if self._contCertificado > 2:
            return
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
