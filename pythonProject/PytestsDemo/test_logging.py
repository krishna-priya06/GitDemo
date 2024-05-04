import inspect
import logging


def test_loggingDemo():
    loggername =inspect.stack()[1][3]
    logger = logging.getLogger(__name__)

    fileHandler = logging.FileHandler('logfile.log')
    formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")#timestamp:levels:testfilename:message`
    fileHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)  #filehandler object

    logger.setLevel(logging.DEBUG)
    #levels:
    logger.debug("A debug statement is executed")
    logger.info("Information statement")
    logger.debug("A debug statement is executed")
    logger.warning("Something is in warning mode")
    logger.error("A Major error has happend")
    logger.critical("Critical issue")



