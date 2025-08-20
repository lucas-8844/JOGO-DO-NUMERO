import random
numero = int(input("escreva um numero de 1 a 10:"))
numero_certo = random.randint(1,10)
tentativa = 0
while numero != numero_certo:
        tentativa += 1
        if numero > numero_certo:
         print("Muito Alto, tente um numero mais baixo:")
        else:
             print("muito baixo, tente um numero maior:")
        numero = int(input("escreva um numero de 1 a 10:"))
print(f"Parabéns, você acertou em {tentativa} tentativas!") 