##Esta linha fara com que o codigo suporte letras com acentos ou c com cedilha
# -*- coding: UTF-8 -*-

### Libraries ###
#Esta biblioteca serve para ler os daods do sensores do Sense HAT
from sense_hat import SenseHat

#Esta função é importada para dar uma "pausa" no funcionamento do códio quando necessário
from time import sleep

# Esta função será usada para rodar vários "pedaços" do código ao mesmo tempo, mas o
# emulador ainda não a suporta, então será desativado por agora
#from threading import Thread

# From datetime import datetime
# Esta biblioteca pareçe não estar disponivel no TrinketIo, então vamos usar outra
import time

# A diferença entre "from x import y" e "import x" é que no segundo é necessário escrever x.y()
# mas no primeiro só é preciso usar y(), no entanto na primeira só será importada essa função
# dessa biblioteca


### Logging Settings ###

#Dirá de quanto em quantos segundos o programa deverá salvar os valores dos sensores
DELAY = 1

### Functions ###

#Esta função irá obter os dados dos sensores necessários
def get_sense_data():
  sense = SenseHat()
  
  global sense_data
  sense_data=[]
  
  sense_data.append(sense.get_temperature_from_humidity())
  sense_data.append(sense.get_temperature_from_pressure())
  sense_data.append(sense.get_humidity())
  sense_data.append(sense.get_pressure())

  #https://docs.python.org/2/library/time.html?highlight=time#time.strftime
  sense_data.append(time.strftime("%d-%m-%Y %H:%M:%S"))
  sleep(DELAY)
  return sense_data

#Verifica se um valor x se encontra entre os valores min e máx, INCLUSIVE
def between(x, min, max):
  return x > min and x < max

#Verifica se a estação encontra-se em condições boas, se estiver mandará de volta o valor verdadeiro
def is_habitable():
  return between(sense_data[0], 18, 27) and between(sense_data[1], 18, 27) and between(sense_data[3], 980, 1027) and between(sense_data[2] ,50, 70)
    
#Coloca um ponto de exclamação no ecrâ, indicado que há perigo
def danger():
  #para definir um pixel é usado uma lista com [r, g, b] (red green blue) que pode ser entre [0,255]
  
  #red
  r = [255, 0, 0]
  #white
  w = [255, 255, 255]
  #black
  b = [0, 0, 0]
  
  screen1 = [ 
    b, b, b, r, r, b, b, b,
    b, b, b, r, r, b, b, b,
    b, b, b, r, r, b, b, b,
    b, b, b, r, r, b, b, b,
    b, b, b, r, r, b, b, b,
    b, b, b, r, r, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, r, r, b, b, b
  ]
  
  screen2 = [
    w, w, w, r, r, w, w, w,
    w, w, w, r, r, w, w, w,
    w, w, w, r, r, w, w, w,
    w, w, w, r, r, w, w, w,
    w, w, w, r, r, w, w, w,
    w, w, w, r, r, w, w, w,
    w, w, w, w, w, w, w, w,
    w, w, w, r, r, w, w, w
    ]

  while True:
    sense.set_pixels(screen1)
    sleep(1)
    sense.set_pixels(screen2)
    sleep(1)
  return 
### Main Code ###
sense = SenseHat()

#Limpa o ecrâ antes de executar o código
sense.clear()

# Para dar tempo para os valores serem ajustados no emulador, é esperado que o utilizador 
# aperte enter para o programa começar
input("Aperte enter para começar o programa")

print(get_sense_data())

while is_habitable():
  print(get_sense_data())
danger()
