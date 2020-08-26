import logging


class Logger(object):
    def log_info(self, informationmessage):
        logging.info(informationmessage)

    def log_error(self, errormessage):
        logging.error(errormessage)

    def log_debug(self, debugmessage):
        logging.debug(debugmessage)

    def log_warning(self, warningmessage):
        logging.warning(warningmessage)

    def log_critical(self, criticalmessage):
        logging.critical(criticalmessage)
