from playwright.sync_api import sync_playwright, Page, Playwright

def prepare_environment(pl: Playwright):
    browser = pl.chromium.launch(headless=False)
    page = browser.new_page()
    return browser, page

def verify_title(page: Page, title_name) -> None:
    assert title_name in page.title(), "Заголовок не совпадает"

def click_link(page: Page, link_text) -> None:
    link = page.locator("a", has_text=link_text)
    assert link.is_visible(), f"Ссылка '{link_text}' не найдена"
    link.click()

def verify_redirect(page: Page, target_url) -> None:
    page.wait_for_url(target_url, timeout=10000)
    assert page.url == target_url, "URL после перехода неверный"

def main() -> None:
    with sync_playwright() as p:
        browser, page = prepare_environment(p)
        page.goto("https://example.com")
        verify_title(page, "Example")
        click_link(page, "More information")
        verify_redirect(page, "https://www.iana.org/help/example-domains")
        browser.close()

if __name__ == "__main__":
    main()