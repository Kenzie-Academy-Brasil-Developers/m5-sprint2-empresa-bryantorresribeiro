from classes.funcionario import Funcionario
import math

class Gerente(Funcionario):

    funcao = "Gerente"
    
    def __init__(self, nome_completo: str, cpf, salario=8000):
       
        super().__init__(nome_completo, cpf, salario)

        self.funcionarios = []

    def __len__(self):
        
        return len(self.funcionarios)
    
    def adicionar_funcionario(self, funcionario):

        if funcionario.funcao == "Gerente":
            return False
        elif funcionario.empresa != self.empresa:
            return False

        for funcionarios in self.funcionarios:

            if funcionarios.get("cpf") == funcionario.cpf:
                return False

        self.funcionarios.append(vars(funcionario))
        return True
    
    def aumento_salarial(self, funcionario, empresa):

        if funcionario.funcao == "Gerente":
            return False
        
        for funcionarios in self.funcionarios:

            if funcionarios.get("cpf") == funcionario.cpf:

                calc = ((10/100) * funcionario.salario)  + funcionario.salario
                funcionario.salario =  math.floor(calc)

                if funcionario.salario > 8000:
                    empresa.demissao(funcionario)
                    promo = Gerente(funcionario.nome, funcionario.cpf, funcionario.salario)
                    empresa.contratar_funcionario(promo)
                    return promo

                return funcionario

        return False
    