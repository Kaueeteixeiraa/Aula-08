class Estudante:
    def __init__(self, nome, idade, curso):
        self.nome = nome
        self.idade = idade
        self.curso = curso
        
    def texto(self):
        print(f"O meu nome é {self.nome}, minha idade é {self.idade} e meu curso é {self.curso}")

    def aniversario(self):
        self.idade += 1

        aluno1 = Estudante("Kaue", 20, "análise")
        aluno2 = Estudante("Kayan", 19, "engenharia")
        aluno3 = Estudante("Kauan", 21, "filosofia")

        aluno1.texto()
        aluno2.texto()
        aluno3.texto()

        aluno1.aniversario()

        print("Idade depois do aniversario:")
        
        aluno1.texto()
        aluno2.texto()
        aluno3.texto()