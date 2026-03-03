from flask import Flask, Response

app = Flask(__name__)

@app.route('/', methods=['GET'])  # Корневой маршрут для GET-запроса
def index():
    # Чтение HTML-страницы index.html
    with open('index.html', 'r', encoding='utf-8') as file:
        html_content = file.read()
    return Response(html_content, content_type='text/html')

@app.route('/contacts', methods=['GET'])  # Маршрут для страницы контактов
def contacts():
    # Чтение HTML-страницы contacts.html
    with open('contacts.html', 'r', encoding='utf-8') as file:
        html_content = file.read()
    return Response(html_content, content_type='text/html')

@app.route('/catalog', methods=['GET'])  # Маршрут для каталога
def catalog():
    # Чтение HTML-страницы catalog.html
    with open('catalog.html', 'r', encoding='utf-8') as file:
        html_content = file.read()
    return Response(html_content, content_type='text/html')

@app.route('/category', methods=['GET'])  # Маршрут для категории
def category():
    # Чтение HTML-страницы category.html
    with open('category.html', 'r', encoding='utf-8') as file:
        html_content = file.read()
    return Response(html_content, content_type='text/html')

if __name__ == '__main__':
    app.run(debug=True)  # Запуск приложения
