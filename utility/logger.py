import logging


class Logger:
    # logging for information
    def log_info(self, informationmessage):
        logging.info(informationmessage)

    # logging for error
    def log_error(self, errormessage):
        logging.error(errormessage)

    # logging for debugging
    def log_debug(self, debugmessage):
        logging.debug(debugmessage)

    # logging for warning
    def log_warning(self, warningmessage):
        logging.warning(warningmessage)

    # logging for critical
    def log_critical(self, criticalmessage):
        logging.critical(criticalmessage)
