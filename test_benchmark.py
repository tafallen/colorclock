import unittest
from unittest.mock import patch, MagicMock
import benchmark
from datetime import datetime

class TestBenchmark(unittest.TestCase):
    @patch('timeit.timeit')
    @patch('builtins.print')
    def test_benchmark_execution(self, mock_print, mock_timeit):
        # Set return values for timeit.timeit
        mock_timeit.side_effect = [0.1234, 5.6789]

        # Execute the benchmark function
        benchmark.benchmark()

        # Verify timeit.timeit was called twice
        self.assertEqual(mock_timeit.call_count, 2)

        # Check first call to timeit
        # The first call uses a lambda, so we can't easily check the exact function object,
        # but we can check the 'number' argument.
        first_call_args, first_call_kwargs = mock_timeit.call_args_list[0]
        self.assertEqual(first_call_kwargs['number'], 100000)

        # Check second call to timeit
        second_call_args, second_call_kwargs = mock_timeit.call_args_list[1]
        self.assertEqual(second_call_kwargs['number'], 1000)

        # Verify print was called twice with expected format
        self.assertEqual(mock_print.call_count, 2)
        mock_print.assert_any_call("get_colours_for_time (100,000 calls): 0.1234 seconds")
        mock_print.assert_any_call("All variants (1,000 iterations of 24h + 60m): 5.6789 seconds")

if __name__ == '__main__':
    unittest.main()
