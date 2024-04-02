# Puzzle 8 (Aufgabenblatt 1)

## Aufgabe 1 (Parität)

> a) Welche Parität hat der Zustand S in Abb. 1?

`16` also `gerade` und somit `lösbar`

> b) Implementieren Sie eine Funktion zur Berechnung der Parität eines Zustands.

Siehe `./paritaet.py`

## Aufgabe 2 (Heuristiken)

> a) Für einen Zustand z ist h1(z) die Anzahl der falsch platzierten Steine in Bezug auf den Zielzustand. In Abb. 1 ist h1(S) = 8. Wieso ist h1 eine monotone Heuristik?

Die Falschplatzierten Felder können weniger werden, aber niemals kleiner als 0, 0 würde bedeuten das alle Felder richtig sind.

> b) Für einen Zustand z ist h2(z) die Summe der Manhattan-Distanzen der Steine von ihren
> Zielpositionen. In Abb. 1 ist h2(S) = 3 + 1 + 2 + 2 + 2 + 3 + 3 + 2 = 18. Wieso ist h2 eine
> monotone Heuristik?

Der Weg bis zum richtigen Ort kann niemals kleiner als 0 sein.

> c) Wieso ist h1(n) ≤ h2(n)? Welche Heuristik ist also besser?

h1 nur die falschplatzierten Felder zählt, somit kann schlechter gesagt werden ob dieser Zug besser als der andere ist.
Bei h2 werden die entfernungen vom richtigen Feld berechnet, was bei einem Zug ein genauers Ergebniss liefert.

> d) Implementieren Sie beide Heuristiken.

Siehe `./heuristik.py`

## Aufgabe 3 (Suchverfahren IDS und A\*)

> a) Implementieren Sie Suchverfahren für das 8-Puzzle in zwei Varianten:
>
> - Iterativ vertiefende Suche (iterative deepening depth-first search IDS)
> - A\* mit einer der Heuristiken aus Aufgabe 2. Gerne dürfen Sie auch eine andere Heuristik einsetzen.

> b) Testen Sie Ihre Suchverfahren für zufällig generierte Startzustände. Beachten Sie dabei die Paritätsüberlegung in Aufgabe 1.

> c) Bestimmen Sie die Anzahl der vom Suchverfahren generierten Zustände und die Länge der Lösungsfolge für verschiedene Startzustände. Für das Board in Abb. 1 links sind 26 Züge notwendig.

> d) Sind Ihre Zugfolgen optimal? Wenn ja, warum?

> e) Welches Problem könnte entstehen (nicht ausprobieren!), falls mit Ihrem Programm (IDS und A\*) das 15-Puzzle gelöst werden sollte?
