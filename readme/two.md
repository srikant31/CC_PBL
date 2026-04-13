# Python Static Code Analyzer Documentation

## 1.1 Project Overview 
The Python Static Code Analyzer is a professional-grade web application designed to automatically audit Python source code for quality, complexity, and security vulnerabilities. Unlike simple linters, this tool combines Static Analysis (SAST), Dynamic Execution Profiling, and AI-driven Fuzzing to provide a 360-degree view of software health. The application was built using a lightweight framework approach with a Bootstrap/Vanilla JS frontend and a backend powered by Python, Flask, and Abstract Syntax Tree (AST) parsing algorithms.

## 1.2 Purpose of the Testing Report 
This report documents the complete Software Testing lifecycle for the Python Static Code Analyzer project. Its purpose is to: 
*   Define the overall test strategy, objectives, and scope adopted for quality assurance. 
*   Present detailed test plans for each testing level: Unit, Fuzzing (Property-based), Integration/E2E UI, and Security testing. 
*   Record all test cases, execution results, and defect findings. 
*   Demonstrate that the system meets its functional and non-functional requirements to achieve a Zero-Critical-Defect state. 
*   Provide a reliable reference for future maintenance, regression testing, and system enhancements. 

## 1.3 System Context 
The Code Analyzer system processes Python source code payloads dynamically and safely. It provides functionality including: 
*   Real-time structural analysis via AST parsing to identify dead code, unused logic, and deep nesting.
*   A dynamic execution evaluation engine using `memory_profiler` for tracking peak RAM usage and script latency. 
*   Security vulnerability interception against OWASP vectors (e.g. Shell/SQL Injection) using Bandit CLI and custom regex filters. 
*   Mathematical code maintainability grading calculated through the Radon complexity engine.
*   Secure HTTP interactions with content security policy (CSP) enforcement via Flask-Talisman. 

## Attribute Details

| Attribute | Details |
| :--- | :--- |
| **Project Name** | Python Static Code Analyzer |
| **Subject** | Software Testing |
| **Institution** | Bharati Vidyapeeth COE, Pune – 411043 |
| **Tech Stack** | Python, Flask, HTML/CSS (Bootstrap), Vanilla JS |
| **Testing Frameworks** | unittest, Selenium WebDriver, Hypothesis (Fuzzing) |
| **Validation Tools** | ast, pyflakes, memory_profiler, radon, bandit |
| **External Utilities** | webdriver-manager, coverage.py |
| **Report Date** | April 10, 2026 |

## 2. Requirement Analysis & Understanding

### 2.1 Requirement Analysis (Business & Functional Needs)
Requirement Analysis is the foundational process of determining exactly what the end-user needs the software to accomplish before any code is written or tested. We identified the following core requirements:
*   **Need 1 (Code Quality):** Users need a reliable way to determine if their Python code is structurally sound ("clean") or poorly written ("messy"), adhering to industry best practices.
*   **Need 2 (Defect Prevention):** Users must be able to proactively identify "hidden" logical bugs or anti-patterns (such as unreachable code or deep nesting) that could lead to unexpected crashes. 
*   **Need 3 (Application Security):** Users require an automated mechanism to scan their code for critical security flaws (like injection vulnerabilities) to prevent malicious exploitation.
*   **Need 4 (Usability & Accessibility):** The tool must provide a fast, intuitive web interface, allowing developers to paste code and receive immediate, formatted feedback without local installations.
*   **Need 5 (Performance Tracking):** Users need visibility into how dynamically memory-intensive their code is to prevent resource exhaustion in production environments.
*   **Need 6 (Error Handling):** The system must gracefully handle completely invalid, syntactically broken, or malicious inputs without crashing the server.

