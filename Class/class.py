class User:
    pass


user_1 = User()
user_1.id = '001'
user_1.username = "leo"

print(user_1.username)

#------------------------#

class User2:
    def __init__(self):
        print('hello') #essa funcao roda quando o codigo inicializa


user = User2()


#----------------------------------#

class Car:
    def __init__(self, bancos,portas,cor):
        self.banco = f'O carro tem {bancos} acentos'
        self.portas = f'O carro tem {portas} portas'
        self.cor = f'O carro tem a cor {cor}'

    def sportmode(self,banco):
        banco = 2
        print(f'agora o carro tem {banco} portas')





carro1 = Car(5,4,'azul')

print(carro1.banco)
print(carro1.portas)
print(carro1.cor)
carro1.sportmode(4)