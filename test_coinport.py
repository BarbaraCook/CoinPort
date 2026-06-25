# test_coinport.py
"""
Tests for CoinPort module.
"""

import unittest
from coinport import CoinPort

class TestCoinPort(unittest.TestCase):
    """Test cases for CoinPort class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CoinPort()
        self.assertIsInstance(instance, CoinPort)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CoinPort()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
