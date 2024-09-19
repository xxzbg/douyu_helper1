# encoding:utf-8
from common.dy_glows import *
from common.login_check import *
from common.config import conf
from common.dy_badge import *
from common.logger import logger
import math
from common.get_secrets import get_secrets
from common.send_message import send_message
from common.dirs import LOG_FILE


def run():
    logger.add(LOG_FILE, encoding='utf-8', level='INFO', format='{level}:{message}')
    logger.debug("------登录检查开始------")
    login_res = is_login()
    logger.debug("------登录检查结束------")
    mode = int(conf.get_conf("Modechoose")['givemode'])
    if login_res:
        get_glow()
    else:
        logger.warning("未登录状态无法进行后续操作,任务已结束")
    try:
        server_key = get_secrets("SERVERPUSHKEY")
        send_message(server_key)
    except Exception as e:
        logger.info("当前未配置Server酱推送，任务结束")
        logger.debug(e)


if __name__ == '__main__':
    run()
