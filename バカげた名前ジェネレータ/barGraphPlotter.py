def main():
    chars: dict[str, int] = {}

    for i in range(26):
        chars[chr(i + 97)] = 0

    file = input("Enter the file name: ")
    with open(file, "r") as f:
        for line in f:
            for char in line:
                if char.isalpha():
                    chars[char.lower()] += 1

    greatest = max(chars.values())
    minimum = min(chars.values())

    for k, v in chars.items():
        normalize = int(50 * (v - minimum) / (greatest - minimum))
        bar = "■" * normalize
        print(f"{k}: {bar}")


if __name__ == "__main__":
    main()
