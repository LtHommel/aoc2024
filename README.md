# TIL
## Day 1
- `split()` zonder argument splitst op whitespace
- met `tuple()` kun je de output van `zip()` printbaar maken

## Day 2
- list slicing! Met `lijst[beginindex:eindindex]` krijg je een slice van de inputlijst. Je kun één of beide indexen ook leeg laten voor het eerste respectievelijk laatste element van de lijst. `lijst[:]` levert dus de gehele lijst. Er zijn een heleboel leuk trucjes uit te halen met slicing, vandaag bijvoorbeeld gecombineerd met concatenatie: `list[:i] = list[i+1:]`, dan krijg je een kopie van je lijst maar zonder het element op positie `i`. 
- `all()` is een functie die checkt of alle items in de iterable die je 'm meegeeft `True` zijn. Dat lijkt niet supernuttig, maar gecombineerd met een list comprehension of generator expression is het superkrachtig en leesbaar: `all(condition for item in iterable)` Dat brengt me bij het volgende:
- python heeft list comprehensions, yay :) Syntax: `new_list = [expression for member in iterable]`.
- een generator expression ziet er uit als een list comprehension zonder de []. Het grote voordeel van een generator expression is dat ie lazy evalueert.