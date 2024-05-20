# Edhouse ukol pro stážisty

## Zadání

Předtím než nastoupíš do Edhouse, musíš odpracovat zkušební směnu na tzv. Předůležitém překladišti. Přece nebudeme do Edhousu brát někoho, kdo nám neukáže, že „za to umí vzít“. Autobus, tě spolu s ostatními stážisty právě vysadil před vraty velké haly překladiště.

„Ach, to je zase den!“ povzdechne si urostlý chlap v ošoupaných monterkách stojící opodál. „Hej ty novej, pocem“ huláká a ukazuje prstem na tebe. “Já su Eda. Potřebuju helfnout.” bručí, zatímco z náprsní kapsy vytahuje aktuální mapku zboží na překladišti.

Eda potřebuje, abys sečetl čísla aktivních kontejnerů. Budeš k tomu potřebovat jeho mapku, kterou najdeš přiloženou k tomuto zadání. Podívejme se na následující příklad:

```
467..257..
...*......
..35..633.
......#...
617*......
.....+.13.
..592.....
......755.
...$.*....
.664.598..
```

Na mapce je vyznačena spousta čísel a symbolů, kterým úplně nerozumíš. To ale nevadí, protože jak Eda prozrazuje, každé číslo, které sousedí s nějakým symbolem, byť diagonálně, je číslo aktivního kontejneru a je nutné ho započítat do výsledné sumy (Tečky (.) nepovažujeme za symbol). Na mapce příkladu jsou dvě čísla, která nejsou čísly aktivního kontejneru, neboť nesousedí s žádným symbolem: 257 (vpravo nahoře) a 13 (vpravo uprostřed). Všechna ostatní čísla sousedí s nějakým symbolem a tudíž se jedná o čísla aktivních kontejnerů; jejich součet je 4361.

### Vstupní data

Edova skutečná mapka je samozřejmě mnohem větší a najdeš ji vloženou v tomto dokumentu a pro jistotu také přiloženou.

[mapka.txt](mapka.txt)

Jaký je součet čísel aktivních kontejnerů na Edově mapce?

## Popis zvoleného prostredia a inštrukcie a spustenie programu

Program je napísaný v jazyku Python 3. Na spustenie programu je potrebné mať nainštalovaný Python vo verzii 3.11
Inštrukcie na spustenie:
Uložte priložený súbor ako `ukol.py`
Vstupný súbor na kontrolu čísel (napr. `mapka.txt`) umiestnite do rovnakého adresára ako skript.
Spustite skript pomocou
`python ukol.py [volitelná_cesta]`
Ak nezadáte cestu k súboru, skript predpokladá, že sa v rovnakom adresári nachádza súbor `mapka.txt`

## Popis použitého algoritmu

Program načíta súbor, ktorý prevedie do dvojrozmernej matice podla riadkov a znakov.
Prechádza každý znak v matici. Ak nájde číslicu, kontroluje, či je platná podľa toho, či nejaký susedný znak je znak iný od bodky alebo čísla.
Ak platné číslo nájde, pridá ho k celkovému súčtu.

## Vypočítaná hodnota

557705

## ukol.exe

Taktiež v repozitári s nachádza `ukol.exe`, je to jednoduchá aplikácia s gui, v ktorej po stupstení ste schopný si vybrať súbor, ktorý chcete skontrolovať a po stlačení tlačidla `RUN` sa vypíše vypočítaná hodnota. Taktiež sa validné čísla ukážu zelenou farbou.

## Závěr

Tento repozitár obsahuje:

1. `ukol.py` - skript, ktorý po spustení vypíše vypočítanú hodnotu
2. `mapka.txt` - súbor s vstupnými dátami
3. `README.md` - tento súbor
4. `ukol.exe` - skompilovaný súbor pre Windows