### 2.2 Requirement Understanding Notes (Technical Mapping)
These notes translate the business needs into concrete, testable technical implementations:
*   **Understanding 1 (Quality):** To measure structural cleanliness, we implement **AST (Abstract Syntax Tree)** parsing to programmatically count unused variables, unused functions, and excessive control-flow nesting.
*   **Understanding 2 (Defects):** To quantify logical complexity and hidden defect risk, we integrate the **Radon** library to calculate the Cyclomatic Complexity score.
*   **Understanding 3 (Security):** To mandate security, we integrate **Bandit** for Static Application Security Testing (SAST). This actively audits the submitted source code for common, high-risk attack patterns to prevent malicious exploitation.
*   **Understanding 4 (Usability):** We build the application using the **Flask** microframework for the backend API and **Bootstrap CSS/Vanilla JS** for a responsive frontend experience.
*   **Understanding 5 (Performance):** We utilize the **memory_profiler** library to dynamically execute code in an isolated sub-process and measure its peak RAM allocation.
*   **Understanding 6 (Resilience):** We wrap core parsing logic in strict `try/except` blocks to catch `SyntaxError` exceptions and generate user-friendly validation messages.

## 3. Test Plan & Strategy

### 3.1 Testing Objectives
The primary objectives of the testing effort for the Python Static Code Analyzer were as follows:
1.  Verify that the backend code parsing algorithms function correctly and accurately calculate quality deductions.
2.  Ensure all security integrations (Bandit/Regex) reliably intercept and flag malicious code payloads (SAST checks).
3.  Validate the accuracy of the Cyclomatic Complexity calculation to confirm it aligns with the Radon library metrics.
4.  Confirm that the memory profiling engine correctly tracks and measures peak RAM consumption during dynamic code execution.
5.  Verify application resilience against erratic or malicious inputs using the Hypothesis property-based fuzz testing framework.
6.  Test system behavior under edge cases such as missing syntax, deeply nested loop structures, and non-ASCII gibberish inputs.
7.  Ensure a reliable end-to-end user experience on the frontend via automated Selenium WebDriver UI regression tests.

### 3.2 Test Scope

#### 3.2.1 In Scope
*   Backend API endpoints and core routing logic (Flask context).
*   Python Abstract Syntax Tree (AST) node traversal parsing functions.
*   Security vulnerability detection logic (Command Subprocess Injection, Data loads).
*   Dynamic performance profiling tracking blocks.
*   Code complexity scoring engine and dynamic "Improvement Tips" generation.
*   Frontend DOM user interface elements (Textareas, Results Rendering mapping, Checkbox states).
*   Edge cases: Syntax boundary errors, malformed procedural streams, zero-byte submission loads.

#### 3.2.2 Out of Scope
*   Global load/stress testing of the live web server under heavy concurrent multi-user traffic.
*   Third-party dynamic database integrations (the system behaves as a strictly stateless API).
*   Mobile-native responsive layout testing (Testing focus strictly on Desktop Chrome environments).
*   Compilation or compatibility support audits for deprecated legacy Python 2.x code blocks.

### 3.3 Multi-Layered Testing Approach
The project adopted a comprehensive, multi-layered testing strategy to ensure maximum coverage across all system components:

| Testing Level | Scope | Tools Used |
| :--- | :--- | :--- |
| **Unit Testing** | Individual parsing logic, AST rules, scoring algorithms | Python `unittest`, `Radon` |
| **Fuzz Testing** | System resilience and API crash-prevention boundaries | `Hypothesis` Framework |
| **Integration Testing** | Testing combinations of parsers and security mechanisms combined | Python `unittest` |
| **UI/UX Testing** | Graphical rendering, DOM form persistence, HTTP state checks | `Selenium WebDriver`, Chrome DevTools |
| **Schema Validation** | SAST evaluation boundary limits of raw user payloads | `Bandit`, Custom Regex AST Checks |
| **Error & Edge Case** | Corrupted inputs, runaway recursive loops, missing syntax | Python `unittest`, `Hypothesis`, Manual |

#### 3.3.1 White-Box vs. Black-Box Testing Methodologies
*   **White-Box Testing (Internal Logic Validation):** Our AST Parsing Tests and backend Unit Tests (`test_analysis.py`) were constructed with full visibility into the source code structure. We specifically designed inputs to trigger specific lines of code and specific mathematical deductions.
    *   *Benefit:* Guarantees that every underlying algorithm and calculation branch executes correctly.
