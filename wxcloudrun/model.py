from datetime import datetime

from wxcloudrun import db


# ticket表
class Tickets(db.Model):
    # 设置结构体表格名称
    __tablename__ = 'ticket'

    # 设定结构体对应表格的字段
    no = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type = db.Column(db.String(64), nullable=False)
    text = db.Column(db.String(4096), nullable=False)
    createtime = db.Column(db.TIMESTAMP, default=datetime.utcnow, nullable=False)
    updatetime = db.Column(db.TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
