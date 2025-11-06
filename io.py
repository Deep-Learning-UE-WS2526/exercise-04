from pathlib import Path


def main():
    base = Path(__file__).parent
    src = base / "wiki.txt"
    if not src.exists():
        print(f"Source file not found: {src}")
        return

    text = src.read_text(encoding="utf-8")
    # splitlines preserves sentences if each line is one sentence
    lines = [line.strip() for line in text.splitlines() if line.strip()]

    # 1) short sentences (< 30 chars)
    short = [s for s in lines if len(s) < 30]

    # 2) sentences that start with an article: Der, Die, Das
    articles = [s for s in lines if s.startswith(("Der", "Die", "Das"))]

    # 3) sentences that contain the substring 'April'
    april = [s for s in lines if "April" in s]

    (base / "short.txt").write_text("\n".join(short), encoding="utf-8")
    (base / "articles.txt").write_text("\n".join(articles), encoding="utf-8")
    (base / "april.txt").write_text("\n".join(april), encoding="utf-8")

    print(f"Wrote short.txt ({len(short)} lines), articles.txt ({len(articles)} lines), april.txt ({len(april)} lines)")


if __name__ == "__main__":
    main()
