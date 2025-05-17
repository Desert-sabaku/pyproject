def main():
    file = input("Enter the file name:")
    with open(file, "r") as f:
        text = f.read()

    transed_txt: list[str] = []

    for word in text.split():
        word = word.lower()
        word = word.strip(".,!?\"'()[]{}<>;:")  # Remove punctuation

        if word.startswith(("a", "e", "i", "o", "u")):
            word += "way"
        else:
            word = word[1:] + word[0] + "ay"

        transed_txt.append(word)

    print(" ".join(transed_txt))


if __name__ == "__main__":
    main()
