from pathlib import Path
import json
import sys

import yaml
from jsonschema import Draft202012Validator, FormatChecker


ROOT = Path(__file__).resolve().parents[1]


VALIDATION_TARGETS = [
    {
        "name": "Space Friendship Event",
        "schema": ROOT / "schemas" / "space-friendship-event.schema.json",
        "examples": [
            ROOT / "examples" / "collision-risk-event.example.yaml",
            ROOT / "examples" / "debris-warning-event.example.yaml",
            ROOT / "examples" / "ai-false-positive-review.example.yaml",
        ],
    },
    {
        "name": "Neutral Coordination Node",
        "schema": ROOT / "schemas" / "neutral-coordination-node.schema.json",
        "examples": [
            ROOT / "examples" / "neutral-coordination-node.example.yaml",
        ],
    },
        {
        "name": "De-escalation Workflow",
        "schema": ROOT / "schemas" / "de-escalation-workflow.schema.json",
        "examples": [
            ROOT / "examples" / "de-escalation-workflow.example.yaml",
        ],
    },
]


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def load_yaml(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def format_error_path(error) -> str:
    return ".".join(str(part) for part in error.path) or "<root>"


def validate_target(target: dict) -> bool:
    schema_path = target["schema"]
    example_paths = target["examples"]

    print(f"[validate] {target['name']}")
    print(f"  schema: {schema_path.relative_to(ROOT)}")

    if not schema_path.exists():
        print(f"[error] Schema file not found: {schema_path.relative_to(ROOT)}")
        return False

    missing_examples = [path for path in example_paths if not path.exists()]
    if missing_examples:
        for path in missing_examples:
            print(f"[error] Example file not found: {path.relative_to(ROOT)}")
        return False

    schema = load_json(schema_path)

    try:
        Draft202012Validator.check_schema(schema)
    except Exception as exc:
        print(f"[error] Invalid JSON Schema: {schema_path.relative_to(ROOT)}")
        print(f"  message: {exc}")
        return False

    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    target_ok = True

    for example_path in example_paths:
        print(f"  example: {example_path.relative_to(ROOT)}")
        data = load_yaml(example_path)
        errors = sorted(validator.iter_errors(data), key=lambda e: e.path)

        if errors:
            target_ok = False
            print(f"  [error] {example_path.name} failed validation")
            for error in errors:
                print(f"    - path: {format_error_path(error)}")
                print(f"      message: {error.message}")
        else:
            print(f"  [ok] {example_path.name} is valid")

    return target_ok


def main() -> int:
    all_ok = True

    for target in VALIDATION_TARGETS:
        target_ok = validate_target(target)
        all_ok = all_ok and target_ok

    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main())
