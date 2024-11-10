from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def submit():
    user_input = request.form['text']
    with open('data.txt', 'w') as file:
        file.write(user_input)
    return f'Данные {user_input} сохранены в файл.'


if __name__ == '__main__':
    app.run(debug=True)

