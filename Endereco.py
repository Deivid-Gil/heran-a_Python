from Estado import Estado

class Endereco:
    def __init__(self, logradouro, numero, complemento, cep, cidade, estado):
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.cep = cep
        self.cidade = cidade
        self.estado = estado  #instância da classe Estado

    def __str__(self):
        return f"{self.logradouro}, {self.numero}, {self.complemento}, {self.cep}, {self.cidade}, {self.estado}"
