# Chapter 07: Large Application Structure

## 왜 6단원은 안하는가?

6단원은 이메일을 보내는 단원입니다. 이제는 더 이상 웹서버에서 직접 이메일을 보내지 않죠? 책에 나온 예제도 `smtp.google.com`을 통해서 메일을 보내는 것입니다. 대략 10년전 가능했던 방법이네요. 회사에서도 그렇게 직접 이메일 보내는 경우는 거의 없기에 6단원 내용은 쓸 일이 없을거 같습니다.

## 개요

7단원의 내용은 5장까지의 내용을 다른 구조로 만드는것입니다. 다음의 구조로 정리되네요.

```bash
(flasky) Macbook2017:Chapter07 sangmin$ tree
.
├── app
│   ├── __init__.py
│   ├── main
│   │   ├── __init__.py
│   │   ├── errors.py
│   │   ├── forms.py
│   │   └── views.py
│   ├── models.py
│   └── templates
│       ├── 403.html
│       ├── 404.html
│       ├── 500.html
│       ├── base.html
│       └── index.html
├── config.py
├── flasky.py
└── tests
    ├── __init__.py
    └── test_basics.py
```

중요한 파일들은 다음입니다.

- [flasky.py](flasky.py): `create_app()`을 불러 앱을 구동합니다. 테스트, 쉘을 등록합니다.
- [config.py](config.py): 설정관련 내용을 모아둡니다.
- [app/__init__.py](app/__init__.py): `create_app` 을 정의합니다.
- [app/models.py](app/models.py): 데이터베이스 테이블을 모아둡니다.
- [app/main/__init__.py](app/main/__init__.py): `view`, `main`을 등록합니다.
- [app/main/views.py](app/main/views.py): 메인으로 라우팅되는 내용들을 모아둡니다.

## Blueprint

이번장에서 `flask-blueprint`라는 패키지를 설치합니다. 만약, 앱이 구동되기 전에 에러페이지들이 요청된다면 어떻게 될까요? 예를들어, 앱이 구동되기 전에 없는 url을 접근한다고 하면요? 그때를 위해 app 구동전에 blueprint 를 통해 에러페이지들을 등록합니다. 자세한것은 [app/__init__.py](app/__init__.py) 를 참조하세요.

```python
def create_app(config_name):
    app = Flask(__name__)
    # ...

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
```

## Test

메인 파일인 [flasky.py](flasky.py) 에 테스팅을 한다고 등록을 해둡니다.

```python
@app.cli.command()
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
```

그러면 `flask test`를 실행하면 테스트가 동작합니다. 참고로, [tests/test_basics.py](tests/test_basics.py) 를 보시면 아시겠지만 테스팅마다 데이터베이스를 새로 만들고 없앱니다.

```bash
(flasky) Macbook2017:Chapter07 sangmin$ flask test
test_app_exists (test_basics.BasicsTestCase) ... ok
test_app_is_testing (test_basics.BasicsTestCase) ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.014s

OK
```

## Database Setup

아직도 Database Migration 을 제대로 이해하지 못했습니다. 5장에서 만들어둔 `data.sqlite`파일을 `data-dev.sqlite`파일로 바꿔준 후에 구동하였습니다.
