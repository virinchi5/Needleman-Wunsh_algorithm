from needleman_wunsch_algorithm_config import Needleman_wunsch_algorithm_config
from needleman_wunsch_algorithm import Needleman_wunsch_algorithm
import fasta_reader as fr
import input_data_validator as idv
import sys


if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    
    # Read arguments from user
    fasta_file1 = sys.argv[1]
    fasta_file2 = sys.argv[2]
    configuration_file = sys.argv[3]
    output_file = sys.argv[4]
    
    # Load sequences from files to strings
    sequence1 = fr.convert_fasta_to_string(fasta_file1)
    sequence2 = fr.convert_fasta_to_string(fasta_file2)
    
    # Load configuration file and create config object with configuration data
    config = Needleman_wunsch_algorithm_config(configuration_file)
    
    # Check if input data are valid
    validation_result = idv.validate_input_data(sequence1, sequence2, config)
    
    # If input data are correct then run algorithm
    if validation_result[0]:
        nwa = Needleman_wunsch_algorithm(sequence1, sequence2, config)
        nwa.print_results(output_file)
    else:
        print(validation_result[1])