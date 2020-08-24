

import logging
import logging.handlers

logger = logging.getLogger(__name__)

r_handler = logging.handlers.RotatingFileHandler(
    'logs/rotation_file.log',
    maxBytes=1000,
    backupCount=5,
    encoding='utf-8'
)

t_handler = logging.handlers.TimedRotatingFileHandler(
    'logs/rotating_time_file_log',
    when='S',
    interval=10,
    backupCount=5,
    encoding='utf-8'
)

logging.setLevel(logging.DEBUG)

r_handler.setLevel(logging.INFO)
t_handler.setLevel(logging.INFO)

sample_formatter = logging.Formatter('%(name)s-%(asctime)s-%(levelname)s-%(message)s')
r_handler.setFormatter(sample_formatter)
t_handler.setFormatter(sample_formatter)
logger.addHandler(r_handler)
logger.addHandler(t_handler)

import time

for _ in range(1000):
    logger.debug('デバッグ')
    logger.info('インフォ')
    logger.error('エラー')
    logger.warning('ワーニング')
    logger.critical('クリティカル')
    time.sleep(1)

