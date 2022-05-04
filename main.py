import os
from flask import Flask, render_template, request
from color_chart import generate_color_chart
from color_model import Color

app = Flask(__name__)
color_db = Color()

@app.route('/', methods=['GET', 'POST'])
def index():
    # get top colors
    top_colors = color_db.get_top_colors()
    print(top_colors)

    if request.method == "GET":
        return render_template('index.html', chart_path="./static/colors.png", top_colors=top_colors)
    else:
        # get form data
        chart_name = request.form["chartNameInput"]
        n_color = request.form["maxColorInput"]
        img = request.files["imageInput"]

        # save temp and generate chart
        img.save("./static/temp/" + img.filename)
        generate_color_chart(chart_name, n_color, img)
    
        # load page with chart
        return render_template('index.html', chart_path="./static/temp/" + img.filename, top_colors=top_colors)


def empty_temp():
    for filename in os.listdir("./static/temp"):
        os.remove("./static/temp/" + filename)


if __name__ == '__main__':
    empty_temp()
    app.run(debug=True)
