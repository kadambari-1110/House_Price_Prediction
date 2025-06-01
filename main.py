from flask import *
import numpy as np
from train_model import train_model

model , features = train_model()

main = Flask(__name__)

@main.route("/")
def home():
    return render_template("index.html")


@main.route("/calculate",methods=["GET","POST"])
def calculate():
    if request.method == "POST":

        bedrooms = int(request.form["bedroom"])
        bathrooms = int(request.form["bathroom"])
        balconies = int(request.form["balcony"])
        parkings = int(request.form["parking"])
        area = float(request.form["area"])
        location = request.form["location"]
        dependent_data = {"bedrooms":bedrooms,"bathrooms":bathrooms,"balconies":balconies,"parkings":parkings,"area":area}

        for i in features:
            if i.startswith("location_"):
                if i == "location_"+location:
                    dependent_data[i] = 1
                else:
                    dependent_data[i]=0

        temp = np.array([[dependent_data[i] for i in features]])
        price = model.predict(temp)[0]
        price = max(price,0)

        return render_template("show.html", prediction=round(price, 2))
    

@main.route("/go_home" , methods=["GET","POST"])
def go_home():
    if request.method=="POST":
        return redirect(url_for("home"))


if __name__ == "__main__" :
    main.run(debug=True)