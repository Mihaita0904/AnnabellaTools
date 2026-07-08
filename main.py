from parser_vouchere import ParserVouchere


def main():

    parser = ParserVouchere("input/vouchere.pdf")

    linii = parser.parse()

    print()
    print("=" * 60)
    print(f"Linii citite: {len(linii)}")
    print("=" * 60)
    print()

    print("Primele 20 linii:\n")

    for linie in linii[:20]:
        print(linie)


if __name__ == "__main__":
    main()