from datetime import datetime
from flask import render_template, request, jsonify
from run import app
from wxcloudrun.dao import insert_ticket
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

    if not data or 'type' not in data or 'text' not in data:
        logger.warning(f"Invalid input data: {data}")
        return jsonify({"error": "Invalid input"}), 400

    new_ticket = Tickets(type=data['type'], text=data['text'])
    logger.info(f"Created new ticket: {new_ticket}")

    try:
        insert_ticket(new_ticket)
        db.session.refresh(new_ticket)
        logger.info(f"Ticket inserted successfully with no: {new_ticket.no}")
    except SQLAlchemyError as e:
        logger.error(f"Failed to insert ticket: {str(e)}")
        return jsonify({"error": f"Failed to insert ticket: {str(e)}"}), 500

    response = {
        "no": new_ticket.no,
        "type": new_ticket.type,
        "text": new_ticket.text,
        "create_time": new_ticket.createtime.isoformat(),
        "update_time": new_ticket.updatetime.isoformat()
    }
    logger.info(f"Response: {response}")
    return jsonify(response), 201
