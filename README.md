# Repository with automated tests for a tester assignment

Site tested: [https://www.t-mobile.pl/](https://www.t-mobile.pl/)

## Technologies used
- Python
- Pytest
- Playwright

## Test Scenarios
- As a new retail customer, I want to search for devices like a blue “iPhone 15”
- As a visitor with accessibility needs, I want to navigate the site via keyboard

## Environment Setup

### 1. Install dependencies
Make sure you have Python 3.8+ and `pip` installed.

```bash
pip install pytest playwright
pip install python-a11y-playwright
```
### 2. Install Playwright browsers

```bash
playwright install
```
### 3. Run the tests

```bash
pytest tests/
```
To run a specific test:

```bash
pytest tests/test_search_phone.py
```