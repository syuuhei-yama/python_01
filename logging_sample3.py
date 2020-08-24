import logging
import logging.config

logging.config.fileConfig(fname='conf/logger.conf')

logger= logging.getLogger('samplelogger')
logger.debug('デバッグログ')
logger.info('インフォログ')
logger.warning('ワーニングログ')
logger.error('エラーログ')
logger.critical('クリティカルログ')

