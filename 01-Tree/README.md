# Aufgabe 1a - Vereinfachtes "tree"-Programm

Die Datei [tree.py](tree.py) implementiert eine nicht-rekursive Version des "tree"-Befehls.
Die Verzeichniseinträge werden mit Unicode-Symbolen dargestellt und alphabetisch Sortiert.

Zuerst habe ich die Zeichen in meiner Funktion deklariert und mir die Symbole in der Console angeschaut:
![screen1](screenshot-1.jpg) ![screen1.1](screenshot-1.1.jpg)

Danach habe ich os.scandir() implementiert und musste es erstmal mit "import os" importieren. Ich wollte mit einer For schleife durch die einzelnen Verzeichnisse iterieren und diese dann mit den symbolen zusammen ausgeben (beim letzten symbol dann "ELBOW" und 2x "DASH" + name in jeder iteration). Ich habe dann jedoch einen Error: "TypeError: object of type 'nt.ScandirIterator' has no len()" erhalten. Das lag daran weil der ScandirIterator ein Objekt ausgibt und es nicht die methode len() unterstützt. Als Lösung habe ich das Object dann einfach vor der Schleife in eine liste umgewandelt mit "list()".

![screen1](screenshot-2.jpg) ![screen1.1](screenshot-2.1.jpg)
