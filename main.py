
import pyrebase
import random

#funcao para sortear um numero
def sorteador():
  numNovo = True
  numeroSorteado = random.randint(1,qttNumeros)
  #testa se ja sorteou todos os numeros
  if len(listaSorteados) == qttNumeros:
    print("Todos os Numeros ja foram sorteados")
  #teste se numero ja foi sorteado     
  while  listaSorteados.__contains__(numeroSorteado):
    numeroSorteado = random.randint(1,qttNumeros)
  return numeroSorteado

#funcao para criar uma cartela
def criarCartela():
  b = []; i = []; n = []; g = []; o = [];
  #Sorteias numeros Circula as 5 letras, e 5 numeros por letra
  for x in range(6):
    #sorteia os numeros de acordo com as Letras do Bingo
    random.seed()
    for y in range(5):
      numeroSorteado = random.randint((qttNumeros/5) * (x-1) + 1,(qttNumeros/5) * x) 
      #testa se ja foi sorteado e coloca na letra correta
      if x == 1:
        while  b.__contains__(numeroSorteado):
          numeroSorteado = random.randint((qttNumeros/5) * (x-1) + 1,(qttNumeros/5) * x) 
        b.append(numeroSorteado)
      elif x == 2: 
        while  i.__contains__(numeroSorteado):
          numeroSorteado = random.randint((qttNumeros/5) * (x-1) + 1,(qttNumeros/5) * x) 
        i.append(numeroSorteado)
      elif x == 3:
        while  n.__contains__(numeroSorteado):
          numeroSorteado = random.randint((qttNumeros/5) * (x-1) + 1,(qttNumeros/5) * x) 
        n.append(numeroSorteado)
      elif x == 4:
        while  g.__contains__(numeroSorteado):
          numeroSorteado = random.randint((qttNumeros/5) * (x-1) + 1,(qttNumeros/5) * x) 
        g.append(numeroSorteado)
      elif x == 5: 
        while  o.__contains__(numeroSorteado):
          numeroSorteado = random.randint((qttNumeros/5) * (x-1) + 1,(qttNumeros/5) * x) 
        o.append(numeroSorteado)
  #tira um numero da letra N pelo ponto do meio da cartela.
  n.pop()
  cartela = [b, i, n, g, o]
  print (cartela)
  return cartela
    


#configuracao do firebase
config = {
  "apiKey": "AAAAevqFh4E:APA91bGHsNR1KP__bFMUQD06s81FWithQc3rVQex9YAHvLeow0CEA8uoU_wchzzW_4ZF_IRAn1EkOlCHVT4T8-u7Bb2Mim6jvJIP23oXOY_bESs96mTTFvd4RZyziiPDNxMzXdIzJ2QK",
  "authDomain": "bingo-e253b.firebaseapp.com",
  "databaseURL": "https://bingo-e253b.firebaseio.com/",
  "storageBucket": "bingo-e253b.appspot.com"
}
#define variaveis
firebase = pyrebase.initialize_app(config)
db = firebase.database()
listaSorteados = []
#define quantidade total de numeros do bingo
qttNumeros = 75
 #limpa base
db.child("numeros").remove()
print ('digite o numero de jogadores')
numJogadores = input()
cartelas = []
for a in range(numJogadores):
  cartelas[a] = criarCartela()

while 1:
  print ('para sortear digite "s"')
  botao = input()
  if botao == "s":
    numeroSorteado = sorteador()
    listaSorteados.append(numeroSorteado)
    listaSorteados.sort()
    db.child("numeros").push(numeroSorteado)
    print(listaSorteados)










