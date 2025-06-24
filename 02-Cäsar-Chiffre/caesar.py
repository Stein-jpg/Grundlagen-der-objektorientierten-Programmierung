import sys


def encode_text(text, key):
    result = []

    # schleife die den text verschlüsselt
    for ch in text:
        if ch.isupper():
            base = ord("A")
            offset = (ord(ch) - base + key) % 26  # modulo 26 damit nach Z wieder A
            result.append(chr(base + offset))
        elif ch.islower():
            base = ord("a")
            offset = (ord(ch) - base + key) % 26
            result.append(chr(base + offset))
        else:
            result.append(ch)  # sonderzeichen bleiben unverändert

    return "".join(result)


def main():
    if len(sys.argv) < 3:
        print("Fehler: Bitte Text und Schlüssel angeben.")
        print(' python ceasar.py "Das ist ein Text" 3')
        sys.exit(1)

    text = sys.argv[1]
    key = int(sys.argv[2])

    print(encode_text(text, key))


if __name__ == "__main__":
    main()