*   **Black-Box Testing (External Behavior Validation):** Our E2E Selenium UI Tests and Property-Based Fuzzing were executed from a purely external perspective. They treat the application as an opaque system, simulating real-world users who have zero knowledge of the backend codebase.
    *   *Benefit:* Proves that the application functions effectively and reliably in an active production environment, regardless of how the internal code is structured.

### 3.4 Test Entry & Exit Criteria

#### 3.4.1 Entry Criteria
*   All static analysis source logic modules are implemented and appropriately version-controlled.
*   The isolated test environment is successfully built running Python 3.10+ alongside standard virtual environments.
*   Required testing and security dependencies (`Bandit`, `radon`, `memory_profiler`, `selenium`) are correctly installed.
*   Automated baseline testing files (e.g. `test_analysis.py`, `test_fuzz.py`, `selenuim test_v2.py`) are pre-configured.

#### 3.4.2 Exit Criteria
*   All required high-priority unit tests and UI test case files have been fully executed with passing checks.
*   No open logic defects leading to backend server termination (HTTP 500) remain unresolved.
*   Fuzz testing sweeps consistently result in graceful UI-level error handling mechanisms instead of backend process death.
*   E2E DOM validation sign-off achieved via verified automated Chrome WebDriver testing sweeps.

### 3.5 Test Deliverables
The following artifacts are produced and maintained as part of this testing strategy:
*   **Test Plan & Strategy Document** (This Report).
*   **Automated Test Scripts** (`test_analysis.py`, `selenuim test_v2.py`, etc.).
*   **Test Execution Bug Reports**.
*   **Consolidated Final Metrics Summary**.

## 4. Test Scenarios & Test Cases
This section outlines the detailed step-by-step test cases executed against the Static Code Analyzer, reflecting a combination of positive functional validations and negative security/error handling validations.

| TC ID | Test Scenario Description | Pre-conditions | Tool Used | Test Steps | Expected Result | Actual Result | Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **TC-001** | **Validate Scoring System:** Submitting perfectly valid, simple code to ensure the baseline grading works. | Web server running.<br>Browser ready. | `Selenium WebDriver` | 1. Navigate to UI.<br>2. Enter basic Python code.<br>3. Check 'Dynamic Profiling'.<br>4. Click Analyze. | UI properly displays "Code Quality Score" of "10.0/10". | System processed the code correctly and returned a perfect score. | **PASS** |
| **TC-002** | **Validate Security Defenses:** Attempt to inject dangerous server commands. | Security scanning active. | `Bandit SAST` | 1. Navigate to UI.<br>2. Input malicious code.<br>3. Check 'Security Scan'.<br>4. Click Analyze. | The system intercepts the input and displays "Security Issues: Shell Injection". | System successfully caught the danger and showed a warning. | **PASS** |
| **TC-003** | **Validate Syntax Error Handling:** Submitting intentionally incomplete code (e.g. missing colon). | Basic application running. | `Selenium WebDriver` | 1. Input broken code.<br>2. Click Analyze. | System catches the mistake and displays the error line without crashing. | System safely paused and provided clear error feedback. | **PASS** |
| **TC-004** | **Validate Code Complexity Rules:** See how the system grades code with too many nested loops. | Complexity module active. | `unittest` / `Radon` | 1. Input code with 5+ nested loops.<br>2. Click Analyze. | The final grade is automatically reduced due to complex code logic. | Grade was safely downgraded from A to D. | **PASS** |
| **TC-005** | **Dead Code Analysis:** Testing a script containing variables that are never actually used. | Static analysis active. | `unittest` / `AST` | 1. Input variables with no usage.<br>2. Click Analyze. | System detects the unused code and prompts: "Remove unused variables". | The unused components were accurately flagged. | **PASS** |
| **TC-006** | **Unpredictable Input Handling:** Blasting the application with random keyboard symbols to test stability. | Automated testing ready. | `Hypothesis` | Send hundreds of randomized text inputs automatically. | System handles the chaotic input safely without causing an internal server crash. | Server remained perfectly stable avoiding any fatal errors. | **PASS** |
| **TC-007** | **Large File Performance:** Test system speed and capability with very long code files. | Performance tracking active. | `memory_profiler` | Submit 500+ lines of Python code. | System analyzes everything without freezing or timing out. | The heavy workload was processed smoothly and rendered accurately. | **PASS** |
| **TC-008** | **Empty Box Validation:** Submitting a completely empty text field. | Input validation active. | `Selenium` / Manual | Click "Analyze" on an empty box. | System stops processing immediately and displays "Please enter code". | The warning accurately blocked the empty submission. | **PASS** |
| **TC-009** | **Special Character Rejection:** System response to completely unreadable non-code symbols. | Text validation active. | `Selenium` / Manual | Input random symbolic arrays and submit. | Quickly rejected as an invalid syntax error. | Safely blocked the unreadable text sequence. | **PASS** |
| **TC-010** | **UI Form Memory:** Verifying that checkboxes stay checked after submitting code. | Web interface active. | `Selenium WebDriver` | 1. Select checkboxes.<br>2. Click Analyze.<br>3. Wait for page reload. | Checkboxes automatically remember their selected setup. | UI settings were perfectly preserved after loading. | **PASS** |
| **TC-011** | **Hybrid Analysis Test:** Passing perfectly valid code and a hidden virus at the exact same time. | All scanners active. | Hybrid SAST / Manual | Input a valid math function that also triggers an exploit. | System calculates the code grade while successfully firing a high-alert security warning. | Both the scoring and security systems worked cooperatively. | **PASS** |

