from datetime import datetime

class Funcionario():

    funcao = "Funcionário"
    
    @staticmethod
    def format_name(name):
        format = name.title().split()
        return  " ".join(format) 

    def __init__(self, nome_completo:str, cpf, salario=3000):
        self.nome = self.format_name(nome_completo)
        self.cpf = cpf
        self.salario = salario
        self.admissao = datetime.now().strftime("%d/%m/%Y")

    def __str__(self):
       return f' {Funcionario.funcao}: {self.nome}' 