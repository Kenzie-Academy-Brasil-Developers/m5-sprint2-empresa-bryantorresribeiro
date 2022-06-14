from classes.empresa import Empresa
from classes.funcionario import Funcionario
from classes.gerente import Gerente

def Tarefa1():
    print("*"*100)

    funcionario_1 = Funcionario(" jordan  cardoso poole ", "32112343215")
    print(funcionario_1.__dict__)
    # {
    #  'nome_completo': 'Jordan Cardoso Poole', 
    #  'cpf': 32112343215, 
    #  'salario': 3000, 
    #  'admissao': '26-05-2022'
    # }
    print(funcionario_1)
    # <Funcionário: Jordan Cardoso Poole>

def Tarefa2():
    print("*"*100)

    empresa_1 = Empresa("  kenzie   brasil ", "12345678910124")
    print(empresa_1.__dict__)
    # {'nome': 'Kenzie Brasil', 'cnpj': 12345678910124, 'contratados': []}
    print(len(empresa_1))
    # 0

    funcionario_1 = Funcionario(" jordan  cardoso poole ", "32112343215")
    funcionario_2 = Funcionario("  stephen  alves curry ", "12332145665")

    # CPF CORRETO
    resposta = empresa_1.contratar_funcionario(funcionario_1)
    empresa_1.contratar_funcionario(funcionario_2)
    print(resposta) 
    # Funcionário contratado!
    print(f'CONTRATADOS: {len(empresa_1)}')
    # CONTRATADOS: 2
    print(f'EMAIL: {funcionario_1.email}')
    # Email: jordan_cardoso_poole@kenziebrasil.com
    print(f'Empresa: {funcionario_1.empresa}')
    # Empresa: Kenzie Brasil

    # CPF REPETIDO
    resposta = empresa_1.contratar_funcionario(funcionario_2)
    print(resposta) 
    # Funcionário com esse CPF já foi contratado.

    # Ao executar esse método deverá gerar o diretório e arquivo na pasta empresas 
    holerite = empresa_1.gerar_holerite(funcionario_1)
    print(holerite)
    # True

    # Funcionario não contratado
    funcionario_3 = Funcionario("lamelo  ball souza ", "98778965434")
    holerite = empresa_1.gerar_holerite(funcionario_3)
    print(holerite)
    # False

def Tarefa3():
    print("*"*100)

    gerente_1 = Gerente(" bill    gates ", "32132186712", 10000)
    print(gerente_1.__dict__)
    # {
    #  'nome_completo': 'Bill Gates', 
    #  'cpf': '32132186712', 
    #  'salario': 10000, 
    #  'admissao': '27-05-2022', 
    #  'funcionarios': []
    # }

    print(len(gerente_1))
    # 0

    empresa_1 = Empresa("  kenzie    brasil ", "12345678910124")
    funcionario_1 = Funcionario(" jordan  cardoso poole ", "32112343215")
    gerente_2 = Gerente("steve  kerr ", "76532186123")
    # Contratando funcionários
    empresa_1.contratar_funcionario(funcionario_1)
    empresa_1.contratar_funcionario(gerente_1)
    empresa_1.contratar_funcionario(gerente_2)
    # Empresa diferente
    empresa_2 = Empresa(" golden state warriors  ", "12345678910111")
    funcionario_3 = Funcionario("lamelo  ball souza ", "98778965434")
    empresa_2.contratar_funcionario(funcionario_3)

    resposta = gerente_1.adicionar_funcionario(funcionario_1)
    print(resposta) 
    # True
    resposta = gerente_1.adicionar_funcionario(funcionario_1)
    print(resposta) 
    # False
    resposta = gerente_1.adicionar_funcionario(gerente_2)
    print(resposta) 
    # False
    resposta = gerente_1.adicionar_funcionario(funcionario_3)
    print(resposta)
    # False
    print(f'FUNCIONARIOS: {len(gerente_1)}')
    # FUNCIONARIOS: 1

