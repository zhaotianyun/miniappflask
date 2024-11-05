import logging

# 配置日志
def setup_logger():
    # 创建一个日志器
    logger = logging.getLogger('wxcloudrun')
    logger.setLevel(logging.INFO)  # 设置日志级别

    # 创建控制台处理器（StreamHandler）用于输出到控制台
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # 创建日志格式
    formatter = logging.Formatter('%(asctime)s - %(filename)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)

    # 将处理器添加到日志器
    logger.addHandler(console_handler)

    return logger

# 创建全局的日志实例
logger = setup_logger()
