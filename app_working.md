# 🧠 How the Application Works: Internal Logic & Architecture
**Project:** Python Static Code Analyzer
**Status:** Operational / Documented

---

## 1. High-Level Architecture (The Big Picture)

The application follows a **Client-Server** model. Think of it like a restaurant:
*   **The Client (Bootstrap UI):** This is the "Customer" (your browser). It uses **Bootstrap 5.3** to create a clean, pretty interface where you can paste your Python code.
*   **The Server (Flask):** This is the "Kitchen." It is written in **Flask (Python)**. It sits and waits for you to click "Analyze Code," then it processes the data and sends a "Security Report" back to you.

---

## 2. The Parser (AST): How the App "Reads" Code

Computers don't read code like humans do. To "understand" your code, our app uses a tool called **AST (Abstract Syntax Tree)**. 
*   **What it is:** Instead of seeing plain text, AST turns your code into a **branching tree**.
*   **How it works:** It looks for `FunctionDef` (functions), `Assign` (variables), and `If` statements. By walking through this "tree," our app can count exactly how many variables you used and find ones that you defined but never actually used!

---

## 3. Cyclomatic Complexity Deep Dive (The "Mathematician")

This is one of the most important parts of the app. It measures how "complicated" a function is.

### What is it?
Cyclomatic Complexity is a count of the number of **decision paths** in your code.
- Every `if`, `for`, `while`, and `except` adds +1 to the complexity.
- A score of **1** is a straight line (Simple).
- A score of **10+** is like a maze (Too Complex).

### How we calculate it (The "McCabe Metric")
We use a professional tool called **Radon**. Radon uses the **McCabe Metric**, which is a mathematical formula that looks at the "Control Flow Graph" of your code. It literally counts the number of ways a piece of code can "split" into different directions.

### The Ranking System (A to F)
Our app uses the industry-standard ranking system:
*   **Rank A (1-3):** Very simple, easy to read. (Perfect!)
*   **Rank B (4-5):** Slightly complex but manageable.
*   **Rank C (6-7):** Moderately complex.
*   **Rank D (8-10):** Very complex. (Hard to test!)
*   **Rank E/F (11+):** Extreme complexity. (You should rewrite this!)

---

## 4. The Complete Toolkit (The Libraries we used)

We didn't build everything from scratch; we used **industry-standard tools** to make our analyzer powerful:
1.  **Flask:** The web server that handles requests.
2.  **Radon:** The math engine that calculates **Cyclomatic Complexity**.
3.  **Pyflakes:** A fast tool that looks for **Logic Errors** and syntax warnings.
4.  **Bandit:** A professional **Security Scanner** used by major companies to find vulnerabilities.
5.  **Memory_Profiler:** A tool that tracks how much **RAM (Memory)** your code consumes while it's running.

---

## 5. The Safety Inspector (Security Logic)

The app looks for "Hacker" patterns using two methods:
*   **Bandit (SAST):** It looks at your code file and checks if you used dangerous commands like `eval()` (which can let a hacker run their own code) or `pickle` (which is insecure for data).
*   **Custom RegEx (Pattern Matching):** We wrote our own "Custom Security Rules." For example, if you type `subprocess.run(shell=True)`, our app instantly recognizes that this is a **Shell Injection** risk!

---

## 6. The 0-10 Grading Formula (The "Final Score")

How do we decide if your code is "Good" or "Bad"? We start with a **Perfect 10.0** and subtract points for mistakes:
*   **-0.3 Points:** For every unused function we find.
*   **-0.2 Points:** For every unused variable.
*   **-0.5 Points:** For every deeply nested loop (over 4 levels deep).
*   **-0.4 Points:** For every point of Cyclomatic Complexity above 3.
*   **-0.5 to -1.0 Points:** For excessive Memory Usage (over 100 MiB).
*   **-0.5 Points:** For every Security Vulnerability found.

*The result is rounded and returned as your **Overall Code Quality Score**.*

---

## 7. Performance Profiling (The "Scale")

When you tick the "Include dynamic profiling" box, the app does something special:
1.  **Temporary Execution:** It saves your code to a temporary file.
2.  **Real-Time Tracking:** It runs that code in a separate process while a **Memory Monitor** watches it.
3.  **Data Capture:** It records the **Peak Memory** usage (in MiB) and the **Execution Time** (in seconds), then deletes the temp file safely.

---

## 8. The Feedback Engine (Improvement Tips)

After the analysis is done, the app generates **Actionable Tips**:
- If your complexity is high, it says: *"💡 Break down complex functions into simpler ones."*
- If we find unused vars, it says: *"💡 Remove unused variables to simplify your code."*
- If we find security bugs, it says: *"🔒 Review security findings and address vulnerabilities."*

This ensures that the user doesn't just get a "bad score," but actually knows **how to fix it**.
