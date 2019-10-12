from flask import Flask

app = Flask(__name__)  # 实例化app实例


@app.route('/')  # 路由
def index():  # 视图
    return 'hello world'  # 返回值

@app.route('/hello')
def hello():
    return 'hello'

if __name__ == '__main__':
    # app.run()#项目启动，默认5000端口
    app.run(host="127.0.0.1", port=8000, debug=True, )
# 开启debug模式：1.显示错误内容，修改代码之后自动重启
