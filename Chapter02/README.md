# Chapter 02: Basic Application Structure

[hello.py](hello.py) 로 Hello World! 만 직어주는 간단한 플라스크 앱을 만들어봅니다.

## 실행

[hello.py](hello.py) 를 다음처럼 실행시키시면 됩니다.

```bash
(flasky) Macbook2017:Chapter02 sangmin$ export FLASK_APP=hello.py
(flasky) Macbook2017:Chapter02 sangmin$ export FLASK_DEBUG=1
(flasky) Macbook2017:Chapter02 sangmin$ flask run
 * Serving Flask app "hello.py" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 228-442-677
```

다음 링크들을 실행시켜보세요.
- [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
- [http://127.0.0.1:5000/user/sangmin](http://127.0.0.1:5000/user/sangmin)
- [http://127.0.0.1:5000/user/jordan](http://127.0.0.1:5000/user/jordan)
- [http://127.0.0.1:5000/agent](http://127.0.0.1:5000/agent)
- [http://127.0.0.1:5000/bad](http://127.0.0.1:5000/bad)
- [http://127.0.0.1:5000/cookie](http://127.0.0.1:5000/cookie)
- [http://127.0.0.1:5000/redirect](http://127.0.0.1:5000/redirect)

## Flask Shell

`flask run`으로 실행하는 것 이외에도 `flask shell` 쉘 자체로 많은 일을 할 수가 있습니다.

```bash
(flasky) Macbook2017:Chapter02 sangmin$ export FLASK_APP=user_agent.py
(flasky) Macbook2017:Chapter02 sangmin$ flask shell
Python 3.7.3 (default, Mar 27 2019, 16:54:48)
[Clang 4.0.1 (tags/RELEASE_401/final)] on darwin
App: user_agent [production]
Instance: /Users/sangmin/git/flasky/Chapter02/instance
>>> from hello import app
>>> from flask import current_app
>>> current_app.name
'user_agent'
>>> app_ctx = app.app_context()
>>> app_ctx.push()
>>> current_app.name
'hello'
>>> app_ctx.pop()
>>> app.url_map
Map([<Rule '/' (OPTIONS, GET, HEAD) -> index>,
 <Rule '/static/<filename>' (OPTIONS, GET, HEAD) -> static>,
 <Rule '/user/<name>' (OPTIONS, GET, HEAD) -> user>])
```