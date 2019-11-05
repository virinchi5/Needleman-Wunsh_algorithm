import fasta_reader as fr
import input_data_validator as idv
import sys
import getopt

from needleman_wunsch_algorithm_config import NeedlemanWunschAlgorithmConfig
from needleman_wunsch_algorithm import NeedlemanWunschAlgorithm


if __name__ == "__main__":
    # Set the recursion limit
    sys.setrecursionlimit(10000)

    # Get the arguments from the command-line except the filename
    argv = sys.argv[1:]

    try:
        # Define the getopt parameters
        opts, args = getopt.getopt(argv, "a:b:c:o:", ["sequence1", "sequence2", "config", "output"])

        # Check if the options' length is 4
        if len(opts) != 4:
            print("Wrong options and parametres! \nUsage: add.py -a <sequence1> -b <sequence2> -c <config> -o <output> \nwhere sequence1, sequence2, config, output are txt files.")
        else:
            # Create list of input arguments
            inputs = []
            for opt, arg in opts:
                inputs.append(arg)

            # Create input variables for algorithm
            fasta_file1 = inputs[0]
            fasta_file2 = inputs[1]
            configuration_file = inputs[2]
            output_file = inputs[3]
            
            # Load sequences from files to strings
            sequence1 = fr.convert_fasta_to_string(fasta_file1)
            sequence2 = fr.convert_fasta_to_string(fasta_file2)
            
            # Load configuration file and create config object with configuration data
            config = NeedlemanWunschAlgorithmConfig(configuration_file)
            
            # Check if input data are valid
            validation_result = idv.validate_input_data(sequence1, sequence2, config)
            
            # If input data are correct then run algorithm
            if validation_result[0]:
                nwa = NeedlemanWunschAlgorithm(sequence1, sequence2, config)
                nwa.print_results(output_file)
            else:
                print(validation_result[1])

    except getopt.GetoptError:
        print("Wrong options and parametres! \nUsage: add.py -a <sequence1> -b <sequence2> -c <config> -o <output> \nwhere sequence1, sequence2, config, output are txt files.")
        sys.exit(2)