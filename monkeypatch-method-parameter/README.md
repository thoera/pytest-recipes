# Monkeypatch a parameter of a method

This is an example showing how to monkeypatch a parameter of a method using `functools.partialmethod()`.

The main idea of using `functools.partialmethod()` is to be able to specify a parameter of the method without having to copy-paste any code.

# Usage

Create a virtual environment and install the dependencies:

```bash
python3 -m venv venv
. venv/bin/activate
pip install pytest
```

Run the main script with:

```bash
python -m main --name <your_name> --birthday <your_birthday> --save
```

This will create a JSON file called `birthday.jsonl`.

Run the test with:

```bash
pytest -rA
```

There is only one test which will test the creation of a file. This illustrates how to manipulate the path of the saved file (which is a parameter set to None by default in the main class).

The `-rA` argument is useful to show extra test summary info (like the path of the saved file in that case).
