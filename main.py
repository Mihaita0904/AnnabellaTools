from parser_vouchere import ParserVouchere
import pandas as pd


def main():

    parser = ParserVouchere("input/vouchere.pdf")

    rows = parser.parse()

    df = pd.DataFrame(rows)

    print(df.head(20))

    print()

    print(df.info())

    print()

    print(f"Total inregistrari: {len(df)}")


if __name__ == "__main__":
    main()