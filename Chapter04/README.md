# Chapter 04: Web Forms

[hello.py](hello.py) 에 bootstrap, wtf 를 사용해서 만듭니다.

## 실행

[Chapter 03](../Chapter03) 에서 설치한 bootstrap 을 사용합니다. 그리고, WTForms 를 설치합니다.

```bash
(flasky) Macbook2017:flasky sangmin$ pip install flask-wtf
```

[hello.py](hello.py) 를 실행시킵니다.

```bash
(flasky) Macbook2017:Chapter02 sangmin$ export FLASK_APP=hello.py
(flasky) Macbook2017:Chapter02 sangmin$ export FLASK_DEBUG=1
(flasky) Macbook2017:Chapter02 sangmin$ flask run
```

## Form을 만드는 두가지 방법

### [Flask-WTF](https://flask-wtf.readthedocs.io/en/stable/) 의 `wtf.quick_form(form)`

아래처럼 간단히 사용하실 수 있습니다. [index.html](templates/index.html) 을 참고하세요.

```html
{% import "bootstrap/wtf.html" as wtf %}
{{ wtf.quick_form(form) }}
```

### HTML form tag

조금 더 긴 코드를 html에 써주셔야 합니다. 참고로, [stackoverflow의 질문처럼](https://stackoverflow.com/questions/24234306/flask-wtform-forms-validate-on-submit-is-always-false) `form.hidden_tag()`이나 `form.csrf_token`을 써주는 것을 잊지 마세요.

```html
<form method="POST" action="/">
    {{ form.hidden_tag() }}
    {{ form.name.label }} {{ form.name() }}
    <input type="submit" value="Go">
</form>
```