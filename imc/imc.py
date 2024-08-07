print('*'*50)
peso = float(input("Digite aqui o seu peso: \n"))
altura = float(input("Digite aqui a altura: \n"))
#Primeiro comando
media = peso/(altura * altura)

print('*'*50)
print(f"IMC: {media:.2f}")

if media < 18.5:
  print("Você está abaixo do peso normal")
#se a media for abaixo de 18,5: "Você está abaixo do peso normal"
elif media < 25:
  print("Você está no peso normal")
#se a media for acima de 18,5 e abaixo de 24,9: "Você está no peso normal"
elif media < 30:
  print("Você está com excesso de peso")
#se a media for acima de 25,0 e abaixo de 29,9: "Você está excesso de peso"
elif media < 35:
  print("Você está com Obesidade Classe I")
#se a media for acima de 30,0 e abaixo de 34,9: "Você está com obesidade Classe I"
elif media < 40:
  print ("Você está com obesidade Classe II")
#se a media for acima de 35,0 e abaixo de 39,9: "Você está com obesidade Classe II"
elif media >= 40:
  print ("Você está com Obesidade Mórbida! Se cuide!")
#se a media for acima de 40: "Você está com Obesidade Mórbida!""
print('*'*50)