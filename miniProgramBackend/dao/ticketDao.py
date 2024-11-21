from miniProgramBackend.utils.logger import logger
from sqlalchemy.exc import OperationalError

from miniProgramBackend import db
from miniProgramBackend.model.ticketsModel import Tickets

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

def query_by_nickname(nickname):
    """
    根据用户的nickname查询所有工单历史
    :param nickname: 用户的昵称
    :return: 返回工单列表
    """
    try:
        # 查询该用户的所有工单记录
        tickets = db.session.query(Tickets).filter(Tickets.nickname == nickname).all()
        result = []
        for ticket in tickets:
            result.append({
                'no': ticket.no,
                'customer': ticket.customer,
                'nickname': ticket.nickname,
                'type': ticket.type,
                'text': ticket.text,
                'status': ticket.status,
                'imagelink': ticket.imagelink,
                'createtime': ticket.createtime.strftime('%Y-%m-%d %H:%M:%S'),  # 格式化日期
                'updatetime': ticket.updatetime.strftime('%Y-%m-%d %H:%M:%S'),  # 格式化日期
            })
        return result
    except Exception as e:
        return {"error": str(e)}

