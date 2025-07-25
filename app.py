from flask import Flask, render_template, request
import pickle
import numpy as np
import requests
import geopy.geocoders

app = Flask(__name__)

# Load your trained model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

# Function to get latitude and longitude using OpenStreetMap (Nominatim API)

def get_lat_lon(city):
    geolocator = geopy.geocoders.Nominatim(user_agent="address_geocoder")
    location = geolocator.geocode(city)
    try:
        if location:
            lon = location.longitude
            lat= location.latitude
            return lat, lon
        else:
            return None, None
    except Exception as e:
        print(f"Error fetching lat/lon: {e}")
    return None, None
    #url = f"https://nominatim.openstreetmap.org/search?q={city}&format=json"

    #try:
    #    response = requests.get(url)
        
        # Debugging prints
        #print("Status Code:", response.status_code)
        #print("Response Text:", response.text)

        #if response.status_code == 200:
        #    data = response.json()

        #    if data:  # Check if data is not empty
        #        lat = data[0]['lat']
        #        lon = data[0]['lon']
        #        return lat, lon
        #    else:
        #        print("No data found for the city")
        #        return None, None
        #else:
        #    print(f"API request failed with status code {response.status_code}")
        #    return None, None
    #except Exception as e:
        #print(f"Error fetching lat/lon: {e}")
        #return None, None


@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = None
    city = None
    if request.method == 'POST':
        city = request.form['city']
        lat, lon = get_lat_lon(city)

        if lat is not None and lon is not None:
            input_data = np.array([[lat, lon]])
            prediction = model.predict(input_data)[0]
        else:
            error_message = "City not found or invalid. Please try again."

    return render_template('index.html', prediction=prediction, city=city)

if __name__ == '__main__':
    app.run(debug=True)
