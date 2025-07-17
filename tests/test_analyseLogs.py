import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from analyseLogs import convertData, countRepeats, flagOutliers, printOutliers
from unittest.mock import mock_open, patch

class TestAnalyseLogs(unittest.TestCase):
    def setUp(self):
        self.sample_data = [
            {'ipAddress': '1.1.1.1', 'userAgent': 'A', 'datetime': '01/07/2025:06:00:01', 'httpPath': '/home'},
            {'ipAddress': '1.1.1.1', 'userAgent': 'A', 'datetime': '01/07/2025:06:00:02', 'httpPath': '/search'},
            {'ipAddress': '2.2.2.2', 'userAgent': 'B', 'datetime': '01/07/2025:06:00:03', 'httpPath': '/home'},
            {'ipAddress': '3.3.3.3', 'userAgent': 'A', 'datetime': '01/07/2025:06:00:04', 'httpPath': '/about'},
            {'ipAddress': '1.1.1.1', 'userAgent': 'C', 'datetime': '01/07/2025:06:00:05', 'httpPath': '/contact'},
            {'ipAddress': '2.2.2.2', 'userAgent': 'B', 'datetime': '01/07/2025:06:00:06', 'httpPath': '/search'},
            {'ipAddress': '4.4.4.4', 'userAgent': 'D', 'datetime': '01/07/2025:06:00:07', 'httpPath': '/home'},
            {'ipAddress': '1.1.1.1', 'userAgent': 'A', 'datetime': '01/07/2025:06:00:08', 'httpPath': '/about'},
            {'ipAddress': '2.2.2.2', 'userAgent': 'B', 'datetime': '01/07/2025:06:00:09', 'httpPath': '/contact'},
            {'ipAddress': '3.3.3.3', 'userAgent': 'A', 'datetime': '01/07/2025:06:00:10', 'httpPath': '/search'},
        ]

        self.sample_file = (
            f'1.1.1.1 - US - [01/07/2025:06:00:01 +0000] "GET /home HTTP/1.1" 200 1234 "-" "UserAgentA" 345{os.linesep}'
            '2.2.2.2 - NO - [01/07/2025:06:00:02 +0000] "GET /search HTTP/1.1" 200 1234 "-" "UserAgentA" 210'
        )

    def test_convertData_1(self):
        m = mock_open(read_data=self.sample_file)

        with patch('builtins.open', m):
            result = convertData('example.log')
        self.assertEqual(len(result), 2) # Tests all lines are converted
                         
    def test_countRepeats_1(self):
        result = countRepeats('ipAddress', self.sample_data)
        self.assertEqual(result['1.1.1.1'], 4) # Tests the count for 1.1.1.1 is correct
        self.assertEqual(result['2.2.2.2'], 3) # Tests the count for 2.2.2.2 is correct
        self.assertEqual(result['3.3.3.3'], 2) # Tests the count for 3.3.3.3 is correct
        self.assertEqual(result['4.4.4.4'], 1) # Tests the count for 4.4.4.4 is correct

    def test_flagOutliers_1(self):
        entryCount = {'a': 1, 'b': 10, 'c': 10, 'd': 100}
        outliers = flagOutliers(entryCount, 1.5, "test")
        self.assertIn('d', outliers) # Tests that 'd' is flagged as an outlier
        self.assertNotIn('a', outliers) # Tests that 'a' is not flagged as an outlier

    def test_flagOutliers_2(self):
        entryCount = {'a': 1, 'b': 1, 'c': 1}
        outliers = flagOutliers(entryCount, 1.5, "test")
        self.assertEqual(outliers, {}) 

if __name__ == '__main__':
    unittest.main()