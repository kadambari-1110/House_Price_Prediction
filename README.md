#  House Price Prediction Web App

## Project Overview

This is a web-based House Price Prediction system developed using Flask, HTML/CSS/JS, and a machine learning model (Linear Regression using scikit-learn). It predicts the approximate price of a house based on user inputs like the number of bedrooms, bathrooms, area, and location.

---

## Technologies Used

* **Frontend**: HTML, CSS, JavaScript
* **Backend**: Python with Flask
* **Machine Learning**: Scikit-learn (Linear Regression)
* **Dataset**: CSV File (stored locally)

---

## Machine Learning Model

* **Algorithm**: Linear Regression
  
* **Input Features**:
  * Bedrooms
  * Bathrooms
  * Balconies
  * Parking
  * Area (in sq. ft.)
  * Location (One-Hot Encoded)
    
* **Output**:
  * Predicted House Price

### Training Function:

```python
def train_model_from_csv():
    df = pd.read_csv("house_data.csv")
    df = pd.get_dummies(df, columns=["location"])
    X = df.drop("price", axis=1)
    y = df["price"]
    model = LinearRegression()
    model.fit(X, y)
    return model, X.columns
```

---

## Web Interface Routes

### 1. `/` (Home Page)

* Displays a welcome message
* Link to navigate to the prediction form

### 2. `#second` (Prediction Form)

* Takes input from the user:

  * Bedrooms, Bathrooms, Balconies, Parking, Area, Location

### 3. `/calculate` (Prediction Logic)

* Fetches form data
* Applies one-hot encoding for location
* Predicts price using the trained model
* Renders result on `show.html`

---

## Folder Structure

```
project/
│
├── static/
│   ├── css/
│   │   └── mysheet.css
│   ├── javascript/
│   │   └── myscript.js
│   └── images/
│       └── img1.jpg
│
├── templates/
│   ├── index.html
│   ├── show.html
│
├── data.csv
├── main.py
```

---

## Features

* Live house price prediction
* Basic frontend validations using JavaScript
* CSS styling with gradients, flexbox, and shadows
* Model trained at runtime from CSV file

---

## How to Use the Project

1. Clone or download this repository to your local machine.
2. Place the `data.csv` file in the root directory (beside `main.py`). 
3. Install required packages:

```bash
pip install flask pandas scikit-learn numpy
```

4. Run the application:

```bash
python main.py
```

5. Open your browser and navigate to:

```
http://127.0.0.1:5000
```

6. Fill out the house details in the form and submit to get a predicted price.

---

