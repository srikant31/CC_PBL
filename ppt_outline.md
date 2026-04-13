# Python Static Code Analyzer - PPT Slide Content (3-4 Bullet Points Per Slide)

---

## SLIDE 1 — TITLE SLIDE

- **Project:** Python Static Code Analyzer — Software Testing Life Cycle Report
- **Subject:** Software Testing
- **Institution:** Bharati Vidyapeeth College of Engineering, Pune - 411043
- **Date:** April 2026

---

## SLIDE 2 — INTRODUCTION

- Python Static Code Analyzer is a professional-grade web application designed to automatically audit Python source code
- Combines Static Analysis (SAST), Dynamic Profiling, and functional parsing to provide a 360-degree view of software health
- Designed to allow developers to paste code and instantly receive a quantifiable "Code Quality Score" based on structural integrity
- This report documents the full Software Testing Life Cycle (STLC) prioritizing error handling, algorithm validation, and crash-resilience

---

## SLIDE 3 — OBJECTIVE

- Verify the built-in mathematical algorithms accurately deduce scores for complex code and structural inefficiencies
- Ensure the SAST engine correctly intercepts malicious code injections and flags them to the user
- Validate the backend logic gracefully handles syntactically broken or randomized "fuzzed" inputs without returning 500 Server Errors
- Confirm all testing phases complete with a 100% pass rate before marking the software ready for production

---

## SLIDE 4 — ABOUT THE APPLICATION

- Provides a centralized web dashboard where developers submit single-file Python scripts for technical feedback
- Calculates McCabe's Cyclomatic Complexity to flag overly nested or difficult-to-maintain code blocks
- Automatically identifies unreachable dead code and unused variables utilizing AST (Abstract Syntax Tree) logic
- Analyzes peak memory and RAM allocation dynamically to ensure the scanned code is resource-efficient

---

## SLIDE 5 — TECHNOLOGY STACK

- **Backend Architecture:** Python 3.10+, Flask 3.0.x (Web Framework)
- **Static Analysis Core:** Python `ast` library (Abstract Syntax Tree), `memory_profiler`
- **Security Engine:** Bandit v1.7.x (Static Application Security Testing)
- **Testing Suite:** `pytest` (Unit logic), `Hypothesis` v6.x (Fuzzing), Selenium WebDriver v4.x (UI Automation)

---

## SLIDE 6 — SYSTEM ARCHITECTURE

- Follows a modular MVC pattern: Web Requests → Flask Routes → Analysis Engine → JSON Response → UI Rendering
- The **Analysis Engine** breaks down into 4 testable modules: AST Parse, Complexity Score, Security Scan, and Memory Trace.
- The built-in Error Trapping middleware catches all `SyntaxError` states before they fatally crash the Flask server process.
- All testing layers are specifically mapped to test exact segments of this data flow (e.g., Selenium tests the UI, Pytest tests the Engine).

---

## SLIDE 7 — THE RADON ENGINE (COMPLEXITY ANALYSIS)

- *Note: Radon is the Python tool that mathematically computes how complicated code is using McCabe's Cyclomatic Complexity formula.*
- Replaces subjective code reviews by assigning a verifiable mathematical score to logical branches.
- Uses the formula: `M = E - N + 2P` (where E = Edges, N = Nodes, P = Connected Components in the execution path).
- By scoring complexity, our testing suite can write assertions verifying that overly messy code successfully degrades the user's total grade.

---

## SLIDE 8 — TESTING STRATEGY

- **Overall Approach:** A 4-tier testing pyramid was adopted — Unit Testing → Fuzz Testing → SAST (Security) → End-to-End UI Testing — progressing from isolated logic verification to full black-box simulation.
- **Rationale:** Each tier is designed to catch a distinct class of defect: algorithmic errors (Unit), crash vulnerabilities (Fuzz), security flaws (SAST), and UI rendering failures (Selenium).
- **Scope & Boundaries:** Unit and Fuzz tests target the backend engine in complete isolation; Selenium tests exercise the full request-response cycle including the HTML frontend.
- **Entry/Exit Criteria:** Testing begins once the Flask server starts without errors; the phase is closed only when all 128 test cases pass with 0 critical defects open.

---

## SLIDE 9 — WHITE-BOX UNIT TESTING (Pytest)

- **Focus:** Validating the core scoring algorithms and AST tree-walking logic in complete isolation from the web server.
- **Methodology:** Wrote explicit functions testing positive logic (valid code), negative logic (syntax errors), and boundary math.
- **Key Executions (6 Cases):** Automated verification that unused variables are accurately tracked and McCabe's complexity scoring logic penalizes accurately.
- **Why it matters:** Ensures the mathematical foundation of our Analyzer is structurally bulletproof before integrating a user interface.

---

## SLIDE 10 — PROPERTY-BASED FUZZ TESTING (Hypothesis)

