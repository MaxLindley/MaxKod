import math

elever = ['Axel', 'Johan', 'Johanna', 'Oscar', 'Bill']
nummer = [1, 2, 3, 4, 5, 6]
elever.sort()
print(elever[0])
print(elever[2])
# Uppgift: Sortera listorna ovan
elever.append("Per")
elever.append("John")
elever.sort()
# Uppgift: skriv en loop som skriver ut allt innehåll i listorna
for i in elever:
    print(i)
for i in nummer:
    print(i)
# Uppgift: Lägg till 2 elever i elevlistan. Behöver du sortera om?
# Ja om loopen ska printa ut samma namn.
# Uppgift: Dubbelkolla om något av elementen i listan är tom i din lista

# Uppgift: kopiera listan på elever i en ny lista

# Uppgift: Skriv en ny lista, kalla den "basgrupp1", fyll på den med de 3 första namnen ur kopian av elevlistan

# Uppgift: Skriv en ny lista, kalla den "basgrupp2", fyll på den med resten av namnen ur kopian av elevlistan

# Uppgift: sortera nummerlistan "baklänges", d.v.s, istället för 1, 2, ...
# 6, 5, 4 ...

# Jag tycker att den ursprungliga listan ska vara en tuple och inte en list:
elever2 = ('Axel', 'Johan', 'Johanna', 'Oscar', 'Bill')

# medans er kopia ska vara en vanlig list:
elever3 = ['Axel', 'Johan', 'Johanna', 'Oscar', 'Bill']

# Varför då? Vad är skillnaden? Testa varianter av att manipulera tuple, tolka
# resultatet och skriv svaret som en kommentar
