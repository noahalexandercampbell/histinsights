"""Allow ``python -m histinsights`` invocation."""

from histinsights.cli import main

if __name__ == "__main__":
    raise SystemExit(main())
