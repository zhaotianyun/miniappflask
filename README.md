## 目录结构说明

~~~
.
├── Dockerfile dockerfile       dockerfile
├── README.md README.md         README.md文件
├── container.config.json       模板部署「服务设置」初始化配置（二开请忽略）
├── requirements.txt            依赖包文件
├── config.py                   项目的总配置文件  里面包含数据库 web应用 日志等各种配置
├── run.py                      flask项目管理文件 与项目进行交互的命令行工具集的入口
└── miniProgramBackend          app目录
    ├── __init__.py             python项目必带  模块化思想
    ├── dao                     数据库访问模块目录
    ├── model                   数据库对应的模型目录
    ├── utils                   工具类目录
    ├── response.py             响应结构构造
    └── views.py                执行响应的代码所在模块  代码逻辑处理主要地点  项目大部分代码在此编写
~~~

## 使用注意
需要在「服务设置」中补全以下环境变量，才可正常使用，否则会引发无法连接数据库。
- MYSQL_ADDRESS
- MYSQL_PASSWORD
- MYSQL_USERNAME
以上三个变量的值请按实际情况填写。如果使用云托管内MySQL，可以在控制台MySQL页面获取相关信息。