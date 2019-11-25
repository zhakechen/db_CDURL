# # #Flask基础#
#
# ## Flask与Django区别
#
# 	Flask - 微框架、灵活、扩展性强、按需组合
# 	Django - 大而全、开箱即用、方便、灵活稍差
#
# ## Flask主要包含
#
# 	* Web服务器网关接口 Werkzeug
#
#  (WSGI Web Server Gateway Interface)
# 	* 	模板系统 Jinja2
# 其他包可自行扩展
#
# ## 安装和运行 (虚拟环境）
#
# ```
# mkdir src
# python3 -m venv venv
# source venv/bin/activate
# pip install flask
# ```
#
# ## 简单的例子 hello.py
#
# ```
# from flask import Flask
#
# app = Flask(__name__)
#
# @app.route('/')
# def index():
#     return '<h1>你好未来</h1>'
#
# @app.route('/user/<name>')
# def user(name):
#     return '<h2>你好啊, %s</h2>' % name
#
# if __name__ == '__main__':
#     app.run(debug=True)
#     # app.run(debug=True, host='0.0.0.0', port=5001)
# ```
#
# ## 程序和请求上下文 context
#
# 为了视图访问方便，Flask使用上下文临时将某些对象变为在一个请求线程中全局可访问
#
# 两种上下文
# 	程序上下文 （跟整个程序有关）
# 	请求上下文 （跟当前用户请求相关）
#
# current_app    程序上下文    当前激活程序的程序实例
# g                        程序上下文    处理请求时用作临时存储对象
# request            请求上下文     请求对象
# session             请求上下文     回话对象
#
# ```
# from flask import request
#
# @app.route('/getip')
# def getip():
#     ip = request.remote_addr
#     user_agent = request.headers.get('User-Agent')
#     return '<h1>你的ip地址是%s, User-Agent是%s</h2>' % (ip, user_agent)
# ```
#
#
# ## 响应
#
# 默认是200
#
# ```
# from flask import make_response
#
# # 自动构建响应, 可以设置返回的状态
# @app.route('/diffrequest')
# def diffrequest():
#     return '<h2>Bad request</h2>', 200
#
# # 手动构建响应
# @app.route('/login/<username>')
# def login(username):
#     response = make_response('<h1>我来使用cookie</h1>')
#     response.set_cookie('username', username)
#     return response
# ```
#
# 重定向
# 没有返回页面，但是给浏览器一个新地址进行加载，状态码302
#
# ```
# # 重定向
# @app.route('/jump')
# def jump():
#     username = 'jon'
#     return redirect('/login/%s' % username)
# ```
#
# abort抛异常的方法
#
# ```
# # abort抛异常的方法
# @app.route('/guess/<int:number>')
# def guess(number):
#     if number < 8000:
#         abort(404)
#     return '<h1>你猜对了</h1>'
# ```
#
# ## Flask-Script
#
# 方便启动flask程序的时候传递启动参数
#
# ```
# $ pip install flask-script
# ```
#
# ```
# from flask_script import Manager
# manager = Manager(app)
# manager.run()
# ```
#
# ```
# $ python hello.py runserver --help
#
# 允许其他机器访问服务器
# $ python hello.py runserver -h 0.0.0.0 -p 5001
# ```
#
# ## jinja2模板
#
# Flask 默认在程序相同文件夹中的templates子文件夹中找模板
#
# ```
# from flask import Flask, render_template
# from flask_script import Manager
#
# app = Flask(__name__)
# manager = Manager(app)
#
# # 渲染一个简单的模板, 模板默认在templates中
# @app.route('/')
# def index():
#     return render_template('index.html')
#
# if __name__ == '__main__':
#     manager.run()
# ```
#
# ### 使用模板变量
#
# ```
# @app.route('/usevar/<name>')
# def usevar(name):
#     result_list = ['苹果', '梨', '西瓜']
#     result_dict = { '姓名': '吴东', '生日': '1999-10-21' }
#     return render_template('usevar.html', name=name, result_list=result_list, result_dict=result_dict)
# ```
#
# ### 模板过滤器语法：
#
# {{ 变量|过滤器|过滤器… }}
# capitalize 单词首字母大写
# lower 单词变为小写
# upper 单词变为大写
# title 每个单词首字母大写
# trim 去掉字符串的前后的空格
# reverse 单词反转
# striptags 渲染之前，将值中标签去掉
# safe 讲样式渲染到页面中
# last 最后一个字母
#
# ### 模板控制结构
#
# ```
#     {% if result_list %}
#         <ul>
#         {% for item in result_list %}
#             <li>{{ item }}</li>
#         {% endfor %}
#         </ul>
#     {% else %}
#     <h2>篮子里是空的</h2>
#     {% endif %}
# ```
#
# 宏，模板上定义的函数
#
# ```
#     {% macro f(content) %}
#         <span style="color:blue;">{{ content }}</span>
#     {% endmacro %}
#
#     <div>{{ f('蓝色的') }}</div>
# ```
#
# ## 模板继承
#
# base.html
#
# ```
# <!DOCTYPE html>
# <html>
# <head>
#     {% block head %}
#     <title>{% block title %}{% endblock %}</title>
#     {% endblock %}
# </head>
# <body>
#     {% block body %}
#     <div class="a1">模板上的默认文字</div>
#     {% endblock %}
# </body>
# </html>
# ```
#
# child.html
#
# ```
# {% extends "base.html" %}
#
# {% block title %}母版页测试{% endblock %}
# {% block head %}
#     {{ super() }}
#     <style>
#         .a1 { color:red;  }
#     </style>
# {% endblock %}
#
# {% block body %}
#     {{ super() }}
#     <div>今天天气如何？</div>
# {% endblock %}
# ```
#
# ### 自定义错误页面
#
# ```
# # 自定义错误页面
# @app.errorhandler(404)
# def page_not_found(e):
#     return render_template('404.html'), 404
#
# @app.errorhandler(500)
# def errorhandler(e):
#     return render_template('500.html'), 500
# ```
#
# ### 链接
#
# url_for 用视图函数名返回对应的url
#
# ```
# url = url_for('index') # 相对链接  /
# url = url_for('index', _external=True) # 绝对链接，比如放在邮件里面 http://127.0.0.1:5000/
# url = url_for('login', username='carmack', v=1) # /login/carmack/?v=1
# ```
#
# ### 静态文件
#
# 默认放在static目录下，包括图片，css,  javascript
#
# ```
# <img src="{{ url_for('static', filename='images/img_2569.jpg') }}" width="400px;">
# ```
#
# ### 视图里如何读取传入的数据
#
# ```
# # 读取GET方式传入的数据
# tag = request.args.get('tag')
# # 读取POST方式传入的数据
# username = request.form.get('username')
# ```
#
# CSRF (Cross-Site Request Forgery) 恶意网站把请求发送到被攻击者已登录的其他网站，防止方式：设置一个密钥，Flask用这个密钥生成加密的令牌，再用令牌验证表单数据
#
# ```
# app.config['SECRET_KEY'] = 'q234asdfad@#$AdfS*UNFs'
# ```
#
# ## 使用Werkzeug实现密码散列
#
# ```
# from werkzeug.security import generate_password_hash, check_password_hash
# ```
#
# generate_password_hash(password, method=_pbkdf2:sha1_, salt_length=8):这个函数将 原始密码作为输入，以字符串形式输出密码的散列值，输出的值可保存在用户数据库中。
# method 和salt_length 的默认值就能满足大多数需求。
#
# check_password_hash(hash, password) :这个函数的参数是从数据库中取回的密码散列 值和用户输入的密码。返回值为
# True ### 表明密码正确
#
#
#
