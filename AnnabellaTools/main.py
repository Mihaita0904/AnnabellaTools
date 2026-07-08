from parser_vouchere import ParserVouchere
from excel_export import ExcelExport

PDF = "vouchere.pdf"
OUT = "output/vouchere.xlsx"

def main():
    parser = ParserVouchere(PDF)
    df = parser.parse()

    ExcelExport.export(df, OUT)

    print(f"Exportate {len(df)} înregistrări.")

if __name__ == "__main__":
    main()
