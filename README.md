# 🥝 Kiwi.com Test Automation Project

This project is a test automation framework developed to validate the core user scenarios on the **Kiwi.com ([www.kiwi.com/en/](http://www.kiwi.com/en/))** website. The framework is built using **Python** with a modern stack, adhering to the **Page Object Model (POM)** and **Behavior-Driven Development (BDD)** principles.

---

## 🚀 Project Goal and Scope

The primary goal of this project is to build a scalable and maintainable test automation solution for Kiwi.com. The scope covers the following key technical requirements and user flows:

1.  **Build a Page Object Model (POM)** for the Kiwi.com homepage.
2.  Utilize the POM within **Gherkin step definitions** to create readable and reusable tests.
3.  Implement the step definitions using **Python**, **Pytest**, and **Playwright**.
4.  Demonstrate how to run a **specific test case** from a larger suite.
5.  Provide a clear list of **dependencies** required to run the project.
6.  Containerize the application using **Docker** to ensure a consistent test environment.
7.  Integrate the tests into a **CI/CD pipeline** for automated execution.

---

## ✨ Technologies and Architecture

| Area                  | Technology / Principle       | Description                                                              |
| --------------------- | ---------------------------- | ------------------------------------------------------------------------ |
| **Programming Language**  | Python 3.11+                 | The core language for test script development.                           |
| **Test Framework**        | Pytest                       | A powerful framework for organizing, running, and reporting on tests.    |
| **UI Automation Tool**    | Playwright                   | For modern, fast, and reliable browser automation and interaction.       |
| **BDD Framework**         | Pytest-BDD                   | Enables writing tests in Gherkin syntax (`.feature` files).              |
| **Architecture**          | Page Object Model (POM)      | Encapsulates page-specific locators and methods for reusability.         |
| **Containerization**      | Docker                       | Ensures a consistent and isolated environment for running tests.         |
| **CI/CD Integration**     | GitHub Actions               | Automates test execution on code changes and allows for manual runs.     |
| **Dependency Management** | pip / `requirements.txt`     | Manages all required Python packages.                                    |


---

## 📁 Project Structure

The project follows a standard BDD and POM structure, separating features, page objects, and step definitions for clarity and maintainability.

```
kiwi-playwright-python/
├── .github/
│   └── workflows/
│       └── ci.yml             # GitHub Actions CI/CD workflow
├── features/
│   └── basic_search.feature   # Test scenarios in Gherkin
├── pages/
│   └── home_page.py           # POM for the Homepage
├── step_definitions/
│   └── basic_search_steps.py  # Step implementations
├── tests/
│   └── test_basic_search.py   # Pytest test runner file
├── .gitignore
├── conftest.py                # Pytest fixtures and configuration
├── Dockerfile                 # Docker configuration for the test environment
├── pytest.ini                 # Pytest configuration (paths, logging)
├── README.md
└── requirements.txt           # Python dependencies
```

---

## 🛠️ Setup and Execution

### Prerequisites

-   Python 3.11+
-   Docker Desktop
-   An IDE of your choice (e.g., VS Code, PyCharm).

### Installation

1.  **Clone the Repository**
    
    ```bash
      git clone <your-repository-url>
      cd kiwi-playwright-python
    ```
    
2.  **Create virtual environment**:
    
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # Linux/Mac
    #.venvScriptsactivate  # Windows
    ```
    
3.  **Install dependencies**:
    
    ```bash
    pip install -r requirements.txt
    ```
    
4.  **Install Playwright browsers**:
    
    ```bash
    playwright install
    ```
    

# 🚀 Running Tests

Once the installation is complete, you can run the tests using any of the following methods.

### Method 1: Running Locally

These commands are run directly in your terminal after activating the virtual environment.

**1. Run in Headed Mode (Default, with browser UI):**

-   **To run all tests:**
    
    ```bash
    pytest
    ```
    
-   **To run a specific test suite (e.g., `T1`):**
    
    ```bash
    pytest -m T1
    ```
    

**2. Run in Headless Mode (No browser UI):**

-   **To run all tests:**
    
    ```bash
    pytest --headless
    ```
    
-   **To run a specific test suite (e.g., `T1`):**
    
    ```bash
    pytest -m T1 --headless
    ```
    

### Method 2: Running via Docker

This method uses the project's `Dockerfile` and does not require a local Python environment, only a running Docker Desktop.

**1. Build the Docker Image (only needs to be done once):**

```bash
  docker build . -t kiwi-tests
```

**2. Run Tests Inside the Container:** The container automatically runs tests in `headless` mode.

-   **To run all tests:**
    
    ```bash
    docker run -e DOCKER_RUN=true --rm kiwi-tests pytest
    ```
    
-   **To run a specific test suite (e.g., `T1`):**
    
    ```bash
    docker run -e DOCKER_RUN=true --rm kiwi-tests pytest -m T1
    ```
    

---

## 🧱 Architectural and Task-Specific Details

### How to Invoke a Specific Test Case

To run a specific test case from a suite of 100, we use **Pytest's native marking system** directly on the test runner function. This provides a robust and Python-centric way to categorize tests.

1.  **Mark the Test Function:** In the `tests/test_basic_search.py` file, the test function is decorated with a Pytest marker.
    
    ```python
    import pytest
    from pytest_bdd import scenario
    
    @pytest.mark.T1
    @scenario(feature_name="../features/basic_search.feature", scenario_name="T1 - One way flight search")
    def test_basic_search():
        pass
    ```
    
2.  **Invoke with `-m` flag:** Use the `-m` flag with `pytest` to run only the tests matching the marker. This command is passed to Docker to execute inside the container.
    
    ```bash
    # This command runs only the tests marked with T1
    pytest -m T1
    ```
    

### List of Dependencies

All required Python packages are listed in `requirements.txt`. Key dependencies include:

-   `pytest`
-   `playwright`
-   `pytest-bdd`
-   `pytest-playwright`

### Docker Environment

The project is fully containerized. The `Dockerfile` sets up a complete, isolated environment with Python, all dependencies from `requirements.txt`, and the necessary Playwright browsers. This guarantees that the tests run identically on any machine, solving the "it works on my machine" problem. The `conftest.py` file detects if it's running inside Docker (via the `DOCKER_RUN` environment variable) and automatically switches to `headless` mode.

### CI/CD Integration with GitHub Actions

The project includes a sophisticated CI/CD pipeline defined in `.github/workflows/ci.yml`. This workflow provides a hybrid approach:

1.  **Automated Regression:** It automatically runs the **entire test suite** on every `push` or `pull_request` to the `master` branch, ensuring code integrity.
2.  **Manual Control:** It allows anyone with access to the repository to manually trigger a workflow run. This provides an interactive way to run specific test suites on demand.
    -   Navigate to the **Actions** tab in the GitHub repository.
    -   Select the **Kiwi Playwright Python** workflow.
    -   Click the **Run workflow** button.
    -   From the **"Which test suite to run?"** dropdown, choose either `all` (for all tests) or `T1` (for smoke tests).
    -   Click the green **"Run workflow"** button to start the job.

This provides both robust automation for developers and flexible, on-demand execution for QA or for demonstration purposes. Test failure artifacts (traces) are automatically uploaded for easy debugging.