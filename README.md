# HistInsights

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Assess historical source reliability from a local text corpus with a lightweight CLI. HistInsights scores documents by historical signal density and surfaces the most promising sources first.

## Installation

```bash
python3 -m pip install .
```

## Usage

```bash
histinsights --source-dir ./corpus
histinsights --source-dir ./corpus --top 5
```

## Contributing

Issues and pull requests are welcome. Please open an issue describing the bug or proposal before sending a code change.

## Features

- Confidence scores for document batches based on historical indicator density
- Pure stdlib implementation, no external runtime dependencies
- Reproducible local-first workflow against a directory of text files
- Optional `--top` flag to surface the most promising sources only

## Development

```bash
python3 -m pip install -e .
pytest -q
```

## License

MIT. See [LICENSE](LICENSE) for details.
