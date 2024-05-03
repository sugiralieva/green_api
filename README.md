## Сайт для взаимодействия с GREEN-API

Сайт развернут на хостинге Heroku.com и находится по адресу: https://green-api1-57149785c644.herokuapp.com

Для разработки сайта использовался следующий стек: Python - фреймворк Flask, HTML/CSS, GREEN-API.

На сайте есть форма, где нужно ввести idInstance и ApiTokenInstance и получить настройки либо состояние инстанса, также можно отправить сообщение или файл, использовав номер телефона, текст сообщения или ссылку на файл соответственно.
### Инструкция по инициализации сайта у себя на компьютере:
1. Установите python.
2. Создайте директорию для проекта и установите виртуальное окружение перейдя в директорию проекта и набрав в терминале: python -m venv venv для windows, либо python3 -m venv venv для Linux
2. Активируйте виртуальное окружение: venv\Scripts\activate для Windows и source venv/bin/activate для Linux
2. Установите git и наберите в терминале: git clone https://github.com/sugiralieva/tengrinews_clone
3. Установите все зависимости с помощью команды pip install -r requirements.txt
4. Запустите приложение main.py

### **Дополнительно:**

Для корректной работы API нужно передать три параметра: APIUrl, idInstance, apiTokenInstance.

Пример: GET {{APIUrl}}/waInstance{{idInstance}}/getSettings/{{apiTokenInstance}}

Но в предложенном макете нет поля ввода для APIUrl и по условиям задания требуется придерживаться макета, поэтому при возникновении ошибки укажите свой APIUrl в main.py в переменной apiurl (22 строка)