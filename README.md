# Ebola-casuality-predictor
This is the model trained to predict the death cases of inknown loacatin based on Latitude and longitude also were taken into account of the humidity temperature and nearby access to medical facilities.
It was originally integrated with [Ai-ne-Bola](https://github.com/AdityaShome/ai-ne-bola)

This project is a web application that predicts the death rate for a given city using its geographic location (latitude and longitude). The prediction is powered by a pre-trained machine learning model.

## Features

- Enter a city name to get its predicted death rate.
- Uses OpenStreetMap (Nominatim) to geocode city names to latitude and longitude.
- Powered by Flask and a pre-trained model (`model.pkl`).

## How It Works

1. User enters a city name in the web form.
2. The app fetches the latitude and longitude of the city using the Nominatim geocoding API.
3. These coordinates are passed to the machine learning model to predict the death rate.

## Setup Instructions

1. **Clone the repository** and navigate to the project directory.

2. **Install dependencies** (preferably in a virtual environment):

    ```bash
    pip install flask numpy geopy
    ```

3. **Ensure you have the following files:**
    - `model.pkl` (the trained model)
    - `train_data.xlsx` and `test_points.xlsx` (data files)

4. **Run the application:**

    ```bash
    python app.py
    ```

5. **Open your browser** and go to `http://127.0.0.1:5000/` to use the app.

## Notes

- The app requires internet access to use the Nominatim geocoding service.
- The model expects input as latitude and longitude; ensure your `model.pkl` is compatible.
- For best results, use well-known city names.

## Example

1. Enter "Lagos" in the input box.
2. Click "Predict".
3. The app will display the predicted death rate for Lagos.
