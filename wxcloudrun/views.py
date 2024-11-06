from datetime import datetime
from flask import render_template, request, jsonify
from run import app
from wxcloudrun.dao import insert_ticket, query_by_nickname
from wxcloudrun.model import Tickets
from wxcloudrun.logger import logger  # 导入日志实例
from sqlalchemy.exc import SQLAlchemyError

@app.route('/')
def index():
    """
    :return: 返回index页面
    """
    logger.info("Accessed the index page.")
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit_data():
    data = request.json
    logger.info(f"Received data: {data}")

    if not data or 'customer' not in data or 'nickname' not in data or 'type' not in data or 'text' not in data:
        logger.warning(f"Invalid input data: {data}")
        return jsonify({"error": "Invalid input"}), 400

    new_ticket = Tickets(customer=data['customer'], nickname=data['nickname'], type=data['type'], text=data['text'], status=0, imagelink=data['imagelink'])
    logger.info(f"Created new ticket: {new_ticket}")

    try:
        insert_ticket(new_ticket)
        logger.info(f"Ticket inserted successfully with no: {new_ticket.no}")
    except SQLAlchemyError as e:
        logger.error(f"Failed to insert ticket: {str(e)}")
        return jsonify({"error": f"Failed to insert ticket: {str(e)}"}), 500

    response = {
        "no": new_ticket.no,
        "customer": new_ticket.customer,
        "nickname": new_ticket.nickname,
        "type": new_ticket.type,
        "text": new_ticket.text,
        "status": new_ticket.status,
        "imagelink": new_ticket.imagelink,
        "create_time": new_ticket.createtime.isoformat(),
        "update_time": new_ticket.updatetime.isoformat()
    }
    logger.info(f"Response: {response}")
    return jsonify(response), 200


@app.route('/tickets/history/<nickname>', methods=['GET'])
def get_ticket_history(nickname):
    # 调用dao层的查询函数
    result = query_by_nickname(nickname)

    # 如果返回的结果包含错误信息，则返回500错误
    if "error" in result:
        return jsonify({"error": result["error"]}), 500

    # 返回查询到的工单历史数据
    return jsonify(result), 200
