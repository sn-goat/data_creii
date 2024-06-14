from data_predictions import *

def followers_forecasting(model: DataPredictions, accuracy: float, data: np.array) -> None:
    print(model.model_name + ": ")
    model.train_model(accuracy)  # If needed.
    model.test_model()
    print("Data: ", end=" ")
    print(data)
    print(model.use_model(data))


def main() -> None:
    data_predictions_facebook = DataPredictions(
        data_path="data/data_facebook.csv", model_name="facebookmodel")

    data_predictions_instagram = DataPredictions(
        data_path="data/data_instagram.csv", model_name="instagrammodel")

    data_predictions_linkedin = DataPredictions(
        data_path="data/data_linkedin.csv", model_name="linkedinmodel")

    data_predictions_facebook.plot_data((5, 500), "Data Facebook")
    data_predictions_instagram.plot_data((5, 150), "Data Instagram")
    data_predictions_linkedin.plot_data((0, 400), "Data Linkedin")

    followers_forecasting(data_predictions_facebook, 0.98, [[150, 2000]])
    followers_forecasting(data_predictions_instagram, 0.80, [[2000]])
    followers_forecasting(data_predictions_linkedin, 0.0, [[2000]])






if __name__ == '__main__':
    main()