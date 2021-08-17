from content_getter import ContentGetter
from handler import CSVHandler
from flask import Flask, request, render_template

DATA_STORAGE = 'data.csv'

app = Flask(__name__)
app.content_dict = CSVHandler.get_data_from(DATA_STORAGE)


@app.route("/", methods=["GET"])
def get_content():
    """
    Основной метод получения контента
    """
    categories: list = request.args.getlist('category')
    content_getter = ContentGetter()
    return render_template('show.html', image=content_getter.get_by_categories(categories), msg=content_getter.msg)


if __name__ == '__main__':
    app.run()
