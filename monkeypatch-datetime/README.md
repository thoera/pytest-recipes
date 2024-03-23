# Monkeypatch `datetime` methods

This is an example showing how to monkeypatch the `datetime` methods by injecting functions to deal with the fact that built-in modules written in `C` cannot be mocked.

# Usage

Create a virtual environment and install the dependencies:

```bash
python3 -m venv venv
. venv/bin/activate
pip install pytest
```

Run the main script with:

```bash
python -m main --date 2024-08-20
```

Run the test with:

```bash
pytest
```
