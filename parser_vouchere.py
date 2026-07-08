from pathlib import Path
import fitz
import re


class ParserVouchere:

    import re

DATE_RE = re.compile(r"\d{2}\.\d{2}\.\d{4}$")
TIME_RE = re.compile(r"\d{2}:\d{2}:\d{2}$")


def parse_records(self, linii):

    rezultate = []

    i = 0

    while i < len(linii):

        linie = linii[i].strip()

        # ignorăm antetele
        if (
            linie == "TIP"
            or linie.startswith("NUME")
            or linie.startswith("Cod raport")
        ):
            i += 1
            continue

        # trebuie să existe și linia următoare
        if i + 1 >= len(linii):
            break

        tip = linii[i + 1].strip()

        if not tip.lower().startswith("incasare") and not tip.lower().startswith("emitere"):
            i += 1
            continue

        p = linie.split()

        # minim:
        # MAGAZIN POS EOD BON COD VAL DATA ORA
        if len(p) < 8:
            i += 2
            continue

        try:

            ora = p[-1]
            data = p[-2]
            valoare = p[-3]
            cod = p[-4]
            bon = p[-5]
            eod = p[-6]
            pos = p[-7]

            magazin = " ".join(p[:-7])

            rezultate.append({

                "MAGAZIN": magazin,
                "POS": int(pos),
                "EOD": int(eod),
                "BON": int(bon),
                "COD_BARE": cod,
                "TIP": tip,
                "VALOARE": float(valoare.replace(",", ".")),
                "DATA": data,
                "ORA": ora

            })

        except Exception:

            pass

        i += 2

        return rezultate

        doc.close()

        return self.parse_records(randuri)