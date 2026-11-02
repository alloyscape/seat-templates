from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SEAT = ROOT / "templates" / "seat"
EXPECTED = {
    "README.md",
    "soul.system.md",
    "start-SEAT-think.sh",
    "SEAT-home.html",
    "nginx.snippet.conf",
}
REQUIRED_PLACEHOLDERS = {
    "soul.system.md": {"{{SEAT}}"},
    "SEAT-home.html": {"{{SEAT}}", "{{THINK_PORT}}"},
    "nginx.snippet.conf": {"{{THINK_PORT}}"},
}


def read_text(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    if "\ufffd" in text or "\x1a" in text:
        raise ValueError(f"{path.relative_to(ROOT)} contains replacement/control characters")
    return text


def main() -> None:
    actual = {path.name for path in SEAT.iterdir() if path.is_file()}
    missing = sorted(EXPECTED - actual)
    if missing:
        raise SystemExit(f"missing template files: {', '.join(missing)}")

    for name, placeholders in REQUIRED_PLACEHOLDERS.items():
        text = read_text(SEAT / name)
        absent = sorted(token for token in placeholders if token not in text)
        if absent:
            raise SystemExit(f"{name} is missing placeholders: {', '.join(absent)}")

    start = read_text(SEAT / "start-SEAT-think.sh")
    required_shell = (
        "set -euo pipefail",
        "THINK_HOST=127.0.0.1",
        'THINK_TRIBE_TOOLBELT="${THINK_TRIBE_TOOLBELT:-false}"',
    )
    absent_shell = [item for item in required_shell if item not in start]
    if absent_shell:
        raise SystemExit(f"start script is missing safety settings: {', '.join(absent_shell)}")

    for name in EXPECTED:
        read_text(SEAT / name)

    print(f"validated {len(EXPECTED)} seat template files")


if __name__ == "__main__":
    main()
