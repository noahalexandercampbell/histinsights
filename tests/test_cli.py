"""Tests for HistInsights."""
from __future__ import annotations

from pathlib import Path

from histinsights.cli import evaluate, _approximate_historical_density

ROOT = Path(__file__).resolve().parent.parent


def make_document(name: str, text: str) -> Path:
    path = ROOT / "corpus" / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return path


def test_density_zero_without_indicators() -> None:
    assert _approximate_historical_density("modern text without history") == 0.0


def test_density_grows_with_indicators() -> None:
    text = "The treaty was signed after the revolution in the empire during his reign."
    density = _approximate_historical_density(text)
    assert density > 0.0


def test_evaluate_calculates_density() -> None:
    ancient = make_document(
        "ancient.txt",
        "The empire issued a proclamation establishing a new kingdom.",
    )
    modern = make_document(
        "modern.txt",
        "Modern software tools improve developer productivity.",
    )
    results = dict(evaluate([modern, ancient]))
    assert results["ancient.txt"] > 0.0
    assert results["modern.txt"] == 0.0
