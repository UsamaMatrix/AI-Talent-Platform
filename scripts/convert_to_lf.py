"""Convert all Python files in the repo to LF line endings."""
import pathlib

ROOT = pathlib.Path(__file__).parent.parent

PATTERNS = ["apps/api/src/**/*.py", "apps/api/tests/**/*.py",
            "apps/worker/src/**/*.py", "apps/worker/tests/**/*.py"]

converted = 0
for pattern in PATTERNS:
    for path in ROOT.glob(pattern):
        content = path.read_bytes()
        lf_content = content.replace(b"\r\n", b"\n")
        if lf_content != content:
            path.write_bytes(lf_content)
            print(f"Converted: {path.relative_to(ROOT)}")
            converted += 1

print(f"\nDone. {converted} files converted to LF.")
