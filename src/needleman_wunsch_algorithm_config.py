from config import Config


class Needleman_wunsch_algorithm_config(Config):
    def __init__(self, config_file = "config.txt"):
        Config.__init__(self, config_file)
        self.SAME = self["SAME"]
        self.DIFF = self["DIFF"]
        self.GP = self["GP"]
        self.MAX_NUMBER_PATHS = self["MAX_NUMBER_PATHS"]
        self.MAX_SEQ_LENGTH = self["MAX_SEQ_LENGTH"]