import fitz


class ParserVouchere:

    def __init__(self, pdf_file):
        self.pdf_file = pdf_file

    def citeste_randuri(self):

        doc = fitz.open(self.pdf_file)

        toate_randurile = []

        print(f"\nPagini: {len(doc)}\n")

        for nr_pagina, pagina in enumerate(doc, start=1):

            print(f"Pagina {nr_pagina}")

            # toate cuvintele cu coordonate
            words = pagina.get_text("words")

            # grupare pe coordonata Y
            rows = {}

            for w in words:

                x0, y0, x1, y1, text, *_ = w

                # rotunjim coordonata pentru a grupa pe aceeași linie
                key = round(y0)

                rows.setdefault(key, []).append((x0, text))

            # sortare după poziția X
            for key in sorted(rows):

                linie = sorted(rows[key], key=lambda v: v[0])

                text = " ".join([v[1] for v in linie]).strip()

                if text:
                    toate_randurile.append(text)

        doc.close()

        return toate_randurile


if __name__ == "__main__":

    pdf = input("PDF: ").strip()

    parser = ParserVouchere(pdf)

    randuri = parser.citeste_randuri()

    print("\n")

    print("=" * 80)

    print(f"Randuri citite: {len(randuri)}")

    print("=" * 80)

    print()

    for r in randuri[:40]:
        print(r)
