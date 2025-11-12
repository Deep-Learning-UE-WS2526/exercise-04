# io.py
from pathlib import Path

INPUT = Path("wiki.txt")
OUT_SHORT = Path("short.txt")
OUT_ARTICLES = Path("articles.txt")
OUT_APRIL = Path("april.txt")
ARTICLES = ("Der", "Die", "Das")

def read_lines(path: Path) -> list[str]:
    """Liest wiki.txt als UTF-8 und gibt getrimmte, nicht-leere Zeilen zurück."""
    with path.open("r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

def write_lines(path: Path, lines: list[str]) -> None:
    """Schreibt eine Zeile pro Satz, UTF-8, sauberes Zeilenende."""
    with path.open("w", encoding="utf-8", newline="\n") as f:
        if lines:
            f.write("\n".join(lines) + "\n")

def main() -> None:
    base = Path(__file__).parent
    src = base / INPUT
    if not src.exists():
        print(f"Quelle nicht gefunden: {src}")
        return

    try:
        sentences = read_lines(src)
    except UnicodeDecodeError:
        print("Kodierungsfehler beim Lesen von wiki.txt (erwarte UTF-8).")
        return

    # 1) < 30 Zeichen
    short_sentences = [s for s in sentences if len(s) < 30]

    # 2) beginnt mit Der/Die/Das (exakte Großschreibung)
    article_sentences = [s for s in sentences if s.startswith(ARTICLES)]

    # 3) enthält 'April' (case-sensitiv gemäß Aufgabenbeschreibung)
    april_sentences = [s for s in sentences if "April" in s]

    # schreiben
    write_lines(base / OUT_SHORT, short_sentences)
    write_lines(base / OUT_ARTICLES, article_sentences)
    write_lines(base / OUT_APRIL, april_sentences)

    print(
        f"Fertig: {OUT_SHORT} ({len(short_sentences)}), "
        f"{OUT_ARTICLES} ({len(article_sentences)}), "
        f"{OUT_APRIL} ({len(april_sentences)})"
    )

if __name__ == "__main__":
    main()
