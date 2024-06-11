import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle
import plotly.express as px

class DataPredictions:
    def __init__(self, data_path: str, model_name) -> None:
        self.__data_path = data_path
        self.__model_name = model_name

    @property
    def model_name(self):
        return self.__model_name
    def __preprocess_data(self) -> tuple:
        df = pd.read_csv(self.__data_path, sep=",", header=0)
        df = df.drop(columns=["Date"])
        Y = df["Followers (Total)"]
        X = df.drop(columns=["Followers (Total)"])

        return train_test_split(X.to_numpy(), Y.to_numpy(), test_size=0.4)

    def train_model(self, best: float) -> None:
        while True:
            X_train , X_test , Y_train ,Y_test = self.__preprocess_data()

            linear = LinearRegression()
            linear.fit(X_train, Y_train)
            accuracy = linear.score(X_test, Y_test)
            print(accuracy)

            if accuracy > best:
                print("Accuracy:", end=" ")
                print(accuracy)

                break
        with open(self.__model_name + ".pickle", "wb") as f:
            pickle.dump(linear, f)

        print("\n")
    def __open_model(self):
        pickle_in = open(self.__model_name + ".pickle", "rb")
        linear = pickle.load(pickle_in)
        return linear

    def test_model(self) -> None:
        x_test = self.__preprocess_data()[1]
        y_test = self.__preprocess_data()[3]

        linear = self.__open_model()
        predictions = linear.predict(x_test)

        print("Co: \n", linear.coef_)
        print("Intercept: \n", linear.intercept_)
        print("\n")

        print("Testing model...")
        for x in range(len(predictions)):
            print(predictions[x], x_test[x], y_test[x])

        print("\n")
    def use_model(self, data: np.array) -> None:
        """"To predict the number based on various varibles.
           The sata should have this format: [[Followers (28 jours), Interactions]]
           Ex: [[10, 61]] """

        linear = self.__open_model()
        predictions = linear.predict(data)

        print("Followers prediction: ", end=" ")
        print(predictions)
        print("\n")

    def plot_data(self, data_range: tuple [int, int], title_plot: str) -> None:
        df = pd.read_csv(self.__data_path, sep=",", header=0)
        dates = df["Date"].tolist()
        data_types = df.columns.tolist()
        data_types.remove('Date')

        graph = px.line(df,x=dates,y=data_types, markers=True, range_y=data_range, width=1100, height=350)
        graph.update_layout(
        title= title_plot,
        xaxis_title="Dates",
        yaxis_title="Data",
        legend_title= "Variables")

        graph.show()
