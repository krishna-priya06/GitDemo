import inspect
import logging


class BaseClass:
    def getlogger(self):
        loggername = inspect.stack()[1][3]
        logger = logging.getLogger(loggername)

        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter(
            "%(asctime)s :%(levelname)s : %(name)s :%(message)s")  # timestamp:levels:testfilename:message`
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.INFO)
        return logger