import pytest
from playwright.sync_api import sync_playwright, Page, Browser, BrowserContext

class TestWebAutomation:
    """Test class for web automation using Playwright"""
    
    @pytest.fixture(scope="class")
    def browser(self):
        """Fixture to set up and tear down browser"""
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            yield browser
            browser.close()
    
    @pytest.fixture
    def page(self, browser):
        """Fixture to create a new page for each test"""
        page = browser.new_page()
        yield page
        page.close()
    
    def test_open_gmail(self, page: Page):
        """Test opening Gmail website"""
        page.goto("https://gmail.com")
        assert page.title() == "Gmail"
        assert page.is_visible("text=Gmail")
        print("✅ Gmail page loaded successfully")
    
    def test_open_google(self, page: Page):
        """Test opening Google website"""
        page.goto("https://google.com")
        assert "Google" in page.title()
        assert page.is_visible("[name='q']")  # Search box
        print("✅ Google page loaded successfully")
    
    def test_gmail_login_form(self, page: Page):
        """Test Gmail login form elements"""
        page.goto("https://gmail.com")
        
        # Check for email input field
        email_input = page.locator("#identifierId")
        assert email_input.is_visible()
        
        # Check for "Next" button
        next_button = page.locator("text=Next")
        assert next_button.is_visible()
        
        print("✅ Gmail login form elements found")
    
    def test_google_search_functionality(self, page: Page):
        """Test Google search functionality"""
        page.goto("https://google.com")
        
        # Find search box and type
        search_box = page.locator("[name='q']")
        search_box.fill("pytest python")
        
        # Press Enter to search
        search_box.press("Enter")
        
        # Wait for results
        page.wait_for_load_state("networkidle")
        
        # Check if results are displayed
        assert page.is_visible("text=pytest")
        print("✅ Google search functionality works")

def test_simple_function():
    """Simple test function to verify pytest is working"""
    assert 2 + 2 == 4
    print("✅ Simple math test passed")

def test_string_operations():
    """Test string operations"""
    text = "Hello, World!"
    assert "Hello" in text
    assert len(text) == 13
    print("✅ String operations test passed")

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
