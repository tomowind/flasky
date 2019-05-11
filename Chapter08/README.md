# Chapter 08: User Authentication

## 개요

7단원의 내용에서 + 로그인 스크린과 새 유저 등록 페이지를 제공합니다. [메인의 화면](app/templates/index.html) 에서는 로그인한 유저 이름만 찍어줍니다. 

```bash
(flasky) Macbook2017:Chapter08 sangmin$ tree | grep -v pyc | grep -v __pyceche__ 
.
├── app
│   ├── __init__.py
│   ├── auth
│   │   ├── __init__.py
│   │   ├── forms.py
│   │   └── views.py
│   ├── main
│   │   ├── __init__.py
│   │   ├── errors.py
│   │   ├── forms.py
│   │   └── views.py
│   ├── models.py
│   └── templates
│       ├── auth
│       │   ├── login.html
│       │   └── register.html
│       ├── base.html
│       └── index.html
├── config.py
├── flasky.py
└── tests
    ├── __init__.py
    ├── test_basics.py
    └── test_user_model.py

```

중요한 파일들은 다음입니다.

- [app/__init__.py](app/__init__.py): login auth 페이지를 정의합니다.
- [app/models.py](app/models.py): `User` 테이블에 패스워드 정보를 담도록 확장합니다.
- [app/auth/forms.py](app/auth/forms.py): `LoginForm`, `RegistrationForm` 구현
- [app/auth/views.py](app/auth/views.py): `login()`, `logout()`, `register()` 구현
- [app/templates/auth/login.html](app/templates/auth/login.html): `LoginForm` 보여주기
- [app/templates/auth/register.html](app/templates/auth/register.html): `RegistrationForm` 보여주기
- [app/templates/base.html](app/templates/base.html): `login`, `logout` 메뉴 상단우측에 표시

## 로그인 과정 (책의 113페이지)

1. [http://127.0.0.1:5000/auth/login](http://127.0.0.1:5000/auth/login) 에서 "Log In" 클릭
2. [app/templates/auth/login.html](app/templates/auth/login.html) 화면에서 정보넣고 Submit 클릭
    1. [app/auth/views.py](app/auth/views.py) 에서 로그인 로직 동작
    2. [app/models.py](app/models.py) 에서 `werkzeug` 를 통해 password hash 비교
    3. `flask_login.login_user()` 가 `User` 객체에서 id 를 뽑아내어 세션 업데이트
    4. [app/auth/views.py](app/auth/views.py) 에서 메인 페이지로 redirect
3. Main page 로 redirect
    1. [app/templates/index.html](app/templates/index.html) 에서 `current_user` 체크
    2. `flask_login._get_user()` 호출
    3. `current_user` 가 존재하면 렌더링 해줌
    
## 스킵

새 유저를 등록할 때에 email verification 하는 과정이 흥미롭습니다. `itsdangerous` 를 사용해서 토큰을 발행한 후에 이메일 컨펌을 하는데요. 테스트할 이메일 발송 서버가 없어서 이 과정을 스킵합니다.

## DB Migration

이번 단원에서 DB Migration 을 알아낸 것 같습니다. 이번장의 `User` 테이블은 기존장에서 몇몇 컬럼을 추가한 형태인데요. 기존장의 `data-dev.sqlite`를 카피해도 바로 안됩니다. 
[models.py](app/models.py) 를 업데이트 한 후에 마이그레이션 커맨드를 실행하시면 됩니다.

```bash
(flasky) Macbook2017:Chapter08 sangmin$ flask db init
  Creating directory /Users/sangmin/git/flasky/Chapter08/migrations ... done
  Creating directory /Users/sangmin/git/flasky/Chapter08/migrations/versions ... done
  Generating /Users/sangmin/git/flasky/Chapter08/migrations/script.py.mako ... done
  Generating /Users/sangmin/git/flasky/Chapter08/migrations/env.py ... done
  Generating /Users/sangmin/git/flasky/Chapter08/migrations/README ... done
  Generating /Users/sangmin/git/flasky/Chapter08/migrations/alembic.ini ... done
  Please edit configuration/connection/logging settings in '/Users/sangmin/git/flasky/Chapter08/migrations/alembic.ini' before proceeding.
(flasky) Macbook2017:Chapter08 sangmin$ flask db migrate -m "initial migration"
INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.autogenerate.compare] Detected added column 'users.email'
INFO  [alembic.autogenerate.compare] Detected added column 'users.password_hash'
INFO  [alembic.autogenerate.compare] Detected added index 'ix_users_email' on '['email']'
  Generating /Users/sangmin/git/flasky/Chapter08/migrations/versions/bcdb7244bb2b_initial_migration.py ... done
(flasky) Macbook2017:Chapter08 sangmin$ flask db upgrade
INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade  -> bcdb7244bb2b, initial migration
```

```bash
>>> users = User.query.all()
>>> for user in users:
...     print(user.id, user.email, user.username, user.password_hash, user.role_id)
... 
1 None john None 1
2 None susan None 3
3 None david None 3
4 None sangmin None None
5 None user None None
6 None jenny None None
7 None caleb None None
```

