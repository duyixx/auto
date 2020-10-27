import logging


def get_logger(
        logger_name="root",
        logfile=None,
        logger_level="DEBUG",
        stream_level="DEBUG",
        file_level="INFO",
        fmt='%(asctime)s,  loglevel:%(levelname)s,  file "%(filename)s", line:%(lineno)d,  msg:%(message)s',
):
    # 获取到收集器
    logger = logging.getLogger(logger_name)
    # 设置收集器的级别
    logger.setLevel(logger_level)

    # 输出管理器
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(stream_level)
    logger.addHandler(stream_handler)

    # 格式
    fmt = logging.Formatter(fmt)
    stream_handler.setFormatter(fmt)

    if logfile:
        file_handler = logging.FileHandler(logfile, encoding='utf8')
        file_handler.setLevel(file_level)
        logger.addHandler(file_handler)
        file_handler.setFormatter(fmt)
    return logger


if __name__ == '__main__':
    logger = get_logger()
    logger.info("hello")
    logger.warning("warning")
