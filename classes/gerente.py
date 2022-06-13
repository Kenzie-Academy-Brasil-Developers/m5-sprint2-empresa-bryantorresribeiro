from classes.funcionario import Funcionario
from classes.empresa import Empresa

class Gerente(Funcionario):
    
    def __init__(self, nome_completo: str, cpf, salario=8000):
       
        super().__init__(nome_completo, cpf, salario)

        self.funcionarios = []

    def __len__(self):
        
        return len(self.funcionarios)
    
    def adicionar_funcionario(self, funcionario):

        lista = [*Empresa.contratados, *self.funcionarios]
        empresa = ""

        for pessoa in lista:

            if pessoa.get("cpf") == self.cpf:
                empresa = pessoa.empresa
           
            try:
                
                if type(pessoa.funcionarios) == []:
                    return False
            except:
                
                if pessoa.get("empresa") != empresa:
                    return False
        
        self.funcionarios.append(vars(funcionario))
        return True     
    
    def aumento_salarial(self, empresa, funcionario):
        ...
