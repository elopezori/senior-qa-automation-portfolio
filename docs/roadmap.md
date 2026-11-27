# Roadmap — Senior QA Automation Portfolio

## 1. Core Projects

- [ ] Complete professional profile and links in the main README.

- [x] Implement Selenium WebDriver automation framework with C#.
  - [x] Create initial framework structure.
  - [x] Implement Page Object Model.
  - [x] Configure Chrome, Edge and Firefox WebDrivers.
  - [x] Implement explicit waits.
  - [x] Implement NUnit test execution.
  - [x] Implement automatic screenshot capture on test failure.
  - [x] Successfully build and execute the test suite on Windows.
  - [x] Validate automatic screenshot capture with an intentionally failing test.
  - [x] Review and validate Allure reporting integration.
  - [x] Verify screenshot attachments in NUnit and Allure.
  - [x] Implement configuration management and environment support.
  - [x] Organize automated tests by functional area.
  - [x] Document project architecture and execution instructions.

- [x] Implement initial Playwright for .NET framework.
  - [x] Create initial framework structure.
  - [x] Implement an initial automated test.
  - [x] Successfully build and execute the existing test on Windows.
  - [ ] Review framework architecture and Page Object implementation.
  - [ ] Review reporting and evidence generation.
  - [ ] Expand automated test coverage.

- [ ] Review and complete Playwright with Python framework.
  - [ ] Validate framework structure and configuration.
  - [ ] Review Page Object implementation.
  - [ ] Execute the test suite.
  - [ ] Validate reporting and evidence generation.

- [ ] Review and complete API automation framework with Python, Requests and Pytest.
  - [ ] Review API clients, configuration and schemas.
  - [ ] Validate positive and negative test scenarios.
  - [ ] Execute the test suite.
  - [ ] Review reporting and test evidence.

## 2. API Automation and Documentation

- [ ] Create Postman collection and API documentation.
- [ ] Implement API automated testing with .NET.
- [ ] Document API testing strategy and technical decisions.
- [ ] Add reproducible API test evidence.

## 3. Performance Testing

- [ ] Create a performance testing scenario using Apache JMeter.
- [ ] Define performance objectives and acceptance criteria.
- [ ] Document test execution and results.

## 4. CI/CD and Reporting

- [ ] Integrate automated test execution into Jenkins.
- [ ] Configure test result publication.
- [ ] Integrate automated reporting and evidence collection.
- [ ] Review centralized execution across portfolio projects.

## 5. Documentation and Professional Presentation

- [ ] Add reproducible test evidence.
- [ ] Document architecture and technical decisions (ADRs).
- [ ] Review project READMEs and execution guides.
- [ ] Complete professional profile and relevant links.
- [ ] Prepare a portfolio demonstration for Senior QA Automation interviews.

---

## 6. Windows Validation

### Selenium WebDriver with C#

**Environment:** Windows
**.NET SDK:** 10.0.404

Latest full execution:

- [x] Restore .NET dependencies.
- [x] Build the solution successfully.
- [x] Verify NUnit test discovery.
- [x] Execute the Selenium test suite.
- [x] Validate Chrome execution.
- [x] Validate Edge execution.
- [x] Validate Firefox execution.
- [x] Validate headless execution.
- [x] Validate automatic screenshot capture on test failure.
- [x] Verify screenshot attachments in NUnit and Allure.
- [x] Generate and open the Allure HTML report.

**Latest full execution result:**

- Total tests: 3
- Passed: 3
- Failed: 0
- Skipped: 0

Browsers validated:
- Chrome
- Edge
- Firefox

Test executed: `HomePage_ShouldDisplayCorrectTitle`

**Additional failure validation:**

- [x] Intentionally modified the expected page title to trigger a test failure.
- [x] Confirmed that the screenshot was saved to disk.
- [x] Confirmed that the screenshot was attached to the NUnit result.
- [x] Confirmed that the screenshot was visible in the Allure report.
- [x] Restored the correct expected title.
- [x] Re-executed the full test suite successfully.

### Playwright with .NET

**Environment:** Windows
**.NET SDK:** 10.0.404

Latest execution:

- [x] Restore .NET dependencies.
- [x] Build the solution successfully.
- [x] Verify NUnit test discovery.
- [x] Execute the existing test.
- [x] Confirm that the test passes.

**Execution result:**

- Total tests: 1
- Passed: 1
- Failed: 0
- Skipped: 0

Test executed: `LoginPage_ShouldDisplayCorrectTitle`

---

## 7. Pending Validation on macOS

The Selenium framework was initially affected by Windows Smart App Control, which blocked the NUnit test adapter DLL with error `0x800711C7` on the corporate Windows machine.

The corporate security restrictions must not be disabled or bypassed.

The Selenium test suite was subsequently executed successfully on Windows.

Validation on the personal Mac remains pending:

- [ ] Clone or update the repository on macOS.
- [ ] Restore .NET dependencies.
- [ ] Run the Selenium test suite using `dotnet test`.
- [ ] Verify that NUnit discovers and executes all tests.
- [ ] Validate automatic screenshot capture when a test fails.
- [ ] Document the validation results.

**Note:** Automatic screenshot capture has been implemented and verified on Windows using an intentionally failing test. Validation on macOS remains pending.

---

## 8. Current Priorities

The next development steps should follow this order:

1. Complete the initial review of Playwright for .NET.
2. Validate Playwright with Python.
3. Validate API automation with Python.
4. Prioritize architecture improvements and additional test coverage.
5. Continue with API automation using .NET, JMeter and Jenkins.

**Development principle:** Existing functionality should be reviewed and validated before introducing new features. Avoid unnecessary rewrites and preserve working implementations.

---

**Senior QA Automation Portfolio**

Roadmap de desarrollo, validación y evolución técnica del portfolio.