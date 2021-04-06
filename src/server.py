from flask import Flask, request, render_template
import json
import webbrowser
from threading import Timer

# template
app = Flask(__name__)

# server on route '/' with both methods (get and post)
@app.route('/', methods=["GET", "POST"])
def writeText() :
    # if the map is clicked
    if request.method == "POST":
        # get data from frontend and make it into json
        data = request.data.decode("utf8")
        jsonData = json.loads(data)
        # get data from json
        longitude = jsonData["longitude"]
        latitude = jsonData["latitude"]
        with open("./coordinate/coordinate.txt",'a') as file :
            # write into coordinate.txt (in ./coordinate) the coordinate that was clicked
            file.writelines("%f, %f\n" % (latitude, longitude))
    # if the web is refreshed or just started
    else:
        with open("./coordinate/coordinate.txt", "w") as file:
            # clear coordinate.txt (in ./coordinate)
            file.writelines("")
    # show the map
    return render_template("coordinate.html")

# to automatically open browser
def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000")

if __name__ == '__main__':
    Timer(1, open_browser).start()
    app.run(port=5000)