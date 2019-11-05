import unittest
import numpy as np

from needleman_wunsch_algorithm_config import NeedlemanWunschAlgorithmConfig
from needleman_wunsch_algorithm import NeedlemanWunschAlgorithm
from cell import Cell
from direction import Direction


class TestNeedlemanWunschAlgorithmMethods(unittest.TestCase):
    """
    Class representing tests for Needleman-Wunsch algorithm
    """

    def setUp(self):
        """
        Method creating object of class NeedlemanWunschAlgorithm to test methods
        """
        config = self._prepare_config(5, -5, -2, 10, 2000)
        self.input_data = ("SUM", "SAM", config)
        self.nwa = NeedlemanWunschAlgorithm(self.input_data[0], self.input_data[1], self.input_data[2])


    def _prepare_config(self, same, diff, gap_penalty, max_number_paths, max_seq_length):
        config = NeedlemanWunschAlgorithmConfig(manual = True)

        config.SAME = same
        config.DIFF = diff
        config.GAP_PENALTY = gap_penalty
        config.MAX_NUMBER_PATHS = max_number_paths
        config.MAX_SEQ_LENGTH = max_seq_length

        return config


    def test_get_scoring_matrix_has_correct_shape_of_matrix(self):
        # Expected result
        expected_result = self._get_expected_result_for_get_scoring_matrix_method()
        expected_result_shape = expected_result.shape

        # Result of the method get_scoring_matrix()
        result = self.nwa.get_scoring_matrix()
        result_shape = result.shape

        # Check scoring matrix shape
        self.assertEqual(result_shape, expected_result_shape, "Wrong shape of scoring matrix!")
    

    def test_get_scoring_matrix_has_correct_cells(self):
        # Expected result
        expected_result = self._get_expected_result_for_get_scoring_matrix_method()

        # Result of the method get_scoring_matrix()
        result = self.nwa.get_scoring_matrix()

        # Compare scoring matrixes
        for i in range(0, 4):
            for j in range(0, 4):
                self.assertEqual(result[i, j], expected_result[i, j])


    def _get_expected_result_for_get_scoring_matrix_method(self):
        n_row = 4
        n_col = 4

        expected_result = np.empty((n_row, n_col), dtype = Cell)
        expected_result_values = [0, -2, -4, -6, 
                                 -2, 5, 3, 1, 
                                 -4, 3, 1, -1, 
                                 -6, 1, -1, 6]
        expected_result_directions = [None, Direction.LEFT, Direction.LEFT, Direction.LEFT, 
                                        Direction.UP, Direction.DIAG, Direction.LEFT, Direction.LEFT, 
                                        Direction.UP, Direction.UP, Direction.UP|Direction.LEFT, Direction.UP|Direction.LEFT, 
                                        Direction.UP, Direction.UP, Direction.UP|Direction.LEFT, Direction.DIAG]
        for i in range(0, n_row):
            for j in range(0, n_col):
                k = i * n_row + j
                expected_result[i, j] = Cell()
                expected_result[i, j].value = expected_result_values[k]
                expected_result[i, j].directions = expected_result_directions[k]

        return expected_result


    def test_get_score(self):
        # Expected result
        expected_result = 6

        # Result of the methos get_score()
        result = self.nwa.get_score()

        # Compare scores
        self.assertEqual(result, expected_result)


    def test_get_result_has_correct_length(self):
        # Result of the get_result() method
        result = self.nwa.get_result()
        result_tuples_list = list(result)
        result_tuples_list_len = len(result_tuples_list)

        # Expected result
        expected_result_tuples_list = self._get_expected_result_for_get_result_method()
        expected_result_tuples_list_len = len(expected_result_tuples_list)

        # Check if lengths are equal
        self.assertEqual(result_tuples_list_len, expected_result_tuples_list_len)


    def test_get_result_has_correct_number_of_strings(self):
        # Result of the get_result() method
        result = self.nwa.get_result()
        result_tuples_list = list(result)
        result_list = [item for t in result_tuples_list for item in t]
        result_list_len = len(result_list)

        # Expected result
        expected_result_tuples_list = self._get_expected_result_for_get_result_method()
        expected_result_list = [item for t in expected_result_tuples_list for item in t]
        expected_result_list_len = len(expected_result_list)

        # Check if lengths are equal
        self.assertEqual(result_list_len, expected_result_list_len)


    def test_get_result_has_correct_lengths_of_elements(self):
        # Result of the get_result() method
        result = self.nwa.get_result()
        result_tuples_list = list(result)

        # Check if lengths are equal 2
        for r in result_tuples_list:
            self.assertEqual(len(r), 2)


    def test_get_result_has_all_strings(self):
        # Result of the get_result() method
        result = self.nwa.get_result()
        result_tuples_list = list(result)
        result_list = [item for t in result_tuples_list for item in t]

        # Expected result
        expected_result_tuples_list = self._get_expected_result_for_get_result_method()
        expected_result_list = [item for t in expected_result_tuples_list for item in t]

        # Check if all strings are in method result
        for r in expected_result_list:
            self.assertIn(r, result_list)


    def test_get_result_has_all_elements(self):
        # Result of the get_result() method
        result = self.nwa.get_result()
        result_tuples_list = list(result)

        # Expected result
        expected_result_tuples_list = self._get_expected_result_for_get_result_method()
        expected_result_tuples_list_len = len(expected_result_tuples_list)

        # Sort result elements and expected result elements to compare
        for i in range(0, expected_result_tuples_list_len):
            result_tuples_list[i] = tuple(np.sort(result_tuples_list[i]))
            expected_result_tuples_list[i] = tuple(np.sort(expected_result_tuples_list[i]))

        # Compare tuples
        for r in expected_result_tuples_list:
            self.assertIn(r, result_tuples_list)
    

    def _get_expected_result_for_get_result_method(self):
        return [("SU_M", "S_AM"), ("S_UM", "SA_M")]
        

if __name__ == '__main__':
    unittest.main()