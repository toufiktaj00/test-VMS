import logging
import os

logger = logging.getLogger(__name__)

class LogGen:

    @staticmethod
    def loggen():
        log_directory = os.path.join(os.getcwd(), "Logs")
        if not os.path.exists(log_directory):
            os.makedirs(log_directory)

        log_file = os.path.join(log_directory, "automation.log")

        logging.basicConfig(filename=log_file, format='%(asctime)s: %(levelname)s: %(message)s',
                            datefmt='%d/%m/%y %I:%M:%S %p', level=logging.INFO)
        return logger












# import logging
# import os
#
# class LogGen:
#
#     @staticmethod
#     def loggen():
#         log_directory = os.path.join(os.getcwd(), "Logs")
#         if not os.path.exists(log_directory):
#             os.makedirs(log_directory)
#
#         log_file = os.path.join(log_directory, "automation.log")
#
#         logging.basicConfig(filename=log_file, format='%(asctime)s: %(levelname)s: %(message)s',
#                             datefmt='%d/%m/%y %I:%M:%S %p', level=logging.INFO)
#         logger = logging.getLogger()
#         return logger

# import logging
#
# class LogGen:
#
#     @staticmethod
#     def loggen():
#         logging.basicConfig(filename=".\\Logs\\automation.log",format='%(asctime)s: %(levelname)s: %(message)s',
#                             datefmt='%d/%m/%y %I:%M:%S %p')
#         logger = logging.getLogger()
#         logger.setLevel(logging.INFO)
#         return logger