# 🏗️ Testing Components & Methodologies (Up Till Now)
**Project:** Python Web-Based Static Code Analyzer

This document serves as an architectural index outlining every layer of Quality Assurance (QA) testing currently integrated into the platform, detailing how it functions mechanically, and defining why it is critical for bringing this project to production.

---

## 1. Unit Testing
**What it is:** 
Unit testing is the practice of testing the absolute smallest, most microscopic parts of an application (individual functions, specific math algorithms) in complete isolation from the rest of the system.

**How we did it:** 
We built a dedicated Python `unittest` suite that completely ignores the Flask (`app.py`) web server and the HTML frontend. Instead, it directly imports the `analyze_code()` algorithm and injects raw data strings straight into the memory of the backend, asserting that the dictionary math returns perfect numbers. 

**Why it matters:** 
If the core math is broken, the entire app is useless. Isolating the backend proves mathematically that our Abstract Syntax Tree (AST) parser works flawlessly without getting confused by network latency or HTML CSS bugs.

## 2. Automated End-to-End (E2E) UI Testing
**What it is:** 
Automating an actual web browser to physically interact with the graphical website exactly as a real human user would.

**How we did it:** 
We deployed Google Chrome via the Selenium WebDriver API (`selenuim test_v2.py`). The script boots up an invisible robotic user that locates the HTML text boxes, types in specific Python strings, ticks the "Include dynamic profiling" checkboxes, hits submit, and visually reads the final HTML output div to verify the data rendered correctly on the screen.

**Why it matters:** 
Even if Unit Tests perfectly pass, if the HTML "Submit" button accidentally gets deleted by a frontend developer, the user can't use the app. E2E testing strictly guarantees that the *Frontend* successfully talks to the *Backend*, completing the full user journey.

## 3. Static Application Security Testing (SAST)
**What it is:** 
Scanning raw source code to algorithmically find known vulnerability patterns and severe security flaws before the code is ever allowed to execute on a computer.

**How we did it:** 
We integrated the open-source, industry-standard `bandit` framework into our backend `run_security_scan()` logic. When a user submits code, our server secretly writes it to a temporary `.py` file, boots up the Bandit command-line interface via `subprocess`, parses the code for OWASP Top 10 vulnerabilities (like Shell Injection & SQL Injection), and passes the severity findings back to the screen.

**Why it matters:** 
It protects organizations and developers from running poorly constructed code that hackers could easily exploit to delete databases or steal credentials.

---

## 📁 Specific Testing Files & Their Purpose

When you open the project repository, you will see two very distinct testing files. Here is exactly what they are and why they exist:

### 1. The `test_analysis.py` File
**What is it?** 
The official, production-ready Unit Testing Suite.

**What does it do?** 
It acts as the strict gatekeeper for the backend application logic. It runs 6 isolated mathematical tests in literally 6 milliseconds. It individually tests:
1. That the parser successfully isolates unused variables.
2. That the parser successfully isolates missing or unused functions.
3. That Cyclomatic Complexity is accurately tracked via the `radon` integration.
4. That the AST correctly catches dangerous "Catch-All" exceptions (`except Exception:`).
5. That the `bandit` security scanner actually spots injected `subprocess.run` vulnerabilities.
6. The raw grading execution (Making sure a score of 10.0 mathematically drops down to exactly 7.1 based on simulated logic penalties).


### 2. The `test_radon.py` File
**What is it?** 
A Development Scratchpad / Iterative Prototype File.

**What does it do?** 
Before the web app was ever fully built, this tiny script was created simply to experiment with the complex third-party `radon` library. 
To avoid building a whole Flask website just to see if the library worked, this script fed a fake `def complex_func():` into `radon.complexity` to observe its raw, unformatted JSON score. It was also used to quickly prototype the `get_rank()` function (the logic that translates numbers into A, B, C, F grades). 

Once that prototype code was mechanically proven to work independently inside this isolated scratchpad, the logic was successfully lifted and permanently integrated into the actual `app.py` master file. 

---

## 4. Unsuccessful Testing Explorations (Mutation Testing)
As part of our commitment to rigorous Quality Assurance, we actively attempted to integrate **Mutation Testing** into our pipeline using the open-source `mutmut` framework. 

**The Goal:** Mutation testing algorithmically injects intentional bugs (mutants) into the `app.py` source code and runs `test_analysis.py` to ensure our Unit Tests are strict enough to catch the sabotage. 

**The Limitation:** While we successfully installed the package and configured the test runner, the final execution generated fatal environment errors. `mutmut` heavily relies on the Linux `multiprocessing` library's `fork` mechanism to instantly clone the testing environment into memory thousands of times simultaneously. Because this project was developed on a native Windows machine, which does not support POSIX forking (relying instead on "spawning"), the framework crashed. 

Rather than integrating the slower and overly complex Windows alternative (`cosmic-ray`), we formally documented Mutation Testing as a blocked requirement pending future deployment from our local Windows environment to a standardized Linux Cloud Staging Server.
