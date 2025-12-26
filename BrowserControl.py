from playwright.sync_api import Page, sync_playwright

def runBrowser():
    pw = sync_playwright().start()
    browser = pw.chromium.launch(executable_path="C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe",headless=False)
    page = browser.new_page()
    
    return pw, browser, page
        
def openNext(page, target):
    path = target.replace(" ", "_")
    
    page.goto(f"https://en.wikipedia.org/wiki/{path}") 
    