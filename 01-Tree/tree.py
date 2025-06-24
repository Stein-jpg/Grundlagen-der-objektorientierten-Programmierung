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
