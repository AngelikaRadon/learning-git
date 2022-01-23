import logging
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
if działanie == '1':
    wynik = a+b
elif działanie == '2':
    wynik = a-b
elif działanie == '3':
    wynik = a*b
elif działanie == '4':
    wynik = a/b    
else:
    wynik = 'Nie ma takiego działania'


logging.warning(wynik)

