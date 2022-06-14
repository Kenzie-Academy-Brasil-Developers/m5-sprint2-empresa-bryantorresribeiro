from helper import read_database, save_to_database
from classes.gerente import Gerente

class Empresa():

    @staticmethod
    def format_name(name):
        format = name.title().split()
        return  " ".join(format) 
    
    @staticmethod
    def format_name_dunde(name):
        format = name.lower().split()
        return  "_".join(format) 

    def __init__(self, nome:str, cnpj:str):

        self.nome = self.format_name(nome)
        self.cnpj = cnpj
        self.contratados = []

    def __len__(self):
        return len(self.contratados)
    
    def contratar_funcionario(self, funcionario):

        for funcionarios in self.contratados:
            if funcionarios.get("cpf") == funcionario.cpf:
                return "Funcionário com esse CPF já foi contratado"

        name = self.format_name_dunde(funcionario.nome)
        email = f'{name}@{self.format_name_dunde(self.nome)}.gmail.com'
        empresa = self.nome

        funcionario.empresa = empresa
        funcionario.email = email

        self.contratados.append(vars(funcionario))
        return "Funcionário contratado!"
    
    def gerar_holerite(self, funcionario):

        nome = self.format_name_dunde(funcionario.nome)
        empresa = f"_{self.format_name_dunde(self.nome)}_"

        for funcionarios in self.contratados:
            if funcionarios.get("cpf") == funcionario.cpf:
                save_to_database(vars(funcionario), empresa, nome)
                return True
        
        return False
    
    @staticmethod
    def ler_holerite(empresa, funcionario):

        format_empresa = empresa.nome.lower().split()
        format_funcionario = funcionario.nome.lower().split()
        
        empresa_name = "_".join(format_empresa)
        funcionario_name = "_".join(format_funcionario)

        path = f"empresas/_{empresa_name}_/{funcionario_name}"

        try:

            read = read_database(path)
            return read  

        except:

            return 'Holerite não gerado!'
    
    def remove_funcionario(self, funcionario):

        for gerente in self.contratados:
            
            num = 0

            try:

                while num <= len(gerente.get("funcionarios")[num])-1:
                    
                    if gerente.get("funcionarios")[num].get("cpf") == funcionario.cpf:
                        gerente.get("funcionarios").remove(gerente.get("funcionarios")[num])

                    num +=1

            except:
                ...

    def demissao(self, funcionario):

        for funcionarios in self.contratados:

            if funcionarios.get("cpf") == funcionario.cpf:

                if funcionario.funcao == "Gerente":
                    funcionario.funcionarios.clear()
                    self.contratados.remove(funcionarios)       
                    return "Gerente demitido!"

                else:
                    self.remove_funcionario(funcionario)
                    self.contratados.remove(funcionarios)       
                    return "Funcionario demitido!"
                
        return "Não consta esse CPF na empresa"
    
    def promocao(self, funcionario):

        if funcionario.funcao == "Gerente":
            return False

        for funcionarios in self.contratados:

            if funcionarios.get("cpf") == funcionario.cpf:
                self.demissao(funcionario)
                promo = Gerente(funcionario.nome, funcionario.cpf, funcionario.salario)
                self.contratar_funcionario(promo)
                return promo
        
        return False
