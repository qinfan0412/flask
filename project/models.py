from main import db
from datetime import datetime


class BaseModel(db.Model):
    __abstract__ = True  ## 声明当前类为抽象类 能被继承 # 调用不会被创建
    id = db.Column(db.Integer, primary_key=True)  ## 继承基类的时候id直接被继承，不用再写id字段

    def save(self):
        db.session.add(self)
        db.session.commit()

    def merge(self):
        db.session.merge(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


## 创建模型
class UserInfo(BaseModel):
    ## 字段
    __tablename__ = "userinfo"  ##  指定表名
    # id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(32))
    age = db.Column(db.Integer, default=1)
    time = db.Column(db.DATETIME, default=datetime.now())


# ------------------------用户表
class User(BaseModel):
    ## 字段
    __tablename__ = "user"  ##  指定表名
    email = db.Column(db.String(32))
    name = db.Column(db.String(32))
    age = db.Column(db.Integer, default=1)
    sex = db.Column(db.String(32))
    password = db.Column(db.Text)
    identity = db.Column(db.String(32))  # 身份
    subject = db.Column(db.String(32))  # 学科
    level = db.Column(db.String(64))  # 阶段
    photo = db.Column(db.String(64))  # 头像


# ------------------------请假条
class Leave_User(BaseModel):
    __tablename__ = 'leave_user'
    request_id = db.Column(db.Integer)
    request_name = db.Column(db.String(32))  # 请假人
    request_type = db.Column(db.String(32))  # 请假类型
    request_start = db.Column(db.String(32))
    request_end = db.Column(db.String(32))
    request_day= db.Column(db.Integer)
    request_description = db.Column(db.TEXT)  # 请假描述
    request_phone = db.Column(db.String(11))
    request_status = db.Column(db.Integer)  # 请假状态
   #   #   审核中   0
    #   通过    1
    #   驳回     2
    #   销假     3