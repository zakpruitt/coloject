from flask import Flask, render_template, request
from color import generate_color_chart

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        return render_template('index.html', chart_path="./static/colors.png")
    else:
        # get form data
        chart_name = request.form["chartNameInput"]
        n_color = request.form["maxColorInput"]
        img = request.files["imageInput"]

        # save temp and generate chart
        img.save("./static/temp/" + img.filename)
        generate_color_chart(chart_name, n_color, img)

        # load page with chart
        return render_template('index.html', chart_path="./static/temp/" + img.filename)


if __name__ == '__main__':
    app.run(debug=True)
