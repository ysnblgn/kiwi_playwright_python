import os
import pytest
from playwright.sync_api import sync_playwright
from pages.home_page import HomePage

pytest_plugins = "steps.basic_search_steps"


@pytest.fixture
def home(page) -> HomePage:
    return HomePage(page)


@pytest.fixture(scope="session")
def browser(request):
    env_config = request.config.getoption("--environment", default="local")

    with sync_playwright() as p:
        if os.getenv("DOCKER_RUN"):
            browser = p.chromium.launch(headless=True, args=["--no-sandbox"])
        else:
            browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture
def page(browser):
    user_agent = (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/108.0.0.0 Safari/537.36"
    )
    context = browser.new_context(user_agent=user_agent)
    page = context.new_page()
    yield page
    context.close()
