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
