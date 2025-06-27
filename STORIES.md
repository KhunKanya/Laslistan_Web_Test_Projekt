# 🛒 Laslistan E-commerce Test Automation  
**End-to-End Testing for Swedish Online Grocery Platform**  
[![Playwright](https://img.shields.io/badge/Playwright-2.4+-45ba4b?logo=playwright)](https://playwright.dev)
[![Behave](https://img.shields.io/badge/Behave-1.2.7-green)](https://behave.readthedocs.io/)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://python.org)
[![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-CI/CD-black?logo=githubactions)](https://github.com/features/actions)

Comprehensive test automation solution for [Laslistan.se](https://www.laslistan.se/), Sweden's grocery e-commerce platform. Validates critical user journeys using industry-standard BDD methodology and Page Object Model design.

## 🌐 Application Under Test
**[Laslistan Production Environment](https://www.laslistan.se/)**  
*Real-world testing of Sweden's grocery e-commerce platform including:*
- User authentication workflows
- Product search and filtering
- Shopping cart management
- Checkout process
- Order history validation

## 🔍 Test Coverage Overview
| Module           | Test Cases | Status |
|------------------|------------|--------|
| User Authentication | 12        | ✅     |
| Product Search     | 15        | ✅     |
| Cart Management    | 10        | ✅     |
| Checkout Process   | 8         | ✅     |
| Order History      | 5         | ✅     |
| **Total**          | **50**    |        |

## 🛠️ Technology Stack
| Component          | Technology              |
|--------------------|-------------------------|
| Test Framework     | Behave (BDD)            |
| Browser Automation | Playwright              |
| Language           | Python 3.10+            |
| CI/CD              | GitHub Actions          |
| Reporting          | Allure Reports          |
| Test Data          | JSON Parameterization   |

## ⚙️ One-Click Setup & Execution
```bash
# 1. Clone repository
git clone https://github.com/KhunKanya/Laslistan_Web_Test_Projekt.git
cd Laslistan_Web_Test_Projekt

# 2. Install dependencies
pip install -r requirements.txt

# 3. Install Playwright browsers
playwright install

# 4. Run all tests (headless)
behave

# 5. Run with Allure reporting
behave -f allure_behave.formatter:AllureFormatter -o reports/ && allure serve reports/

```

```gherkin
# features/product_search.feature
Feature: Product Search
  Scenario: Filter organic products
    Given I'm on the homepage
    When I search for "mjölk"
    And I apply "Ekologisk" filter
    Then only organic milk products should be shown

# features/checkout.feature  
Feature: Checkout Process
  Scenario: Guest checkout
    Given I have added "Kung Markatta Soya" to cart
    When I checkout as guest with:
      | Field         | Value              |
      | Email         | test@example.com   |
      | Payment Method| Swish              |
    Then I should see order confirmation
```


