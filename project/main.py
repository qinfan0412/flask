from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
## 解决一开始报错没有Mysqldb模块
import pymysql

pymysql.install_as_MySQLdb()

app = Flask(__name__)

BASE_DIR = os.path.abspath(os.path.dirname(__file__))  ##当前__file__文件的上一级目录  项目所在根目录
app.config.from_pyfile("settings.py")  ## 使用python文件做配置文件
app.config.from_object("settings.TestConfig")


## sqlite3
# app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///" + os.path.join(BASE_DIR,"test.db")  ## 链接sqlite3配置

## mysql
# app.config["SQLALCHEMY_DATABASE_URI"]="mysql://root:123456@localhost/flask"  ## 链接mysql配置
# app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True  ## 请求结束之后自动提交
# app.config["SQLALCHEMY_RTACK_MODIFICATIONS"] = True   ## 跟踪修改  flask 1.x 之后增加的配置项
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True   ## 报错修改
# # app.config["DEBUG"] = True  # 修改后自动启动项目，会报错


db = SQLAlchemy(app)  ## 绑定flask项目