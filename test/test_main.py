import logging
import unittest
from unittest.mock import patch

from app import main


class TestSum(unittest.TestCase):
    '''
    Testing Class for Cicada
    '''

    @patch.object(logging, 'warning')
    def test_math(self, mock_warning):
        '''
        test that math function calls logging
        '''
        main.math()
        mock_warning.assert_called()

if __name__ == '__main__':
    '''
    Testing Entrypoint
    '''
    unittest.main()
