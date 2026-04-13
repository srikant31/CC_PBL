import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

class CodeAnalyzerAdvancedUITest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Using ChromeDriverManager to automatically install and match the driver version
        
        # Chrome options
        options = Options()
        # options.add_argument("--headless")  # Keeping it visible!
        options.add_argument("--window-size=1200,800")

        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    def setUp(self):
        # 5. Refresh the Page Automatically
        # This guarantees every single test starts with a completely fresh, reloaded webpage.
        self.driver.get("http://127.0.0.1:5000/")
        time.sleep(1) # Let the page load

    def test_basic_code_analysis(self):
        driver = self.driver

        sample_code = '''def add(a, b):\n    return a + b\nadd(2, 3)'''

        textarea = driver.find_element(By.ID, "code")
        textarea.clear()
        textarea.send_keys(sample_code)

        checkbox = driver.find_element(By.ID, "dynamic")
        if not checkbox.is_selected():
            checkbox.click()

        submit = driver.find_element(By.XPATH, '//button[@type="submit"]')
        submit.click()

        time.sleep(2)

        result_div = driver.find_element(By.CLASS_NAME, "result-section")
        
        # 4. Much Stricter Assertions
        # Verifying the exact name AND the quality score separately for robustness
        self.assertIn("add", result_div.text)  
        self.assertIn("Code Quality Score", result_div.text)
        self.assertIn("10.0/10", result_div.text)

        print("\n[PASS] Basic Analysis Test Passed. Perfect Score Confirmed.")

    def test_security_vulnerabilities(self):
        # 1. Test the "Security Scan" Checkbox
        driver = self.driver

        # Dangerous hacker code that injects shell commands
        sample_code = "import subprocess\nsubprocess.run(['ls', '-l'], shell=True)"

        textarea = driver.find_element(By.ID, "code")
        textarea.clear()
        textarea.send_keys(sample_code)

        # Tick the "Security Check" box instead of the Dynamic box
        security_checkbox = driver.find_element(By.ID, "security")
        if not security_checkbox.is_selected():
            security_checkbox.click()

        submit = driver.find_element(By.XPATH, '//button[@type="submit"]')
        submit.click()

        time.sleep(2)

        result_div = driver.find_element(By.CLASS_NAME, "result-section")
        
        # Assert that the warning context appears
        self.assertIn("Security Issues:", result_div.text)
        self.assertIn("Shell Injection", result_div.text)

        print("\n[PASS] Security Analysis Test Passed. Vulnerability Caught.")

    def test_code_with_syntax_error(self):
        driver = self.driver
        sample_code = '''def subtract(a, b)\n    return a - b\nsubtract(5, 3)'''

        textarea = driver.find_element(By.ID, "code")
        textarea.clear()
        textarea.send_keys(sample_code)

        submit = driver.find_element(By.XPATH, '//button[@type="submit"]')
        submit.click()

        time.sleep(2)

        result_div = driver.find_element(By.CLASS_NAME, "result-section")
        self.assertIn("expected ':' on line 1", result_div.text)  

        print("\n[PASS] Syntax Error Test Passed.")

    def test_code_without_function(self):
        driver = self.driver
        sample_code = '''print("Hello World!")'''

        textarea = driver.find_element(By.ID, "code")
        textarea.clear()
        textarea.send_keys(sample_code)

        submit = driver.find_element(By.XPATH, '//button[@type="submit"]')
        submit.click()

        time.sleep(2)

        result_div = driver.find_element(By.CLASS_NAME, "result-section")
        self.assertIn("Code Quality Score", result_div.text)
        self.assertIn("10.0/10", result_div.text)

        print("\n[PASS] No Function Test Passed.")

    def test_code_with_recursion(self):
        driver = self.driver
        sample_code = '''def factorial(n):\n    if n == 0:\n        return 1\n    return n * factorial(n - 1)\nfactorial(5)'''

        textarea = driver.find_element(By.ID, "code")
        textarea.clear()
        textarea.send_keys(sample_code)

        submit = driver.find_element(By.XPATH, '//button[@type="submit"]')
        submit.click()

        time.sleep(2)

        result_div = driver.find_element(By.CLASS_NAME, "result-section")
        self.assertIn("factorial", result_div.text)  
        self.assertIn("Code Quality Score", result_div.text)
        self.assertIn("10.0/10", result_div.text)

        print("\n[PASS] Recursion Test Passed.")

    def test_code_with_large_input(self):
        driver = self.driver
        sample_code = '''def sum_numbers(n):\n    return sum(range(n))\nsum_numbers(1000000)'''

        textarea = driver.find_element(By.ID, "code")
        textarea.clear()
        textarea.send_keys(sample_code)

        checkbox = driver.find_element(By.ID, "dynamic")
        if not checkbox.is_selected():
            checkbox.click()

        submit = driver.find_element(By.XPATH, '//button[@type="submit"]')
        submit.click()

        time.sleep(2)

        result_div = driver.find_element(By.CLASS_NAME, "result-section")
        self.assertIn("sum_numbers", result_div.text)  

        print("\n[PASS] Large Input Performance Test Passed.")

    def test_hidden_debug_route(self):
        """[ADVANCED] Test for Information Disclosure vulnerability at /debug"""
        driver = self.driver
        driver.get("http://127.0.0.1:5000/debug")
        
        # Accessing the full page body text
        body_text = driver.find_element(By.TAG_NAME, "body").text
        
        self.assertIn("[SECURITY VULNERABILITY]", body_text)
        self.assertIn("Debug Info", body_text)
        
        print("\n[PASS] Hidden Route Vulnerability Discovered and Verified.")

    def test_improvement_tips_logic(self):
        """[ADVANCED] Test if multiple improvement tips appear for messy code"""
        driver = self.driver
        
        # Code with: 
        # 1. Unused variable (x)
        # 2. Deep nesting (4+ levels)
        messy_code = (
            "def messy_function():\n"
            "    x = 10\n"
            "    if True:\n"
            "        if True:\n"
            "            if True:\n"
            "                if True:\n"
            "                    if True:\n"
            "                        print('Deeply nested')\n"
            "messy_function()"
        )

        textarea = driver.find_element(By.ID, "code")
        textarea.clear()
        textarea.send_keys(messy_code)

        submit = driver.find_element(By.XPATH, '//button[@type="submit"]')
        submit.click()

        time.sleep(2)

        result_div = driver.find_element(By.CLASS_NAME, "result-section")
        
        # Check for specific tips generated in app.py
        self.assertIn("💡 Remove unused variables", result_div.text)
        self.assertIn("💡 Refactor deeply nested code", result_div.text)

        print("\n[PASS] Improvement Tips Logic Verified.")

    def test_form_state_persistence(self):
        """[ADVANCED] Test if checkboxes stay selected after submitting form"""
        driver = self.driver
        
        dynamic_check = driver.find_element(By.ID, "dynamic")
        security_check = driver.find_element(By.ID, "security")

        # Select both
        if not dynamic_check.is_selected(): dynamic_check.click()
        if not security_check.is_selected(): security_check.click()

        submit = driver.find_element(By.XPATH, '//button[@type="submit"]')
        submit.click()

        time.sleep(2)

        # Re-locate elements after page reload
        dynamic_check = driver.find_element(By.ID, "dynamic")
        security_check = driver.find_element(By.ID, "security")

        self.assertTrue(dynamic_check.is_selected(), "Dynamic checkbox should stay checked")
        self.assertTrue(security_check.is_selected(), "Security checkbox should stay checked")

        print("\n[PASS] Form State Persistence Verified.")

    def test_malformed_input_graceful_failure(self):
        """[ADVANCED] Test UI handling of non-python malformed input"""
        driver = self.driver
        
        bad_input = "THIS IS NOT PYTHON !!! @#$%^"

        textarea = driver.find_element(By.ID, "code")
        textarea.clear()
        textarea.send_keys(bad_input)

        submit = driver.find_element(By.XPATH, '//button[@type="submit"]')
        submit.click()

        time.sleep(2)

        result_div = driver.find_element(By.CLASS_NAME, "result-section")
        
        # Verify it shows a syntax error returned by the backend
        self.assertIn("❌ Syntax Error", result_div.text)

        print("\n[PASS] Malformed Input Error Handling Verified.")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
