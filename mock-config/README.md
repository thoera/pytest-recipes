# Mock a configuration file

This is an example showing how to mock the content of a configuration file using `patch.object()` and `patch.dict()` from `unittest.mock`.

# Usage

Create a virtual environment and install the dependencies:

```bash
python3 -m venv venv
. venv/bin/activate
pip install omegaconf pytest
```

Run the main script with:

```bash
python -m main
```

Run the tests with:

```bash
pytest
```
