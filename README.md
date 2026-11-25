# Calculator with Memory

A calculator that remembers every sum, even after you close it. It has two front ends, a terminal app and a web page, sharing one Python class and one SQLite database.

Built as my first complete Python project while learning backend development.

## Features

- Add, subtract, multiply and divide (`+ - * /`)
- **Persistent history:** every result is saved to SQLite and still there after a restart
- **Two front ends, one brain:**
  - a terminal app (`history`, `clear`, `quit`)
  - a web page served by a FastAPI API
- **Error handling:** division by zero, unknown operators and non-numeric input are handled without crashing. Errors are never saved to the history
- **Input validation** in the API with Pydantic (bad requests get a `422`)

## How it works

```
Terminal (calculator_app.py) ─┐
                              ├──▶ Calculate class (calculator_core.py) ──▶ calculator.db
Web page (index.html) ──▶ FastAPI (api.py) ─┘
```

| File | Job |
| --- | --- |
| `calculator_core.py` | The `Calculate` class: does the maths and reads and writes the history in SQLite |
| `calculator_app.py` | The terminal interface |
| `api.py` | The FastAPI app: serves the page and the API endpoints |
| `index.html` | The web page (HTML + JavaScript using `fetch`) |
| `requirements.txt` | Python dependencies |

## Run it

Requires Python 3.12.

```bash
git clone https://github.com/MohitNadipineni/calculator-with-memory.git
cd calculator-with-memory
python3.12 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

**Terminal version:**

```bash
python calculator_app.py
```

Type a sum with spaces, like `12 / 4`, or `history`, `clear` or `quit`.

**Web version:**

```bash
uvicorn api:app --reload
```

Then open http://127.0.0.1:8000 for the page, or http://127.0.0.1:8000/docs to try the API.

The database file `calculator.db` is created automatically on first run.

## API

| Method | Path | What it does |
| --- | --- | --- |
| `GET` | `/` | Serves the web page |
| `POST` | `/calculate` | Body `{"a": 12, "op": "/", "b": 4}` returns `{"result": 3.0}` |
| `GET` | `/history` | Returns `{"history": [{"expression": "12.0 / 4.0", "result": 3.0}, ...]}` |
| `DELETE` | `/history` | Clears the history |

## Built with

Python, SQLite (`sqlite3`), FastAPI, Uvicorn, Pydantic, HTML and JavaScript.

## What I learned

- Classes and methods, and keeping logic (the class) separate from the interface (the terminal or the web)
- Saving data with SQLite, using safe `?` placeholders
- Handling errors with `try` / `except`
- Building a REST API with FastAPI, validating input with Pydantic, and reading status codes and tracebacks
- Connecting a web page to an API with `fetch`
- Virtual environments, `requirements.txt`, `.gitignore` and Git

## Next steps

- Round long decimal results on the page
- Add styling with CSS
- Add automated tests with `pytest`
