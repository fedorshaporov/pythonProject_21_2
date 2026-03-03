from flask import Flask, Response, request, render_template_string

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def contacts():
    if request.method == 'POST':
        # Получение данных из формы
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # Печать полученных данных в консоль
        print(f"Имя: {name}, Почта: {email}, Сообщение: {message}")

        # Возвращаем пользователю сообщение об успешной отправке (можно настраивать по желанию)
        return f"Спасибо, {name}! Ваше сообщение отправлено."

    # Если GET-запрос, считываем HTML-файл
    with open('contacts.html', 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Возвращаем HTML с нужным типом контента
    return Response(html_content, content_type='text/html')

if __name__ == '__main__':
    app.run(debug=True)  # Запускаем приложение