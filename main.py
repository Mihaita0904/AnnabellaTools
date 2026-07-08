from pathlib import Path


def main():
    print("=" * 60)
    print(" AnnabellaTools v0.1")
    print("=" * 60)

    pdf = Path("input") / "vouchere.pdf"

    if not pdf.exists():
        print(f"\n❌ Nu am găsit fișierul:\n{pdf}")
        return

    print(f"\n✅ PDF găsit:\n{pdf}")
    print("\nUrmătorul pas: parsarea PDF-ului...")


if __name__ == "__main__":
    main()