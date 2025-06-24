import os


def print_directory(path):
    # Unicode-Zeichen
    TEE = chr(9500)  # ├
    ELBOW = chr(9492)  # └
    VERT = chr(9474)  # │
    DASH = chr(9472)  # ─
    # print(TEE, ELBOW, VERT, DASH)

    with os.scandir(path) as entries:
        entries = list(entries)
        for i, entry in enumerate(entries):
            connector = TEE if i < len(entries) - 1 else ELBOW
            print(f"{connector}{DASH*2} {entry.name}")


print_directory(".")
