# TIL
## 1 december
- `split()` zonder argument splitst op whitespace
- met `tuple()` kun je de output van `zip()` printbaar maken

## 2 december
- list slicing: met `lijst[beginindex:eindindex]` krijg je een slice van de inputlijst. Je kun één of beide indexen ook leeg laten voor het eerste respectievelijk laatste element van de lijst. `lijst[:]` levert dus de gehele lijst. Er zijn een heleboel leuk trucjes uit te halen met slicing, vandaag bijvoorbeeld gecombineerd met concatenatie: `list[:i] = list[i+1:]`, dan krijg je een kopie van je lijst maar zonder het element op positie `i`. 
- `all()` is een functie die checkt of alle items in de iterable die je 'm meegeeft `True` zijn. Dat lijkt niet supernuttig, maar gecombineerd met een list comprehension of generator expression is het superkrachtig en leesbaar: `all(condition for item in iterable)` Dat brengt me bij het volgende:
- python heeft list comprehensions, jeeh :) Syntax: `new_list = [expression for member in iterable]`.
- een generator expression ziet er uit als een list comprehension zonder de []. Het grote voordeel van een generator expression ten opzichte van een list comprehension is dat ie lazy evalueert.

## 3 december
Regexdag!
- basic gebruik van de regex lib `re`: 
  - met `re.compile(r'<regex-hier>')` maak je een Pattern object #TODO zoek uit wat die `r` voor de string voor ding is
  - daar kun je verschillende zoekacties mee uitvoeren, zoals bijvoorbeeld `findall()` en `match()`
  - twee manieren om dat te doen: `pattern.findall(source)` of `re.findall(pattern, source)`. Geen idee of er een reden is om voor de een of de ander te kiezen behalve persoonlijke voorkeur 
- regex-details:
  - je kunt ' niet escapen. Zet je regex in dubbele quotes als je op een single quote wilt matchen
  - `(?!...)` oftewel negative lookahead assertion. Geeft een hit als de expressie niet matcht
  - bijvoorbeeld: `r"(do)(?!n't)"` matcht wel op `do` maar niet op `don't`
  - `|` ,oftewel alternation. Geplaatst tussen twee patterns matcht ie op de een of de ander.
