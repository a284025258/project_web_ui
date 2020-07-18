"""登录测试用例数据"""

login_data = [
    {'case_id': 1, 'title': '手机号为空', 'username': '', 'password': 'a12345678', 'expected': '请输入手机号',
     'tags': ['error', 'login']},
    {'case_id': 2, 'title': '手机号不存在', 'username': '13981111111', 'password': 'a12345678',
     'expected': '此账号没有经过授权，请联系管理员!', 'tags': ['alert', 'login']},
    {'case_id': 3, 'title': '手机号格式有误', 'username': '1398111111', 'password': 'a12345678', 'expected': '请输入正确的手机号',
     'tags': ['error', 'login']},
    {'case_id': 4, 'title': '密码不正确', 'username': '18684720553', 'password': 'python1', 'expected': '帐号或密码错误!',
     'tags': ['alert', 'login']},
    {'case_id': 5, 'title': '正常登录', 'username': '18684720553', 'password': 'python', 'expected': '我的帐户[python]',
     'tags': ['success', 'login']}
]
