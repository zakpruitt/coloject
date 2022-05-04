from flask import Flask, render_template, request
from color import generate_color_chart

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        return render_template('index.html')
    else:
        print(request.form["chartNameInput"])
        print(request.form["maxColorInput"])
        f = request.files["imageInput"]
        print(f.filename)
        f.save("./static/temp/" + f.filename)
        generate_color_chart(f)
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
