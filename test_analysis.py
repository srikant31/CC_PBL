import unittest
from app import analyze_code, run_security_scan, calculate_score

class TestCodeAnalysis(unittest.TestCase):

    def test_unused_variables(self):
        code = "a = 10\nprint('hello')"
        results = analyze_code(code)
        unused = results.get('unused_variables', [])
        self.assertIn('a', unused)

    def test_unused_functions(self):
        code = "def unused(): pass\ndef used(): pass\nused()"
        results = analyze_code(code)
        unused = results.get('unused_functions', [])
        self.assertIn('unused', unused)
        self.assertNotIn('used', unused)

    def test_complexity(self):
        code = "def hello():\n    if True:\n        print('hi')"
        results = analyze_code(code)
        complexity = results.get('complexity', [])
        self.assertTrue(len(complexity) > 0)
        self.assertEqual(complexity[0]['name'], 'hello')

    def test_broad_exceptions(self):
        code = "try:\n    pass\nexcept Exception:\n    pass"
        results = analyze_code(code)
        broad_exceptions = results.get('broad_exceptions', [])
        self.assertTrue(len(broad_exceptions) > 0)
        
        # Verify that it caught the exact text of the exception
        found_broad = any("except Exception:" in warning for warning in broad_exceptions)
        self.assertTrue(found_broad)

    def test_security_scanner_isolated(self):
        code = "import subprocess\nsubprocess.run('ls', shell=True)"
        # Run JUST the security scan isolated from everything else
        issues = run_security_scan(code)
        self.assertTrue(len(issues) > 0)
        
        # Verify it specifically tags Shell Injection
        found_inject = any("Shell Injection" in issue for issue in issues)
        self.assertTrue(found_inject)

    def test_calculate_score_logic(self):
        # We can test the math logic by bypassing the parser entirely
        # and feeding it a fake, mathematically engineered dictionary
        mock_results = {
            'unused_functions': ['foo'],            # Deduction: -0.3
            'unused_variables': ['bar'],            # Deduction: -0.2
            'max_nesting': 5,                       # Deduction: -0.5 (1 level over 4 = 1 * 0.5)
            'avg_complexity': 4,                    # Deduction: -0.4 (1 level over 3 = 1 * 0.4)
            'broad_exceptions': ['except:'],        # Deduction: -0.5
            'peak_memory': 65,                      # Deduction: -0.5 (over 60 MiB)
            'security_issues': ['SQL Injection']    # Deduction: -0.5
        }
        
        expected_score = 10.0 - 0.3 - 0.2 - 0.5 - 0.4 - 0.5 - 0.5 - 0.5 # equals 7.1
        score = calculate_score(mock_results)
        
        # The math function should perfectly equal 7.1
        self.assertEqual(score, round(expected_score, 2))

if __name__ == '__main__':
    unittest.main()
