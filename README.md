# Brightstone Logistics Report Generator

A command-line Python application that reads order data from a CSV file, processes it, and generates a report in Markdown or JSON.

## Features

- CSV validation and custom exception handling
- Centralized error handling and logging
- Markdown and JSON report generation
- `argparse` CLI with a clean `--help` message
- Output format/extension validation
- Exit codes: `0` success, `1` input/CLI error, `2` system/configuration error
- Ruff formatting and linting
- Strict Mypy type checking
- Automated tests with **100% test coverage**

## Setup

Requires Python 3.12 or newer. A virtual environment is recommended.

```bash
python -m venv .venv
.venv\Scripts\activate
```

Install the development tools used by the project:

```bash
python -m pip install ruff mypy pytest pytest-cov
```

## CLI Usage

The tool starts with:

```bash
python -m report --input orders.csv --output report.md --format markdown
```

Arguments:

| Argument | Required | Description |
|---|---|---|
| `--input` | Yes | Input CSV file |
| `--output` | Yes | Generated report file |
| `--format` | No | `markdown` or `json`; defaults to `markdown` |

Examples:

```bash
python -m report --input orders.csv --output report.md --format markdown
python -m report --input orders.csv --output report.json --format json
python -m report --input orders.csv --output report.md
python -m report --help
```

The selected format must match the output extension. For example, Markdown requires `.md` and JSON requires `.json`. A mismatch raises `MismatchReportFormat`, is logged, and returns exit code `1`.

## Technical Notes

### Data and Processing

`orders.csv` is **dummy/sample test data** included to demonstrate and test the CLI. It is not production data.

CSV values are initially read as strings and converted by the `Order` model to the appropriate types, such as `quantity` to `int` and `price` to `float`.

The processing layer calculates:

- Total number of orders
- Total revenue
- Top products by revenue
- Top spending customers
- Revenue per category

Revenue is calculated as:

```text
quantity × unit price
```

Products are ranked by revenue.

### Report Generation

Report generation is separated from processing logic. The application supports:

```text
Markdown → .md
JSON     → .json
```

The Markdown report contains the calculated totals, top products, top customers, revenue by category, and a generation timestamp.

### Error Handling and Logging

Expected errors use custom exceptions including:

- `InvalidCSVError`
- `InvalidCSVRow`
- `MissingColumnError`
- `MismatchReportFormat`

Errors are handled centrally in `main.py` and logged with Python's `logging` module rather than error-related `print()` statements.

Exit codes:

| Code | Meaning |
|---|---|
| `0` | Successful execution |
| `1` | Input or CLI problem |
| `2` | System/configuration problem |

### Package Structure

`classes/__init__.py` makes `classes` an explicit Python package, allowing imports such as:

```python
from classes.order import Order
```

`report/__main__.py` provides the module entry point for:

```bash
python -m report
```

`report/__init__.py` marks `report` as a package and does not require application logic.

The project also uses `classes/types.py` for shared structured type definitions such as `ProductRevenue` and customer-spending types.

## Project Structure

```text
project/
├── classes/
│   ├── __init__.py
│   ├── order.py
│   └── types.py
├── report/
│   ├── __init__.py
│   └── __main__.py
├── tests/
│   ├── test_csv.py
│   ├── test_order.py
│   ├── test_processing.py
│   └── test_reporting.py
├── csv_handling.py
├── exceptions.py
├── main.py
├── processing_logic.py
├── report_logic.py
├── utils.py
├── orders.csv
├── pyproject.toml
├── README.md
└── .gitignore
```

## Quality Checks and Testing

Ruff formatting:

```bash
ruff format --check .
```

Ruff linting:

```bash
ruff check .
```

Strict type checking:

```bash
mypy --strict .
```

Run all tests:

```bash
python -m pytest
```

Run tests with coverage:

```bash
python -m pytest --cov --cov-report=term-missing
```

The project currently achieves **100% test coverage**.

## Final Verification

Before committing or submitting, run:

```bash
ruff format --check .
ruff check .
mypy --strict .
python -m pytest
python -m pytest --cov --cov-report=term-missing
```

All required checks pass and the test suite achieves **100% coverage**.
