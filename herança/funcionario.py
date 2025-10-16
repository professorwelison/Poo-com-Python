class Funcionario:
    def __init__(self, nome, cpf, salario):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario
    
    def aumentar_salario(self, aumento):
        if aumento > 0:
            self.salario += self.salario*aumento/100
            print(f"Novo salário: {self.salario}")
    
    def quem_sou_eu(self):
        print("Funcionário")

class Gerente(Funcionario):
    def __init__(self, nome, cpf, salario, senha, qfuncionario):
        super().__init__(nome, cpf, salario)
        self.senha = senha
        self.qfuncionario = qfuncionario

    def quem_sou_eu(self):
        print("Gerente")

g1 = Gerente("Welison", "123456789", 30000, 1234, 30)
g1.quem_sou_eu()
g1.aumentar_salario(3)

print(f"{g1.nome} - Funcionários: {g1.qfuncionario}")