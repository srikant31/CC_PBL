import unittest
from hypothesis import given, settings, strategies as st
from app import analyze_code

class FuzzTestAnalyzer(unittest.TestCase):
    
    # 💥 Fuzz Testing Engine (Property-Based Fuzzing)
    # Instead of human-written code like "a = 10", Hypothesis will automatically 
    # algorithmically blast 100 completely randomized, corrupted, garbage strings 
    # (like "a = \n \000\n", emoji combinations, and weird network artifacts) at your backend.
    
    @settings(max_examples=100) # Number of corrupted mutations to fire
    @given(st.text()) # Strategy: Generate random unicode text payloads
    def test_fuzz_analyze_code_stability(self, random_garbage_string):
        """Fuzz test: Does the AST parser crash when fed unpredictable garbage?"""
        
        # The AST parser should gracefully catch exceptions and return a clean dictionary
        # instead of throwing a massive internal HTTP 500 server crash, memory leak,
        # or hanging infinitely on unexpected inputs.
        print(f"\n[FUZZING IN PROGRESS] Injecting malicious payload: {repr(random_garbage_string)}")
        result = analyze_code(random_garbage_string)
        
        # 1. Assert the application reliably returns a standard Dictionary object
        # no matter what chaotic garbage the virtual user injected.
        self.assertIsInstance(result, dict)
        
        # 2. Assert logic routing: If the garbage string wasn't valid Python code,
        # the system must have securely handled the crash and returned the 'error' key.
        if 'error' not in result:
             # 2. Assert logic routing: If the code was valid, it should at least
             # have a final score (even if it's a perfect 10.0)
             self.assertIn('score', result)

if __name__ == '__main__':
    unittest.main()
