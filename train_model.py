import pandas as pd
from sklearn.linear_model import LinearRegression

def train_model():
    data = pd.read_csv("data.csv")

    df = pd.DataFrame(data)

    df = pd.get_dummies(df,columns=['location'])
    x = df.drop("price", axis=1)  
    y = df["price"]               


    model = LinearRegression()
    model.fit(x, y)

    return model,x.columns


