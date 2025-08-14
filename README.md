# My Python Project

A comprehensive Python project with web automation capabilities using Selenium, Playwright, Robot Framework, and pytest.

## Getting Started

1. Clone this repository
2. Install dependencies:
   ```bash
   pip3 install -r requirements.txt
   ```
3. Run the main script:
   ```bash
   python3 test.py
   ```

## Project Structure

- `test.py` - Main Python script using Playwright for web automation
- `gmail_test.robot` - Basic Robot Framework test for Gmail
- `web_automation_demo.robot` - Comprehensive Robot Framework demo
- `test_web_automation.py` - pytest tests for web automation
- `test_main_functionality.py` - pytest tests for main functionality
- `pytest.ini` - pytest configuration
- `requirements.txt` - Python dependencies
- `README.md` - Project documentation

## Features

### Python Script (`test.py`)
- Open Gmail using Playwright
- Open multiple websites in separate tabs
- Interactive menu system

### Robot Framework Tests
- **gmail_test.robot**: Basic Gmail website testing
- **web_automation_demo.robot**: Comprehensive web automation examples

### pytest Tests
- **test_web_automation.py**: Web automation tests using Playwright
- **test_main_functionality.py**: Tests for main functionality and dependencies

## Running Tests

### Robot Framework Tests
```bash
# Run all Robot Framework tests
robot *.robot

# Run specific test file
robot gmail_test.robot

# Run tests with specific tags
robot --include selenium *.robot

# Generate detailed reports
robot --outputdir reports *.robot
```

### pytest Tests
```bash
# Run all pytest tests
python3 -m pytest

# Run specific test file
python3 -m pytest test_web_automation.py

# Run tests with verbose output
python3 -m pytest -v

# Run tests and generate HTML report
python3 -m pytest --html=reports/pytest_report.html

# Run specific test class
python3 -m pytest test_web_automation.py::TestWebAutomation

# Run tests with specific markers
python3 -m pytest -m "web"
```

## Dependencies

- **Selenium**: Web automation with browser drivers
- **Playwright**: Modern web automation framework
- **Robot Framework**: Test automation framework
- **Robot Framework SeleniumLibrary**: Selenium integration for Robot Framework
- **Robot Framework Playwright**: Playwright integration for Robot Framework
- **pytest**: Python testing framework
- **pytest-playwright**: Playwright integration for pytest
- **pytest-selenium**: Selenium integration for pytest

## Test Reports

After running tests, you'll find reports in:
- **Robot Framework**: `log.html`, `report.html`, `output.xml`
- **pytest**: `reports/pytest_report.html`

## License

This project is open source and available under the [MIT License](LICENSE).
