import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Product:
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True  ## 请求结束之后自动提交
    SQLALCHEMY_RTACK_MODIFICATIONS = True  ## 跟踪修改  flask 1.x 之后增加的配置项
    SQLALCHEMY_TRACK_MODIFICATIONS = True  ## 报错修改
    # app.config["DEBUG"] = True  # 修改后自动启动项目，会报错
    SECRET_KEY='123456'


class Config(Product):
    ## 正式环境的 配置
    SQLALCHEMY_DATABASE_URI = "mysql://root:123456@localhost/flask"  ## 链接mysql配置



class TestConfig(Product):
    ## 测试环境的 配置
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, "test.db")  ## 测试环境用sqlite
    DEBUG = True  # 修改后自动启动项目，会报错

import os
STATIC_PATH=os.path.join(BASE_DIR,'static')
