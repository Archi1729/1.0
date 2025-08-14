import pytest
import sys
import os

# Add the current directory to Python path to import test module
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import the functions from test.py
from test import open_gmail, open_multiple_sites

class TestMainFunctionality:
    """Test class for main functionality from test.py"""
    
    def test_open_gmail_function_exists(self):
        """Test that open_gmail function exists and is callable"""
        assert callable(open_gmail)
        print("✅ open_gmail function exists and is callable")
    
    def test_open_multiple_sites_function_exists(self):
        """Test that open_multiple_sites function exists and is callable"""
        assert callable(open_multiple_sites)
        print("✅ open_multiple_sites function exists and is callable")
    
    def test_import_playwright(self):
        """Test that Playwright can be imported"""
        try:
            from playwright.sync_api import sync_playwright
            print("✅ Playwright import successful")
        except ImportError as e:
            pytest.fail(f"Failed to import Playwright: {e}")
    
    def test_playwright_browser_launch(self):
        """Test that Playwright can launch a browser"""
        from playwright.sync_api import sync_playwright
        
        with sync_playwright() as p:
            try:
                browser = p.chromium.launch(headless=True)
                page = browser.new_page()
                page.goto("https://example.com")
                assert page.title() == "Example Domain"
                browser.close()
                print("✅ Playwright browser launch successful")
            except Exception as e:
                pytest.fail(f"Failed to launch browser: {e}")

def test_python_version():
    """Test Python version compatibility"""
    version = sys.version_info
    assert version.major == 3
    assert version.minor >= 8
    print(f"✅ Python version {version.major}.{version.minor}.{version.micro} is compatible")

def test_required_modules():
    """Test that all required modules are available"""
    required_modules = [
        'selenium',
        'playwright',
        'pytest'
    ]
    
    for module in required_modules:
        try:
            __import__(module)
            print(f"✅ {module} module available")
        except ImportError:
            pytest.fail(f"Required module {module} is not available")

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
