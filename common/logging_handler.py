import logging
import os

from config import config


class Logger():
    # 输出管理器
    stream_handler = logging.StreamHandler()

    def __init__(self, log_config=None):
        # 默认配置
        if log_config is None:
            log_config = {}
        log_conf = {
            "logger_name": "test",
            "logfile": None,
            "logger_level": "DEBUG",
            "stream_level": "DEBUG",
            "file_level": "INFO",
            "fmt": '[%(levelname)s  %(asctime)s  ]: %(filename)s  line:%(lineno)d  msg:%(message)s'

        }
        for k, v in log_config.items():
            log_conf[k] = v
            if k == "logfile":
                log_conf[k] = os.path.join(config.LOG_PATH, v)

        # 获取到收集器
        self.logger = logging.getLogger(log_conf["logger_name"])

        # 设置收集器的级别
        self.logger.setLevel(log_conf["logger_level"])

        # 日志格式
        self.fmt_str = log_conf["fmt"]
        fmt = logging.Formatter(log_conf["fmt"])

        if log_conf["logfile"]:
            file_handler = logging.FileHandler(log_conf["logfile"], encoding='utf8')
            file_handler.setLevel(log_conf["file_level"])
            file_handler.setFormatter(fmt)
            self.logger.addHandler(file_handler)

        # stream_handler = logging.StreamHandler()
        # stream_handler.setLevel(log_conf["stream_level"])
        # logger.addHandler(stream_handler)

        # stream_handler.setFormatter(fmt)

    def fontColor(self, color):
        # 不同的终端日志输出不同的颜色
        formatter = logging.Formatter(color % self.fmt_str)
        self.stream_handler.setFormatter(formatter)
        self.logger.addHandler(self.stream_handler)

    def debug(self, message):
        self.fontColor('\033[0;51m%s\033[0m')
        self.logger.debug(message)

    def info(self, message):
        self.fontColor('\033[0;37m%s\033[0m')
        self.logger.info(message)

    def warning(self, message):
        self.fontColor('\033[0;31m%s\033[0m')
        self.logger.warning(message)

    def error(self, message):
        self.fontColor('\033[0;33m%s\033[0m')
        self.logger.error(message)

    def critical(self, message):
        self.fontColor('\033[0;30m%s\033[0m')
        self.logger.critical(message)


if __name__ == '__main__':
    logger = Logger()
    logger.info("hello")
    logger.warning("warning")
    logger.error("error")
    logger.debug("debug")
    logger.critical("critical")
