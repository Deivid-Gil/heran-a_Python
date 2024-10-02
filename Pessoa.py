from abc import ABC, abstractmethod
from Endereco import Endereco

class Pessoa(ABC):
    def __init__(self, idade, nome, telefone, email, endereco: Endereco) -> None:
        self.idade = idade
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco  # recebe uma instância de Endereco

    @abstractmethod
    def apresentar(self):
        pass
