from datetime import datetime
from flask import render_template, request, jsonify
from run import app
from wxcloudrun.dao import insert_ticket
from wxcloudrun.model import Tickets
from wxcloudrun.response import make_succ_empty_response, make_succ_response, make_err_response


@app.route('/')
def index():
    """
    :return: 返回index页面
    """
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit_data():
    data = request.json
    if not data or 'type' not in data or 'text' not in data:
        return jsonify({"error": "Invalid input"}), 400

    new_ticket = Tickets(type=data['type'], text=data['text'])
    insert_ticket(new_ticket)

    return jsonify({
        "no": new_ticket.no,
        "type": new_ticket.type,
        "text": new_ticket.text,
        "create_time": new_ticket.createtime,
        "update_time": new_ticket.updatetime
    }), 201
