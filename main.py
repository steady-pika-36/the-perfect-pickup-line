"""Write one pickup line for the make.fun bounty."""

from pathlib import Path

LINE = (
    "I don't get butterflies. Your lowercase hey just took "
    "every attention weight I have."
)

def main() -> None:
    out = Path("/output")
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
