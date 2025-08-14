from playwright.sync_api import sync_playwright
import time

def open_gmail():
    with sync_playwright() as p:
        # Launch browser (you can change 'chromium' to 'firefox' or 'webkit')
        browser = p.chromium.launch(headless=False)  # Set headless=True to run without UI
        page = browser.new_page()
        
        try:
            # Navigate to Gmail
            print("Opening Gmail...")
            page.goto("https://gmail.com")
            
            # Wait for the page to load
            page.wait_for_load_state("networkidle")
            
            print("Gmail opened successfully!")
            print("Press Enter to close the browser...")
            input()  # Wait for user input before closing
            
        except Exception as e:
            print(f"An error occurred: {e}")
        
        finally:
            # Close the browser
            browser.close()
            print("Browser closed.")

def open_multiple_sites():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        
        # Open multiple tabs
        page1 = browser.new_page()
        page2 = browser.new_page()
        
        try:
            print("Opening multiple sites...")
            
            # Open Gmail in first tab
            page1.goto("https://gmail.com")
            page1.wait_for_load_state("networkidle")
            
            # Open Google in second tab
            page2.goto("https://google.com")
            page2.wait_for_load_state("networkidle")
            
            print("Sites opened successfully!")
            print("Press Enter to close the browser...")
            input()
            
        except Exception as e:
            print(f"An error occurred: {e}")
        
        finally:
            browser.close()
            print("Browser closed.")

if __name__ == "__main__":
    print("Hello, Cursor!")
    print("Choose an option:")
    print("1. Open Gmail only")
    print("2. Open multiple sites (Gmail + Google)")
    
    choice = input("Enter your choice (1 or 2): ")
    
    if choice == "1":
        open_gmail()
    elif choice == "2":
        open_multiple_sites()
    else:
        print("Invalid choice. Opening Gmail by default...")
        open_gmail()