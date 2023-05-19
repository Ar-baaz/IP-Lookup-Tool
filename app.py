from flask import Flask, render_template, request
import ipapi

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    search = request.form.get('search')
    data = ipapi.location(ip=search, output='json')
    return render_template("index.html", data=data)
    # return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
