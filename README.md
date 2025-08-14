# My Python Project

A comprehensive Python project with web automation capabilities using Selenium, Playwright, and Robot Framework.

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

## Running Robot Framework Tests

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

## Dependencies

- **Selenium**: Web automation with browser drivers
- **Playwright**: Modern web automation framework
- **Robot Framework**: Test automation framework
- **Robot Framework SeleniumLibrary**: Selenium integration for Robot Framework
- **Robot Framework Playwright**: Playwright integration for Robot Framework

## License

This project is open source and available under the [MIT License](LICENSE).