## 5. Defect Log & Resolutions
During the multi-layered testing phases, automation scripts uncovered several critical paths requiring remediation. The log below details the discovery context, user impact, and the final engineering resolution implemented to secure the release.

| Bug ID | Title | Severity | Phase | Steps to Reproduce | Expected Result | Actual Result | Resolution | Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **BUG-01** | Unexpected Input Crash in AST Parser | High | Fuzz Testing | Submit Python code with syntax error (e.g., missing colon) | System should return a validation error message | Server crashes with HTTP 500 error | Wrapped `ast.parse()` in try/except to handle `SyntaxError` and return user-friendly message | Fixed |
| **BUG-02** | XSS Vulnerability | Critical | Manual Review | Submit `<script>alert(1)</script>` | Script should be escaped | Script executed in browser | Identified via internal review. Resolved by enabling Jinja2 HTML auto-escaping. | Fixed |
| **BUG-03** | Hardcoded WebDriver Path Issue | Medium | E2E Testing | Run test suite on a different computer | Tests should run on any environment | Tests fail due to missing local driver path | Integrated `webdriver-manager` for dynamic browser driver synchronization | Fixed |
| **BUG-04** | "Clear" Button Failure | Low | UI Testing | Type code and click the "Clear" button | Textbox should be wiped clean | Text remains in the box | Corrected the JavaScript event listener to properly reset the textarea value | Fixed |
| **BUG-05** | False Positive Complexity Warning | Medium | Unit Testing | Submit simple code like `print("Hello World")` | No complexity warnings should appear | System labeled simple code as "Moderately Complex" | Adjusted the Radon complexity threshold to ignore baseline procedural lines | Fixed |

## 6. Requirements Traceability Matrix (RTM)
The Traceability Matrix connects every business and technical requirement to the test cases that prove the requirement was successfully met functionality.

| Req ID | Business/Technical Requirement | Test Case ID Mapped | Verification Method | Execution Status |
| :--- | :--- | :--- | :--- | :--- |
| **REQ-01** | Structural Code Parsing | TC-003, TC-005, TC-008, TC-009 | Unit Testing / E2E / Edge Cases | Passed & Deployed |
| **REQ-02** | Quality Scoring Algorithm | TC-001 | Unit Testing / E2E Testing | Passed & Deployed |
| **REQ-03** | Cyclomatic Complexity Check | TC-004 | Unit Testing / E2E Testing | Passed & Deployed |
| **REQ-04** | Security Scanning Defense | TC-002, TC-011 | SAST / Hybrid Testing | Passed & Deployed |
| **REQ-05** | Backend Stability & Speed | TC-006, TC-007 | Fuzzing / Performance Testing | Passed & Deployed |
| **REQ-06** | UI Usability & Error Trapping | TC-001 to TC-006, TC-010, TC-011 | Selenium WebDriver / Manual | Passed & Deployed |

