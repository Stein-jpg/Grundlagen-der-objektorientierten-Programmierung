# Aufgabe 1 - Tree-Funktion

Die Datei [tree.py](tree.py) implementiert eine vereinfachte Version des "tree"-Befehls.
Die Verzeichniseinträge werden mit Unicode-Symbolen dargestellt und alphabetisch Sortiert.

## Teil a) - Einfache Ausgabe

Zuerst habe ich die Zeichen in meiner Funktion deklariert und mir die Symbole in der Console angeschaut:

```python
def print_directory(path):
    # Unicode-Zeichen
    TEE = chr(9500)  # ├
    ELBOW = chr(9492)  # └
    VERT = chr(9474)  # │
    DASH = chr(9472)  # ─
    print(TEE, ELBOW, VERT, DASH)

print_directory(".")
```

<details>
<summary>Console</summary>

![screen1.1](screenshot-1.1.jpg)

</details>

Danach habe ich os.scandir() implementiert und musste es erstmal mit "import os" importieren. Ich wollte mit einer For schleife durch die einzelnen Verzeichnisse iterieren und diese dann mit den symbolen zusammen ausgeben (beim letzten symbol dann "ELBOW" und 2x "DASH" + name in jeder iteration). Ich habe dann jedoch einen Error: "TypeError: object of type 'nt.ScandirIterator' has no len()" erhalten. Das lag daran weil der ScandirIterator ein Objekt ausgibt und es nicht die methode len() unterstützt. Als Lösung habe ich das Object dann einfach vor der Schleife in eine liste umgewandelt mit "list()".

```python
import os

def print_directory(path):
    # Unicode-Zeichen
    TEE = chr(9500)  # ├
    ELBOW = chr(9492)  # └
    VERT = chr(9474)  # │
    DASH = chr(9472)  # ─

    with os.scandir(path) as entries:
        entries = list(entries)
        for i, entry in enumerate(entries):
            connector = TEE if i < len(entries) - 1 else ELBOW
            print(f"{connector}{DASH*2} {entry.name}")

print_directory(".")
```

<details>
<summary>Console</summary>

![screen2.1](screenshot-2.1.jpg)

</details>

Zuletzt wurde mein Code mit der Zeile "entries = sorted(entries, key=lambda f: f.name.lower())" erweiter um sicherzustellen, dass es auch Sortiert wird. Leider kann ich das nur schlecht veranschaulichen, weil meine IDE die Dateien automatisch sortiert deswegen zeige ich es mit dem parameter Reverse: True:

```python
import os

def print_directory(path):
    # Unicode-Zeichen
    TEE = chr(9500)  # ├
    ELBOW = chr(9492)  # └
    VERT = chr(9474)  # │
    DASH = chr(9472)  # ─

    with os.scandir(path) as entries:
        # iterator in Liste Umwandeln
        entries = list(entries)
        # liste sortieren
        entries = sorted(entries, key=lambda f: f.name.lower(), reverse=True)
        for i, entry in enumerate(entries):
            connector = TEE if i < len(entries) - 1 else ELBOW
            print(f"{connector}{DASH*2} {entry.name}")

if __name__ == "__main__":
    print_directory(".")
```

<details>
<summary>Console</summary>

![screen3.1](screenshot-3.1.jpg)

</details>

## Teil b) - Erweiterung mit Rekursion und Einrückung

Zuerst wurde die Funktion print_directory mit

```python
def print_directory(path, indentation_level=0):
```

erweiter.

Danach habe ich das Print statement zu folgendem abgeändert:

```python
print(f"{'    ' * indentation_level}{connector}{DASH*2} {entry.name}")
```

Zuletzt habe ich noch am Ende der Schleife folgendes angefügt:

```python
# Wenn weiteres Directory wiederhole print_directory (rekursiv)
if entry.is_dir():
    print_directory(entry.path, indentation_level + 1)
```

Nun ist mir aufgefallen das mir der Vertikale Strich fehlt und dass ich diesen ja nur Anzeigen will wenn ich in einem Unter-Verzeichnis bin also habe ich folgende logik eingebaut und das Print Statement angepasst:

```python
# Einrückung mit │ nur bei level > 0
if indentation_level > 0:
    indent = (VERT + "    ") * indentation_level
else:
    indent = "    " * indentation_level

print(f"{indent}{connector}{DASH*2} {entry.name}")
```

Der Komplette Code und die Consolen augabe sehen nun so aus:

```python
import os


def print_directory(path, indentation_level=0):
    # Unicode-Zeichen
    TEE = chr(9500)  # ├
    ELBOW = chr(9492)  # └
    VERT = chr(9474)  # │
    DASH = chr(9472)  # ─

    with os.scandir(path) as entries:
        # iterator in Liste Umwandeln
        entries = list(entries)
        # liste sortieren
        entries = sorted(entries, key=lambda f: f.name.lower(), reverse=False)
        for i, entry in enumerate(entries):
            connector = TEE if i < len(entries) - 1 else ELBOW

            # Einrückung mit │ nur bei level > 0
            if indentation_level > 0:
                indent = (VERT + "    ") * indentation_level
            else:
                indent = "    " * indentation_level

            print(f"{indent}{connector}{DASH*2} {entry.name}")

            # Wenn weiteres Directory wiederhole print_directory (rekursiv)
            if entry.is_dir():
                print_directory(entry.path, indentation_level + 1)


if __name__ == "__main__":
    print_directory(".")
```

<details>
<summary>Console</summary>

![screen4.1](screenshot-4.1.jpg)

</details>
