import logging
from tkinter import Variable
logging.basicConfig(level=logging.DEBUG)

logging.info('Kalkulator')
logging.info('1. Dodawanie')
logging.info('2. Odejmowanie')
logging.info('3. Mnożenie')
logging.info('4. Dzielenie')
logging.info('Podaj pierwszy składnik: ')
a = int(input())
logging.info('Podaj drugi składnik: ')
b = int(input())
wynik = 0
działanie = input('Wybierz działanie: ')
def dodawanie(a,b):
  if działanie == '1':
    wynik = a+b
    
def odejmowanie(a,b):    
  if działanie == '2':
    wynik = a-b
    
def mnożenie(a,b):
  if działanie == '3':
    wynik = a*b
    
def dzielenie(a,b):
  if działanie == '4':
    wynik = a/b
    variable = 1/0
    logging.info(wynik)





wynik_dodawania = a+b
logging.debug('Suma: {} + {} = {}'.format(a, b, wynik_dodawania))
wynik_odejmowania = a-b
logging.debug('Różnica: {} + {} = {}'.format(a, b, wynik_odejmowania))
wynik_mnożenia = a*b
logging.debug('Iloczyn: {} + {} = {}'.format(a, b, wynik_mnożenia))
wynik_dzielenia = a/b
logging.debug('Iloraz: {} + {} = {}'.format(a, b, wynik_dzielenia))