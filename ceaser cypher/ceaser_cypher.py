import encode
logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""


print(logo)

print('_'*100 )

print("Digite 'enconde' para criptar uma mensagem, ou 'decode' para descriptar uma mensagem ")
user = input().lower()
print('_'*100 )
if user == 'encode':
    mensagem = input('Digite a mensagem: \n')
    print('_'*100 )
    chave = int(input('Qual será a chave da mensagem? \n'))
    print('_'*100 )
    encode.encripta(mensagem,chave)
elif user == 'decode':
    mensagem = input('Digite a mensagem que quer descriptografar: \n')
    print('_'*100 )
    chave = int(input('Qual é a chave da mensagem? \n'))
    print('_'*100 )
    encode.desencripta(mensagem,chave)


    


