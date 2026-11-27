# Playwright QA Automation Framework

A Python-based test automation framework built with Playwright and Pytest, following the Page Object Model (POM) design pattern.

This project demonstrates practical QA Automation skills, including browser automation, reusable page objects, test organization, logging, automated reporting and PowerShell execution.

## Project Overview

The framework automates end-to-end user workflows on [SauceDemo](https://www.saucedemo.com/) and includes browser navigation examples using Google.

The main objective is to demonstrate a maintainable automation structure with reusable components, clear test scenarios and automated execution reports.

## Tech Stack

- **Python** – Programming language
- **Playwright** – Browser automation
- **Pytest** – Test execution and test organization
- **Page Object Model (POM)** – Test architecture
- **pytest-json-report** – Test results in JSON format
- **HTML / CSS** – Custom test reporting dashboard
- **PowerShell** – Test execution automation
- **Git / GitHub** – Version control

## Project Structure

```text
playwright_learning/
│
├── common/
│   ├── __init__.py
│   └── helpers.py
│
├── MANUAL_QA/
│   ├── 00_INDICE.md
│   ├── 01_ENTORNO_VIRTUAL.md
│   └── ...
│
├── pages/
│   ├── __init__.py
│   ├── detalle_producto.py
│   ├── google_page.py
│   ├── pagina_login.py
│   ├── pagina_productos.py
│   ├── pagina_carrito.py
│   └── pagina_checkout.py
│
├── reporting/
│   ├── __init__.py
│   └── generate_report.py
│
├── tests/
│   ├── conftest.py
│   ├── test_01_open_page.py
│   ├── test_02_google_search.py
│   ├── test_03_login.py
│   ├── test_04_add_to_cart.py
│   └── test_05_manual_testing.py
│
├── requirements.txt
├── run_tests.ps1
├── README.md
└── .gitignore
```

## Framework Architecture

The project follows the Page Object Model pattern to separate test scenarios from page-specific elements and actions.

### Pages

The `pages/` directory contains page objects responsible for:

- Locating web elements.
- Performing user interactions.
- Exposing reusable methods.
- Validating page states and expected results.

### Tests

The `tests/` directory contains the automated test scenarios.

Each test focuses on a specific user workflow and uses the page objects to interact with the application.

### Fixtures

The `tests/conftest.py` file provides shared Playwright fixtures.

The framework creates an isolated browser context for each test and ensures resources are closed after execution.

### Reporting

The `reporting/` directory contains the custom HTML report generator.

Test results are collected in JSON format using `pytest-json-report` and transformed into an HTML dashboard.

## Automated Test Scenarios

The current suite includes five test scenarios:

| Test | Description |
|---|---|
| Test 01 | Open a web page |
| Test 02 | Navigate from Google to SauceDemo |
| Test 03 | Validate SauceDemo login |
| Test 04 | Add a product to the shopping cart |
| Test 05 | Execute a complete shopping cart workflow |

The scenarios cover browser navigation, login validation, product selection, shopping cart operations and product detail navigation.

## Automated Reporting

The framework generates a custom HTML dashboard containing test execution information.

The reporting process includes:

- Total tests executed.
- Passed, failed and skipped tests.
- Execution duration.
- Test-level results.
- Error details when available.

Generated reports are stored in the `reports/` directory.

## Installation

### Requirements

- Python 3.10 or higher
- Git
- PowerShell
- Visual Studio Code (recommended)

### 1. Clone the repository

```bash
git clone https://github.com/elopezori/senior-qa-automation-portfolio.git
```

### 2. Navigate to the project directory

```bash
cd senior-qa-automation-portfolio/playwright_learning
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 6. Install Playwright browsers

```bash
python -m playwright install chromium
```

## Running the Tests

Execute the PowerShell script from the project directory:

```powershell
.\run_tests.ps1
```

The script automatically:

1. Checks Python and Pytest availability.
2. Prepares the reports directory.
3. Removes previous JSON test results.
4. Executes the automated test suite.
5. Generates the JSON results file.
6. Creates the HTML dashboard.
7. Opens the generated report.

## Running Tests Manually

To execute the complete test suite directly:

```bash
python -m pytest tests -v
```

To execute an individual test:

```bash
python -m pytest tests/test_03_login.py -v
```

## Current Project Status

The framework has been executed successfully in a local Windows environment.

**Latest validated execution:**

- Total tests: 5
- Passed: 5
- Failed: 0
- Skipped: 0

The project currently focuses on local browser automation and reporting. CI/CD integration is not yet implemented.

## QA Documentation

The `MANUAL_QA/` directory contains supporting QA documentation, including environment setup, manual testing concepts and testing checklists.

This documentation complements the automation framework and demonstrates a broader understanding of software quality assurance.

## Author

**QA Automation Engineer**

GitHub: [elopezori](https://github.com/elopezori)
