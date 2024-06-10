import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle
import plotly.express as px



def preprocess_data(path: str="data_facebook.csv") -> tuple:
    df = pd.read_csv(path, sep=",", header=0)
    df = df.drop(columns=["Date"])
    Y = df["Followers(Total)"]
    X = df.drop(columns=["Followers(Total)"])


    return train_test_split(X.to_numpy(), Y.to_numpy(), test_size=0.5)
def train_model(model, best: float) -> None:
    while True:
        X_train , X_test , Y_train ,Y_test = preprocess_data()

        linear = model
        linear.fit(X_train, Y_train)
        accuracy = linear.score(X_test, Y_test)
        print(accuracy)

        if accuracy > best:
            break
    with open('facebookmodel.pickle', 'wb') as f:
        pickle.dump(linear, f)


def open_model():
    pickle_in = open('facebookmodel.pickle', 'rb')
    linear = pickle.load(pickle_in)

    print("Co: \n", linear.coef_)
    print("Intercept: \n", linear.intercept_)

    return linear
def test_model() -> None:
    x_test = preprocess_data()[1]
    y_test = preprocess_data()[3]

    linear = open_model()
    predictions = linear.predict(x_test)

    for x in range(len(predictions)):
        print(predictions[x], x_test[x], y_test[x])

def use_model(data: np.array) -> None:

    linear = open_model()
    predictions = linear.predict(data)
    print(predictions)

def plot_data(range: tuple, title: str, path: str="data_facebook.csv") -> None:
    df = pd.read_csv(path, sep=",", header=0)
    dates = df["Date"].tolist()
    data_types = df.columns.tolist()
    data_types.remove('Date')
    graph = px.line(df,x=dates,y=data_types, markers=True, range_y=range, width=1100, height=350)
    graph.update_layout(
        title= title,
        xaxis_title="Dates",
        yaxis_title="Data",
        legend_title= "Variable")

    graph.show()

