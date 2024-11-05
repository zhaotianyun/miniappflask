from wxcloudrun.logger import logger
from sqlalchemy.exc import OperationalError

from wxcloudrun import db
from wxcloudrun.model import Tickets

def insert_ticket(ticket):
    """
    插入一个ticket实体
    :param ticket: tickets实体
    """
    try:
        db.session.add(ticket)
        db.session.commit()
        logger.info(f"Ticket inserted successfully with no: {ticket.no}")
    except OperationalError as e:
        logger.info("insert_ticket errorMsg= {} ".format(e))