- **Focus:** Extreme stress testing to eliminate unexpected server crashes (Internal Server 500 errors).
- **Methodology:** Uses the **Hypothesis** tool as a "bug search engine" to blast the backend parser with 100 randomized payloads (emojis, gibberish strings, massive loop counts).
- **Why it matters:** Human testers only write tests for inputs they *expect*. Fuzzing tests the unpredictable real-world inputs users might paste into the app.
- **Outcome:** Successfully proved the backend `try/except` syntax safeguards handle 100% of malicious garbage inputs without freezing.

---

## SLIDE 11 — STATIC APPLICATION SECURITY TESTING (Bandit)

- **Focus:** White-Box security auditing to locate highly dangerous code vectors.
- **Methodology:** Implemented **Bandit** to scan the AST nodes specifically hunting for security anti-patterns (SAST).
- **Vulnerabilities Tracked:** Successfully intercepts Shell Command Injections (e.g., `os.system()`), SQL Injection structures, and weak cryptographic hashes.
- **Why it matters:** Proves the Analyzer acts as an active defense layer for developers, preventing them from deploying fatal security flaws into their own production environments.

---

## SLIDE 12 — END-TO-END UI TESTING (Selenium)

- **Focus:** Black-box functional validation mimicking a real human interaction.
- **Methodology:** Used **Selenium WebDriver** to automate Google Chrome. It boots the app, types code into the textarea, submits the form, and reads the DOM tree.
- **Key Executions (10 Scenarios):** Verified Bandit alerts paint correctly in red HTML, form state persists on reload, and the 500+ line execution test doesn't lock up the browser.
- **Why it matters:** Proves that the underlying Python backend successfully communicates with the JavaScript/HTML frontend for a flawless user experience.

---

## SLIDE 13 — DEFECT LOG

- **BUG-01 (High):** AST Parser crashed on syntax errors — fixed by wrapping `ast.parse()` in a strict try/except catch block.
- **BUG-02 (Critical):** Application was vulnerable to XSS script execution — fixed by enforcing Jinja2 HTML auto-escaping.
- **BUG-03 (Medium):** Automated UI tests failed on different machines due to hardcoded paths — fixed by integrating `webdriver-manager`.
- **BUG-04 (Low):** UI 'Clear' button did not reset textarea — fixed by correcting the JavaScript reset event listener.
- **BUG-05 (Medium):** Radon engine gave false positive complexity ratings for simple code — fixed by tuning baseline thresholds.
- **Result: 5 defects tracked, 5 resolved, 0 open — 100% resolution rate**

---

## SLIDE 14 — TEST CASES SUMMARY

- **128 automated tests executed across 4 unique testing tiers (Unit, Fuzzing, Security, UI)**
- **Unit & Logic:** 6 assertions proving mathematical scoring and structural deductions.
- **Fuzzing Engine:** 100 Hypothesis property iterations validating system crash immunity.
- **UI & Integration:** 10 Selenium End-to-End assertions validating end-user visual components and data persistence.
- **Performance:** 2 profile executions verifying latency remains under 1.5 seconds.
- **Result: 128 Executed, 128 Passed, 0 Failed — 100% Pass Rate**

---

## SLIDE 15 — REQUIREMENTS TRACEABILITY MATRIX

- RTM proves every business and technical requirement is mathematically verified by a matched test execution — 100% traceability density.
- **REQ-01** (Structural Code Parsing) → TC-003, TC-005, TC-008, TC-009 | **REQ-02** (Quality Scoring Algorithm) → TC-001
- **REQ-03** (Cyclomatic Complexity Check) → TC-004 | **REQ-04** (Security Scanning Defense) → TC-002, TC-011
- **REQ-05** (Backend Stability & Speed) → TC-006, TC-007 | **REQ-06** (UI Usability & Error Trapping) → TC-001 to TC-006, TC-010, TC-011
- **Result: 6 Requirements defined, 6 Verified, 0 Untraced — Full RTM Coverage Achieved**

---

## SLIDE 16 — TEST AUTOMATION SNIPPETS

**Selenium UI Asserts:**
```python
# Verifies the malicious subprocess was blocked and flagged
assert "Security Issues:" in result_text
assert "Shell Injection" in result_text
```

**Hypothesis Fuzzing Engine:**
```python
@given(st.text())
def test_fuzz_analyze_code(fuzzed_code):
    try:
        # Asserts the system never throws an unhandled crash
        analyze_code(fuzzed_code) 
    except SyntaxError:
        pass
```

---

## SLIDE 17 — CONCLUSION & FUTURE ENHANCEMENTS

- **Conclusion:** Completed a highly rigorous STLC blending exploratory testing with 128 multi-layered automation tests.
- Successfully verified algorithmic scoring, fuzz-resilience, exact UI rendering, and SAST monitoring.
- **Project Status:** 0 Open critical bugs remaining — **STABLE & APPROVED FOR PRODUCTION**.
- **Future Enhancements:** Integrating GitHub Actions for CI/CD pipelines to trigger `pytest` and `selenium` workflows on every code push, and utilizing local LLMs to suggest automated code refactoring.
