def exercicio1 ():
    class PetGato:
        #construtor
        def __init__(self,nome_do_pet):
            #atributos
            self.nome = str(nome_do_pet)

    petshop = PetGato("psicoPATO")

    print(f"O nome do meu gato é: {petshop.nome}")

def exercicio2():
    class Alunos:
        #construtor
        def __init__(self,nome_aluno,nome_turma):
            #atributos
            self.nome = int(nome_aluno)
            self.nomet = str(nome_turma)

    chamada = Alunos("Deivid","Informática segundo ano B")

    print(f" Deivid? {chamada.nome}\n {chamada.nomet}")

def exercicio3 ():
    class Garcon:
        def __init__ (self,matricula,nome,telefone,comissao):
            #construtor
            self.cod_matricula = int(matricula)
            self.garcom_nome = str(nome)
            self.num_telefone = str(telefone)
            self.valor_comisso = float(comissao) 