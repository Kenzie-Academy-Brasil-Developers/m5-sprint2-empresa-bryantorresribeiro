from helper import read_database, save_to_database
#from models.gerente import Gerente

class Empresa():

    @staticmethod
    def format_name(name):
        format = name.title().split()
        return  " ".join(format) 
    
    @staticmethod
    def format_name_dunde(name):
        format = name.lower().split()
        return  "_".join(format) 
    
    contratados = []

    def __init__(self, nome:str, cnpj:str):
        self.nome = self.format_name(nome)
        self.cnpj = cnpj

    def __len__(self):
        return len(Empresa.contratados)
    
    def contratar_funcionario(self, funcionario):

        for funcionarios in Empresa.contratados:
            if funcionarios.get("cpf") == funcionario.cpf:
                return "Funcionário com esse CPF já foi contratado"

        name = self.format_name_dunde(funcionario.nome)
        email = f'{name}@{self.nome.lower()}.gmail.com'
        empresa = self.nome

        Empresa.contratados.append(({**vars(funcionario), "email":email, "empresa":empresa}))
    
    def gerar_holerite(self, cadastrar_usuario):

        nome = self.format_name_dunde(cadastrar_usuario.nome)
        empresa = f"_{self.format_name_dunde(self.nome)}_"

        for funcionarios in Empresa.contratados:
            if funcionarios.get("cpf") == cadastrar_usuario.cpf:
                save_to_database(vars(cadastrar_usuario), empresa, nome)
                return True
        
        return False
    
    @staticmethod
    def ler_holerite(empresa, funcionario):

        format_empresa = empresa.nome.lower().split()
        format_funcionario = funcionario.nome.lower().split()
        
        empresa_name = "_".join(format_empresa)
        funcionario_name = "_".join(format_funcionario)
        path = f"_{empresa_name}_/{funcionario_name}"

        try:

            read = read_database(path)
            return read  

        except:

            return 'Holerite não gerado!'
    
    def demissao(self, empregado):

        for user in Empresa.contratados:

            if user.get("cpf") == empregado.cpf:

                try:

                    if type(user.get("funcionarios") == []):
                        user.get("funcionarios").clear()
                        Empresa.contratados.remove(user)       
                        return "Gerente demitido!"

                except:
                    
                    Empresa.contratados.remove(user)       
                    return "Funcionario demitido!"  
                
        return "Não consta esse CPF na empresa"
    
""" def promocao(self, funcionario):

        for user in Empresa.contratados:
            
            try:
                
                if type(user.get("funcionarios")) == []:
                    return False
            except:

                if user.get("cpf") == funcionario.cpf:
                    Empresa.contratados.remove(user)
                    promo = Gerente(**vars(funcionario))
                    Empresa.contratados.append(promo)
"""