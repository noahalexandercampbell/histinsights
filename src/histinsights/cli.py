"""HistInsights CLI."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Iterable, List, Tuple


def _approximate_historical_density(text: str) -> float:
    indicators = (
        "annex",
        "art.",
        "bce",
        "century",
        "chronicle",
        "colony",
        "coronation",
        "dated",
        "dynasty",
        "empire",
        "established",
        "founded",
        "kingdom",
        "monarch",
        "proclamation",
        "reign",
        "revolution",
        "treaty",
        "truce",
        "year",
    )
    lower = text.lower()
    count = sum(lower.count(token) for token in indicators)
    tokens = max(1, len(lower.split()))
    return count / tokens


def evaluate(paths: Iterable[Path]) -> List[Tuple[str, float]]:
    results: List[Tuple[str, float]] = []
    errors: List[str] = []
    for path in paths:
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except Exception as exc:
            errors.append(f"Failed to read {path}: {exc}")
            continue
        results.append((path.name, _approximate_historical_density(text)))
    return results


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Assess reliability of historical text sources.",
    )
    parser.add_argument(
        "--source-dir",
        type=Path,
        default=Path("corpus"),
        help="Directory containing source documents.",
    )
    parser.add_argument(
        "--top",
        type=int,
        default=0,
        help="Limit output to the N most promising sources.",
    )
    args = parser.parse_args()
    if not args.source_dir.exists():
        print(f"Error: source directory not found: {args.source_dir}", file=sys.stderr)
        return 1
    results = evaluate(args.source_dir.iterdir())
    results.sort(key=lambda item: item[1], reverse=True)
    if args.top > 0:
        results = results[: args.top]
    if results:
        print("source,density")
        for name, density in results:
            print(f"{name},{density:.4f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
