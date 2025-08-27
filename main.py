import random
import string
try:
  numero = int(input("escreva um numero de 1 a 100:"))
  numero_certo = random.randint(1,100)
  tentativa = 1
  nome = string 
  tentativas_passadas = []
  while numero != numero_certo:
        if numero in tentativas_passadas:
           print("você ja usou este numero, tente outro!")
        else:
         tentativas_passadas.append(numero)
         tentativa += 1
         if numero > numero_certo:
          print("Muito Alto, tente um numero mais baixo:")
         else:
             print("muito baixo, tente um numero maior:")
        numero = int(input("escreva um numero de 1 a 100:"))
  print(f"Parabéns, você acertou em {tentativa} tentativas!")
  print(tentativas_passadas)
except:
 print("Entrada não é valida")
'''pegar o nome do jogador, salvar a pontuação e jogar denovo, se for o mesmo, salva a resposta'''
