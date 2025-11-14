# SauceDemo Automation Project

This repository contains a full-stack QA automation framework featuring:

* **Frontend (FE)** automation using Playwright + Python + BDD
* **Backend (BE)** API layer that wraps Playwright actions into clean REST endpoints
* **End-to-end workflow**: login → get product → add to cart → checkout → finish order
* **Logging and screenshot support** for debugging and reporting

---

#  Project Structure

```
SauceDemo/
│
├── be/                     # Backend API service
│   ├── main.py             # FastAPI app
│   ├── services/           # Playwright logic
│   │   └── sauce_service.py
│   ├── api_tests/          # Manual test requests
│   │   └── test_api_calls.py
│   ├── logs/               # Logging output (auto-generated)
│   └── screenshots/        # Screenshot captures (auto-generated)
│
├── fe/                     # Frontend automation
│   ├── features/           # Gherkin scenarios
│   ├── steps/              # Step definitions
│   ├── pages/              # Page Object Models
│   ├── logs/               # FE logs
│   └── screenshots/        # FE screenshots
│
└── README.md               # This documentation
```

---

# 🚀 Backend (BE) – API Automation Layer

The backend wraps Playwright browser actions into API endpoints so tests can:

* Login
* Retrieve product data
* Add products to cart
* Checkout
* Trigger full end-to-end automation **via HTTP calls**

## ️ Run the Backend

```
cd be
uvicorn be.main:app --port 8000
```

Open Swagger UI:

```
http://127.0.0.1:8000/docs
```

##  API Endpoints

### **POST /login**

Logs in with SauceDemo credentials.

### **GET /product/{name}**

Returns product title, description, price.

### **POST /cart/{item_name}**

Adds the product to cart.

### **POST /checkout/{item_name}?first=John&last=Doe&zip=11111**

Performs the full checkout flow and completes purchase.

---

#  Backend Testing

Use the provided test runner:

```
python be/api_tests/test_api_calls.py
```

This runs:
✔ Login
✔ Product lookup
✔ Add to cart
✔ Checkout

---

#  Logging (BE)

Logs are automatically saved to:

```
be/logs/api.log
```

BE logging includes:

* Request start/end
* Playwright navigation
* Errors, exceptions
* Checkout flow steps

---

#  Screenshots (BE)

Screenshots for debugging are saved in:

```
be/screenshots/
```

Captured on:

* Failed selector waits
* Failed navigations
* Checkout errors

---

#  Frontend (FE) – Playwright BDD Framework

The FE folder contains:

* **Gherkin feature files**
* **Step definitions**
* **Page Object Model (POM)** implementation using Playwright

## ▶ Run FE Tests

Your frontend automation uses **Behave (Cucumber BDD)**, not pytest.

Run **all scenarios**:

```
behave
```

Run **a specific feature**:

```
behave features/purchase.feature
```

Run **headed mode** (visible browser):

```
behave -D headed=true
```

Run **headless mode**:

```
behave -D headed=false
```

---

#  Screenshots (FE)

Screenshots are automatically saved inside:

```
fe/screenshots/
```

Used for debugging failed scenarios.

```
Used for debugging failed scenarios.

---

#  BE + FE Integration
This project demonstrates **full-stack QA automation**:
- BE provides a stable automation API layer powered by Playwright
- FE uses Playwright directly for visual/UI flow testing
- Both layers share consistent selectors and structure

Interviewers love this because it demonstrates:
- API architecture
- Async Playwright usage
- Maintainable code patterns
- Full automation understanding

---

#  Final Notes
Your project is now:
- Interview-ready
- Portfolio-ready
- Full end-to-end automated
- Organized with clean structure, logs, and screenshots

If you want next steps:
- CI/CD with GitHub Actions
- Reporting (Allure, HTML test reports)
- Dockerization
- Mocking backend with pytest
- Load testing

Just ask!

```