# Repository with automated tests for a tester assignment
# T-Mobile Automation Testing Project - Environment Setup
## Project Overview
This repository contains automated tests for the T-Mobile website ([https://www.t-mobile.pl/](https://www.t-mobile.pl/)). The tests cover common user scenarios including device search and accessibility testing.
## Technologies Used
- Python 3.11
- Pytest 8.3.5
- Playwright 1.51.0
- Python-A11y-Playwright 1.0.1

### Docker Support
The project now supports running tests in Docker containers, ensuring consistent test execution across different environments:
- Added `Dockerfile` for containerized test execution
- Added `docker-compose.yml` for easy container management
- Container runs tests in headless mode with proper browser configurations

### Virtual Environment Setup
For local development, the project now includes scripts to easily set up and use Python virtual environments:
- `setup.sh` (Unix/Linux/Mac) and `setup.bat` (Windows) scripts to create and configure virtual environments
- `run_tests.sh` (Unix/Linux/Mac) and `run_tests.bat` (Windows) scripts to execute tests within the virtual environment

## Getting Started
### Option 1: Using Docker (Recommended for CI/CD)
``` bash
# Build and run tests in Docker
docker-compose up
```
### Option 2: Using Virtual Environment (Recommended for Development)
``` bash
# For Unix/Linux/Mac
chmod +x setup.sh
./setup.sh
./run_tests.sh

# For Windows
setup.bat
run_tests.bat
```
### Manual Installation
``` bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # Unix/Linux/Mac
venv\Scripts\activate.bat  # Windows

# Install dependencies
pip install -r requirements.txt

# Install Playwright browsers
playwright install chromium

# Run tests
pytest tests/
```
## Test Scenarios
- **Device Search Test:** Simulates a customer searching for a blue iPhone 15
- **Accessibility Test:** Validates website accessibility compliance using Axe

## Project Structure
``` 
project/
├── pages/            # Page object models
├── tests/            # Test scenarios
├── reports/          # Test reports directory
├── requirements.txt  # Python dependencies
├── Dockerfile        # Container configuration
├── docker-compose.yml # Docker services setup
├── setup.sh/bat      # Environment setup scripts
├── run_tests.sh/bat  # Test execution scripts
└── README.md         # Project documentation
```
## Notes
- Test reports are saved to the `reports/` directory
- IDE configuration files (.idea/) are now ignored in git
- The project is configured to run in both containerized and local environments
