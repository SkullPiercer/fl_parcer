# О проекте:
## Проект для получения актуальных вакансий и заказов с фриланс бирж.

## Автор проекта:
### GitHub [SkullPiercer](https://github.com/)

## Стек:
```python
  beautifulsoup4==4.12.3
```
```python
  pyTelegramBotAPI==4.20.0
```
```python
  requests==2.32.3
```
# Как запустить проект.
### **Клонировать репозиторий и перейти в него в командной строке:**
```python 
  git clone git@github.com:SkullPiercer/fl_parcer.git
```
```python
  cd fl_parcer
```
### **Cоздать и активировать виртуальное окружение:**
#### Windows:
```python
  python -m venv venv
```
```python
  source venv/Scripts/activate
```
#### Linux/Mac:
```python
  python3 -m venv env
```
```python
  source env/bin/activate
```
### **Установить зависимости из файла requirements.txt:**
#### Windows:
```python
  python -m pip install --upgrade pip
```
```python
  pip install -r requirements.txt
```
#### Linux/Mac
```python
  python3 -m pip install --upgrade pip
```
```python
  pip install -r requirements.txt
```
### **Создать и заполнить файл .env:**
```python
  toucn .env
```
В файле потребуются следующие значения:
```python
TOKEN=Тут ваш токен для работы с телеграм ботом
USER_AGENT=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3 - Я использовал такие заголовки, чтобы имитировать запросы браузера
Далее ссылки с которых все парсится
HH=https://hh.ru/search/vacancy?text=Python&from=suggest_post&area=160&hhtmFrom=main&hhtmFromLabel=vacancy_search_line
HABR=https://freelance.habr.com/tasks?q=python
FLRU=https://freelance.ru/project/search/pro?c=&c%5B%5D=116&q=python&m=or&e=&a=0&a=1&v=0&v=1&f=&t=&o=0&o=1&b=
```
### **Запустить проект:**
#### Windows:
```python
  python main.py
```

### Хост:
При попытке поставить сайт на pythonanywhere будет возникать ошибка работы с прокси серверами, если кто знает как это оперативно можно решить, буду ждать pull request'ов