## 7. Automated Test Suites Summary

### 7.1 Unit Testing
* **Description:** Testing individual backend functions (scoring algorithm, AST parser, security scanner) in **complete isolation** from the Flask web interface. Each function is invoked programmatically with controlled inputs and the output is verified against expected values.
* **Tool:** Python `unittest` framework.
* **Script:** `test_analysis.py` (6 test cases)
* **Test Cases Covered:**
  * `test_unused_variables` — Verifies AST detection of unused variable assignments.
  * `test_unused_functions` — Verifies AST detection of defined-but-never-called functions.
  * `test_complexity` — Verifies Radon cyclomatic complexity calculation.
  * `test_broad_exceptions` — Verifies regex detection of dangerous `except Exception:` patterns.
  * `test_security_scanner_isolated` — Verifies Shell Injection detection in isolation.
  * `test_calculate_score_logic` — Verifies the mathematical scoring deduction algorithm with mock data.
* **Command:**
  ```bash
  python -m unittest test_analysis.py
  ```

---

### 7.2 Fuzz Testing (Property-Based Testing)
* **Description:** Instead of manually writing test inputs, the **Hypothesis** library automatically generates 100+ randomized, corrupted, and adversarial string payloads (including Unicode, emojis, null bytes, and empty strings) and fires them at the `analyze_code()` backend to ensure it **never crashes** with an unhandled exception.
* **Tool:** `Hypothesis` (Property-Based Fuzzing Framework).
* **Script:** `test_fuzz.py` (100 automated iterations)
* **Key Assertion:** The function must always return a valid Python `dict` object — no HTTP 500 errors, no memory leaks, no infinite hangs.
* **Command:**
  ```bash
  python test_fuzz.py
  ```

---

### 7.3 End-to-End (E2E) UI Testing
* **Description:** Automated browser-based testing that simulates a **real human user** interacting with the live Flask website. Selenium WebDriver opens Chrome, types Python code into the textarea, clicks buttons, and verifies that the correct results appear in the HTML DOM.
* **Tool:** `Selenium WebDriver` + `webdriver-manager`.
* **Script:** `selenuim test_v2.py` (**10 Success/Failure Scenarios**)
* **Unique UI Test Cases Covered:**
  1. `test_basic_code_analysis` — Verifies 10.0/10 score for valid code.
  2. `test_security_vulnerabilities` — Verifies detection of Shell Injection alerts.
  3. `test_code_with_syntax_error` — Verifies graceful error messages for typos.
  4. `test_code_without_function` — Verifies logic for non-function procedural code.
  5. `test_code_with_recursion` — Verifies AST handling of recursive calls.
  6. `test_code_with_large_input` — Verifies performance monitoring for heavy math.
  7. `test_hidden_debug_route` — Verifies identification of information disclosure risks.
  8. `test_improvement_tips_logic` — Verifies concurrent display of multiple optimization tips.
  9. `test_form_state_persistence` — Verifies checkbox stability after form submission.
  10. `test_malformed_input_graceful_failure` — Verifies resilience against non-Python gibberish.
* **Pre-requisite:** Flask server must be running at `http://127.0.0.1:5000`.
* **Command:** `python "selenuim test_v2.py"`

---

## 8. Conclusion
We have successfully completed all planned testing phases for the Python Static Code Analyzer, spanning from granular AST unit tests to massive property-based fuzzing and E2E UI automation. The application has definitively proven its resilience against adversarial or corrupted payloads, gracefully intercepting syntax anomalies without triggering HTTP 500 server crashes. Furthermore, the integration of advanced QA methodologies—including Static Application Security Testing (SAST) via Bandit and real-time execution telemetry—ensures that the underlying scoring algorithms are both mathematically sound and enterprise-secure. Following the successful execution of 128+ combined validation sequences, the software meets all functional and non-functional requirements and is considered officially **Stable and Release Ready** for academic and professional evaluation.
