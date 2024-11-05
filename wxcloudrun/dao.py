import logging

from sqlalchemy.exc import OperationalError

from wxcloudrun import db
from wxcloudrun.model import Tickets

# 初始化日志
logger = logging.getLogger('log')


def insert_ticket(ticket):
    """
    插入一个ticket实体
    :param ticket: tickets实体
    """
    try:
        db.session.add(ticket)
        db.session.commit()
    except OperationalError as e:
        logger.info("insert_ticket errorMsg= {} ".format(e))


