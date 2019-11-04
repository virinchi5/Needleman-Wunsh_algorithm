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
        config = self._prepare_config(5, -5, -2, 10, 2000)
        self.input_data = ("SUM", "SAM", config)
        self.nwa = NeedlemanWunschAlgorithm(self.input_data[0], self.input_data[1], self.input_data[2])


    def _prepare_config(self, same, diff, gp, max_number_paths, max_seq_length):
        config = NeedlemanWunschAlgorithmConfig(manual = True)

        config.SAME = same
        config.DIFF = diff
        config.GP = gp
        config.MAX_NUMBER_PATHS = max_number_paths
        config.MAX_SEQ_LENGTH = max_seq_length

        return config
    

    def test_get_scoring_matrix(self):
        result = self.nwa.get_scoring_matrix()
        
        expected_result = np.empty((4, 4), dtype = Cell)
        expected_result_values = [0, -2, -4, -6, 
                                 -2, 5, 3, 1, 
                                 -4, 3, 1, -1, 
                                 -6, 1, -1, 6]
        expected_result_directions = [None, Direction.LEFT, Direction.LEFT, Direction.LEFT, 
                                        Direction.UP, Direction.DIAG, Direction.LEFT, Direction.LEFT, 
                                        Direction.UP, Direction.UP, Direction.UP|Direction.LEFT, Direction.UP|Direction.LEFT, 
                                        Direction.UP, Direction.UP, Direction.UP|Direction.LEFT, Direction.DIAG]
        for i in range(0, 4):
            for j in range(0, 4):
                k = i * 4 + j
                expected_result[i, j] = Cell()
                expected_result[i, j].value = expected_result_values[k]
                expected_result[i, j].directions = expected_result_directions[k]

        for i in range(0, 4):
            for j in range(0, 4):
                self.assertEqual(result[i, j], expected_result[i, j])


    def test_get_score(self):
        result = self.nwa.get_score()
        expected_result = 6
        self.assertEqual(result, expected_result)
    
    
    # TO DO: correct and finish
    def test_get_result(self):
        result = self.nwa.get_result()
        result_tuples_list = list(result)
        result_tuples_list_len = len(result_tuples_list)
        result_list = [item for t in result_tuples_list for item in t]
        result_list_len = len(result_list)

        expected_result_tuples_list = [("SU_M", "S_AM"), ("S_UM", "SA_M")]
        expected_result_tuples_list_len = len(expected_result_tuples_list)
        expected_result_list = ["SU_M", "S_AM", "S_UM", "SA_M"]
        expected_result_list_len = len(expected_result_list)

        self.assertEqual(result_tuples_list_len, expected_result_tuples_list_len)
        self.assertEqual(result_list_len, expected_result_list_len)

        for r in result_tuples_list:
            self.assertEqual(len(r), 2)
        
        for r in expected_result_list:
            self.assertIn(r, result_list)

        # self.assertTrue((result_tuples_list[0][0] == expected_result_tuples_list[0][0] or result_tuples_list[0][0] == expected_result_tuples_list[0][1]) and
        #                 (result_tuples_list[0][1] == expected_result_tuples_list[0][0] or result_tuples_list[0][1] == expected_result_tuples_list[0][1]))


if __name__ == '__main__':
    unittest.main()