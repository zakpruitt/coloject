from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        return render_template('index.html')
    else:
        print(request.form["chartNameInput"])
        print(request.form["maxColorInput"])
        f = request.files["imageInput"]
        f.save("./static/temp/" + f.filename)
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
