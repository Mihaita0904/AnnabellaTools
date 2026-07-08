from pathlib import Path
import fitz


class ParserVouchere:
    def __init__(self, pdf_path):
        self.pdf_path = Path(pdf_path)

    def parse(self):
        """
        Returnează lista liniilor utile din PDF.
        Deocamdată NU parsează coloanele.
        """
        if not self.pdf_path.exists():
            raise FileNotFoundError(self.pdf_path)

        rezultate = []

        doc = fitz.open(self.pdf_path)

        print(f"PDF deschis ({doc.page_count} pagini)\n")

        for nr, pagina in enumerate(doc, start=1):
            print(f"Pagina {nr}/{doc.page_count}")

            text = pagina.get_text()

            for linie in text.splitlines():

                linie = " ".join(linie.split())

                if not linie:
                    continue

                # eliminăm antetele
                if "NUME" in linie and "VCH_COD_BARE" in linie:
                    continue

                if "Cod raport" in linie:
                    continue

                rezultate.append(linie)

        doc.close()

        return rezultate