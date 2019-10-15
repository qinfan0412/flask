# 项目的管理/运行 文件
# 类似python manage.py runserver/migrate
# 从终端获取输入的参数
import sys
from views import *
from models import *

from flask_script import Manager

manager = Manager(app)


@manager.command
def migrate():
    db.create_all()


if __name__ == '__main__':
    manager.run()
