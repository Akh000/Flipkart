import inspect
import logging


class LogGenerator:
    @staticmethod
    def loggen():
        name = inspect.stack()[1][3]
        logger = logging.getLogger(name)
        filepath = logging.FileHandler(".\\Logs\\flipkart.logs")
        formate = logging.Formatter("%(asctime)s : %(name)s : %(funcName)s : %(lineno)s : %(message)s : ")
        filepath.setFormatter(formate)
        logger.addHandler(filepath)
        logger.setLevel("INFO")
        return logger
