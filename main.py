from pathlib import Path

Path('/output').mkdir(parents=True, exist_ok=True)
Path('/output/entry.txt').write_text("Our office printer has a paper jam; it says the meeting could've been an email.", encoding="utf-8")
