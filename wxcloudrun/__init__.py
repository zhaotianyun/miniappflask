from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
import config

# 因MySQLDB不支持Python3，使用pymysql扩展库代替MySQLDB库
pymysql.install_as_MySQLdb()

# 初始化 web 应用
app = Flask(__name__, instance_relative_config=True)

# 加载配置
app.config.from_object(config)

# 设置数据库 URI
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{config.username}:{config.password}@{config.db_address}/flask_demo'

# 关闭 SQLALCHEMY_TRACK_MODIFICATIONS，避免无意义的性能开销
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 初始化 DB 操作对象
db = SQLAlchemy(app)

# 加载控制器（视图函数）
from wxcloudrun import views
