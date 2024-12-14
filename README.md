# TIL

## 14 december
- list multiplication om een lijst te initialiseren `quadrants = [0] * 4`

## 13 december
- hoe zat het ook alweer met die stelsels van lineaire vergelijkingen? :)

## 12 december
- walrus operator

## 11 december
- decorators! In het bijzonder de decorator `@lru_caching`
- `//` is \_\_floordiv__, dat maakt voor een deling met hele getallen niet uit, maar `/` oftewel \_\_truediv__ retourneert een float en die kun je niet gebruiken voor slicing (slicing is uit de definitieve versie van dag 11 verdwenen, maar ik ben dit wel tegengekomen)
- ik verwachtte wel dat een `total = sum([doe_iets for item in list])` sneller zou zijn dan ```for item in list:\n\t total += doe_iets()```, maar een verschil van zo'n 3ms versus zo'n 50ms zag ik niet aankomen!

## 10 december

## 9 december

## 8 december
- imports van de vorm `from file import function` werken niet met een `-` in de bestandsnaam.
- `part1 = part2 = 0` werkt prima, maar `part1 = part2 = set()` niet. Meer algemeen geldt dat je dit wel zo kan doen voor primitieve types (int, float, bool, str), omdat ze immutable zijn, en voor andere types niet.
- gecompileerde code wordt opgeslagen in een folder genaamd `__pycache__` voor verbeterde performance bij herhaaldelijk runnen van dezelfde code. Als programmeur hoef je je niks van deze bestanden aan te trekken, en PyCharm verbergt ze dan ook automatisch. Deze folder wil je niet in vcs.

## 7 december
- lekker gespeeld met de libraries treelib en binarytree. Ik ben zeer te spreken over de api van binarytree, lekker simpel én compleet. Wel een beperkte usecase natuurlijk, dus mijn vreugde was groot toen treelib ook bleek te bestaan. 
- vooral geleerd dat ik beter moet nadenken over welk soort oplossing voor welk probleem. Waar ik eerder van de week de mist in ging met een recursieve oplossing die niet in memory paste, had ik hier wel die route kunnen (en moeten, denk ik) nemen.

## 6 december
- als je een datastructuur waar je over itereert wrapt in `enumerate()` krijg je een index erbij als eerste waarde, bijv `for i, line in enumerate(data):`

## 5 december
- sets and dicts
  - beiden worden met curly braces aangegeven. `{}` creeert een lege dict. Lege set nodig? `set()`
- dicts
  - een structuur met key value paren is een dict
  - er is ook een defaultdict. De constructor kun je een type meegeven en dat krijg je dan terug als je een key opvraagt die er niet is. Bijv: `rule_dict = defaultdict(set)`. In werkelijkheid wordt de niet bestaande key aangemaakt, met een lege of default waarde van het gespecificeerde type, wanneer je 'm opvraagt.
- als je een argument aan een variabele toewijst creeer je een pointer. Als je de waarde bewerkt is dit dus niet veilig! Dit moet ik trouwens nog oplossen in de code van vandaag.

## 4 december
Je kunt een variabele `_` noemen als de waarde genegeerd wordt. Bijv: `['' for _ in range(num_rows + num_cols - 1)]`

## 3 december

Regexdag!

- basic gebruik van de regex lib `re`:
    - met `re.compile(r'<regex-hier>')` maak je een Pattern object #TODO zoek uit wat die `r` voor de string voor ding
      is
    - daar kun je verschillende zoekacties mee uitvoeren, zoals bijvoorbeeld `findall()` en `match()`
    - twee manieren om dat te doen: `pattern.findall(source)` of `re.findall(pattern, source)`. Geen idee of er een
      reden is om voor de een of de ander te kiezen behalve persoonlijke voorkeur
- regex-details:
    - je kunt `'` niet escapen. Zet je regex in dubbele quotes als je op een single quote wilt matchen
    - `(?!...)` oftewel negative lookahead assertion. Geeft een hit als de expressie niet matcht
    - bijvoorbeeld: `r"(do)(?!n't)"` matcht wel op `do` maar niet op `don't`
    - `|` ,oftewel alternation. Geplaatst tussen twee patterns matcht ie op de een of de ander.

## 2 december

- list slicing: met `lijst[beginindex:eindindex]` krijg je een slice van de inputlijst. Je kun één of beide indexen ook
  leeg laten voor het eerste respectievelijk laatste element van de lijst. `lijst[:]` levert dus de gehele lijst. Er
  zijn een heleboel leuk trucjes uit te halen met slicing, vandaag bijvoorbeeld gecombineerd met concatenatie:
  `list[:i] = list[i+1:]`, dan krijg je een kopie van je lijst maar zonder het element op positie `i`.
- `all()` is een functie die checkt of alle items in de iterable die je 'm meegeeft `True` zijn. Dat lijkt niet
  supernuttig, maar gecombineerd met een list comprehension of generator expression is het superkrachtig en leesbaar:
  `all(condition for item in iterable)` Dat brengt me bij het volgende:
- python heeft list comprehensions, jeeh :) Syntax: `new_list = [expression for member in iterable]`.
- een generator expression ziet er uit als een list comprehension zonder de []. Het grote voordeel van een generator
  expression ten opzichte van een list comprehension is dat ie lazy evalueert.

## 1 december

- `split()` zonder argument splitst op whitespace
- met `tuple()` kun je de output van `zip()` printbaar maken