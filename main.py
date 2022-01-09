lista_zakupów = {'piekarnia' : ['chleb', 'pączek', 'drożdżówka'], 'warzywniak' : ['pomidor', 'ogórek', 'marchewka', 'seler'] }
ilosc = 0
for sklep, rzeczy in lista_zakupów.items():
  print("Idę do, {} kupuję {}" .format(sklep, rzeczy))
  ilosc += len(rzeczy)
  
print("W sumie kupuję {} produktów" .format (ilosc))