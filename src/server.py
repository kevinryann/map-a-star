from flask import Flask, request, render_template
import json

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

if __name__ == '__main__':
    app.run(debug=True)