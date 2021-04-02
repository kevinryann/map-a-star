from flask import Flask, request, render_template
import json

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def writeText() :
    if request.method == "POST":
        data = request.data.decode("utf8")
        jsonData = json.loads(data)
        longitude = jsonData["longitude"]
        latitude = jsonData["latitude"]
        with open("coordinate.txt",'w') as file :
            file.writelines("%f, %f" % (longitude, latitude))
    return render_template("coordinate.html")

if __name__ == '__main__':
    app.run(debug=True)