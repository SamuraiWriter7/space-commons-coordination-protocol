from pathlib import Path
import json
import sys

import yaml
from jsonschema import Draft202012Validator, FormatChecker


ROOT = Path(__file__).resolve().parents[1]

SCHEMA_PATH = ROOT / "schemas" / "space-friendship-event.schema.json"

EXAMPLES = [
    ROOT / "examples" / "collision-risk-event.example.yaml",
    ROOT / "examples" / "debris-warning-event.example.yaml",
    ROOT / "examples" / "ai-false-positive-review.example.yaml",
]


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def load_yaml(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def main() -> int:
    schema = load_json(SCHEMA_PATH)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())

    failed = False

    for example_path in EXAMPLES:
        print(f"[validate] {example_path.relative_to(ROOT)}")
        data = load_yaml(example_path)
        errors = sorted(validator.iter_errors(data), key=lambda e: e.path)

        if errors:
            failed = True
            print(f"[error] {example_path.name} failed validation")
            for error in errors:
                path = ".".join(str(part) for part in error.path) or "<root>"
                print(f"  - path: {path}")
                print(f"    message: {error.message}")
        else:
            print(f"[ok] {example_path.name} is valid")

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
