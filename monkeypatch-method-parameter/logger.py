import logging


def logger(name):
    # Create a logger.
    logger = logging.getLogger(name=name)
    logger.setLevel(logging.DEBUG)

    # Create a console handler and set the level to debug.
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # Create a formatter.
    formatter = logging.Formatter("%(levelname)s:%(filename)s:%(lineno)d %(message)s")

    # Add the formatter to the console handler.
    ch.setFormatter(formatter)

    # Add the console handler to the logger.
    logger.addHandler(ch)

    return logger
