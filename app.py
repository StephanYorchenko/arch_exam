from flask import Flask, render_template, request, Markup
import os

app = Flask(__name__)
import dict_words


def is_active_page(index, title):
    return int(index) + 1 == int(title)


def tool_for(word: str) -> str:
    if word in app.config['DICTIONARY'].keys():
        return app.config['DICTIONARY'][word]
    return ":("


def task_name(index) -> str:
    try:
        if isinstance(index, str):
            index = int(index) - 1
        return app.config['NAMES'][index]
    except IndexError:
        return "404"


@app.route('/arch', methods=['GET'])
def hello_world():
    current_id = request.args.get('task')
    return render_template(f'{current_id}.html',
                           title=current_id,
                           names=range(36),
                           tool_for=tool_for,
                           task_name=task_name,
                           is_active_page=is_active_page)


@app.errorhandler(404)
@app.errorhandler(500)
def not_found_error(error):
    return render_template('404.html',
                           title="404",
                           names=range(36),
                           tool_for=tool_for,
                           task_name=task_name,
                           is_active_page=is_active_page), 404


if __name__ == '__main__':
    app.run()
