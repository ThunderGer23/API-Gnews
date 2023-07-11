import logging
import os
import traceback


# The Logger class is used for logging messages and events in a Python program.
class Logger():

    def __set_logger(self):
        """
        The function sets up a logger with a specified log directory and filename, and returns the
        logger object.
        :return: a logger object.
        """
        log_directory = 'src/utils/log'
        log_filename = 'app.log'

        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)

        log_path = os.path.join(log_directory, log_filename)
        file_handler = logging.FileHandler(log_path, encoding='utf-8')
        file_handler.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s', "%Y-%m-%d %H:%M:%S")
        file_handler.setFormatter(formatter)

        if (logger.hasHandlers()):
            logger.handlers.clear()

        logger.addHandler(file_handler)

        return logger

    @classmethod
    def add_to_log(cls, level, message):
        """
        The function `add_to_log` adds a log message to a logger object based on the specified log level
        and message.
        
        :param cls: The parameter `cls` is a reference to the class itself. It is used to access
        class-level variables and methods
        :param level: The `level` parameter is a string that represents the severity level of the log
        message. It can have one of the following values: "critical", "debug", "error", "info", or
        "warn"
        :param message: The `message` parameter is a string that represents the log message that you
        want to add to the log. It can contain any information that you want to include in the log, such
        as error messages, debugging information, or general information about the program's execution
        """
        try:
            logger = cls.__set_logger(cls)

            if (level == "critical"):
                logger.critical(message)
            elif (level == "debug"):
                logger.debug(message)
            elif (level == "error"):
                logger.error(message)
            elif (level == "info"):
                logger.info(message)
            elif (level == "warn"):
                logger.warn(message)
        except Exception as ex:
            print(traceback.format_exc())
            print(ex)
