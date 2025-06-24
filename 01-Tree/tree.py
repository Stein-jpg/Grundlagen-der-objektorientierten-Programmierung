def print_directory(path):
    # Unicode-Zeichen
    TEE = chr(9500)  # ├
    ELBOW = chr(9492)  # └
    VERT = chr(9474)  # │
    DASH = chr(9472)  # ─
    print(TEE, ELBOW, VERT, DASH)


print_directory(".")
