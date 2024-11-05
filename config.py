import os

# 是否开启debug模式
DEBUG = True

# 读取数据库环境变量
username = os.environ.get("MYSQL_USERNAME", 'miniapp')
password = os.environ.get("MYSQL_PASSWORD", 'Zty1234!')
db_address = os.environ.get("MYSQL_ADDRESS", '10.22.100.117:3306')

print(f"Using MySQL username: {username}, address: {db_address}")