def Tarefa4():
    print("*"*100)
    
    empresa_1 = Empresa("  kenzie   brasil ", 12345678910124)
    funcionario_1 = Funcionario(" jordan  cardoso poole ", 32112343215)
    gerente_1 = Gerente(" bill    gates ", "32132186712")
    gerente_3 = Gerente("elon musk", "12342186574")
    # Adicionando funcionários
    empresa_1.contratar_funcionario(funcionario_1)
    empresa_1.contratar_funcionario(gerente_1)
    empresa_1.contratar_funcionario(gerente_3)
    # Adicionando funcionário ao gerente
    gerente_1.adicionar_funcionario(funcionario_1)
    # Funcionário não contratado
    funcionario_4 = Funcionario("klay mota thompson ", 92478965434)

    empresa_1.gerar_holerite(funcionario_1)
    holerite = Empresa.ler_holerite(empresa_1 ,funcionario_1)
    print(holerite)
    # {
    #  'nome': 'Jordan Cardoso Poole', 
    #  'cpf': 32112343215, 
    #  'salario': 3000, 
    #  'mes': 'May', 
    #  'admissao': 
    #  '27-05-2022'
    # }

    print(len(empresa_1.contratados))
    # 3
    resposta = empresa_1.demissao(funcionario_4)
    print(resposta) 
    # Não consta esse CPF na empresa
    resposta = empresa_1.demissao(gerente_3) 
    print(resposta) 
    # Gerente demitido!
    print(len(gerente_1.funcionarios)) 
    # 1
    resposta = empresa_1.demissao(funcionario_1)
    print(resposta) 
    # Funcionário demitido!
    print(len(gerente_1.funcionarios)) 
    # 0
    print(len(empresa_1.contratados)) 
    # 1

def Tarefa5():
    print("*"*100)

    funcionario_1 = Funcionario(" jordan  cardoso poole ", "32112343215")
    funcionario_4 = Funcionario("klay mota thompson ", "92478965434")
    gerente_3 = Gerente("elon musk", "12342186574")
    empresa_1 = Empresa("  kenzie   brasil ", "12345678910124")
    # Contratação do funcionário
    empresa_1.contratar_funcionario(funcionario_1)

    resposta = empresa_1.promocao(gerente_3)
    print(resposta) 
    # False
    resposta = empresa_1.promocao(funcionario_4)
    print(resposta) 
    # False
    print(funcionario_1.funcao)
    # Funcionário
    resposta = empresa_1.promocao(funcionario_1)
    print(resposta.funcao) 
    # Gerente

    funcionario_1 = Funcionario(" jordan  cardoso poole ", "32112343215")
    funcionario_4 = Funcionario("klay mota thompson ", "92478965434")
    gerente_1 = Gerente(" bill    gates ", "32132186712")
    empresa_1 = Empresa("  kenzie   brasil ", "12345678910124")

    # Contratação dos funcionários
    empresa_1.contratar_funcionario(funcionario_1)
    empresa_1.contratar_funcionario(gerente_1)

    # Adicionar funcionário ao gerente
    gerente_1.adicionar_funcionario(funcionario_1)

    resposta = gerente_1.aumento_salarial(funcionario_4, empresa_1)
    print(resposta) 
    # False
    print(funcionario_1.salario) 
    # 3000
    resposta = gerente_1.aumento_salarial(funcionario_1, empresa_1)
    print(resposta.funcao) 
    # Funcionário
    print(resposta.salario) 
    # 3300

    # Aqui vamos setar um valor alto para teste
    funcionario_1.salario = 7500
    print(funcionario_1.salario) 
    # 7500
    resposta = gerente_1.aumento_salarial(funcionario_1, empresa_1)
    print(resposta.funcao) 
    # Gerente
    print(resposta.salario) 
    # 8250 
            
if __name__ == "__main__":
    Tarefa1()
    Tarefa2()
    Tarefa3()
    Tarefa4()
    Tarefa5()


   