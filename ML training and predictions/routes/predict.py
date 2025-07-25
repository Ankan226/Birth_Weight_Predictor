# import os
# import pandas as pd
# import pickle
# from flask import Blueprint, request,jsonify, render_template
# from extensions import cache

# model_path =os.path.join("..","ML training and predictions" ,"model","model.pkl")
# with open(model_path, 'rb') as obj:
#     model = pickle.load(obj)

# predict_bp = Blueprint("predict",__name__)




# def get_cleaned_data(form_data):
#     gestation = float(form_data['gestation'])
#     parity = int(form_data['parity'])
#     age = float(form_data['age'])
#     height = float(form_data['height'])
#     weight = float(form_data['weight'])
#     smoke = float(form_data['smoke'])

#     cleaned_data = {"gestation":[gestation],
#                     "parity":[parity],
#                     "age":[age],
#                     "height":[height],
#                     "weight":[weight],
#                     "smoke":[smoke]
#                     }

#     return cleaned_data



# EXCPECTED_COLUMNS = ["gestation","parity","age","height","weight","smoke"]

# @app.route('/', methods=['GET'])
# def home():
#     return render_template("index.html")


# # define your endpoint
# @predict_bp.route("/predict", methods = ['POST'])
# @cache.cached(timeout=30, query_string=True)
# def get_prediction():
#     # get data from user
#     baby_data_form = request.form
#     baby_data_cleaned=get_cleaned_data(baby_data_form)

#     # convert into dataframe
#     baby_df = pd.DataFrame(baby_data_form)
#     baby_df = baby_df[EXCPECTED_COLUMNS]

#     # make prediciton on user data
#     prediction = model.predict(baby_df)
#     prediction = round(float(prediction), 2)

#     # return reponse in a json format
#     response = {"Prediction":prediction}
#     return render_template("index.html", prediction=prediction)


















import os
import pandas as pd
import pickle
from flask import Blueprint, request, jsonify, render_template
from extensions import cache

# Safe model path (adjust this to work both during dev and deployment)
model_path = os.path.join(os.path.dirname(__file__), '..', 'model', 'model.pkl')
model_path = os.path.abspath(model_path)

# Load ML model
with open(model_path, 'rb') as f:
    model = pickle.load(f)

# Create blueprint
predict_bp = Blueprint("predict", __name__)

# Expected columns for the model
EXPECTED_COLUMNS = ["gestation", "parity", "age", "height", "weight", "smoke"]

# Home page route (use the blueprint)
@predict_bp.route('/', methods=['GET'])
def home():
    return render_template("index.html")

# Function to clean form data
def get_cleaned_data(form_data):
    return {
        "gestation": [float(form_data['gestation'])],
        "parity": [int(form_data['parity'])],
        "age": [float(form_data['age'])],
        "height": [float(form_data['height'])],
        "weight": [float(form_data['weight'])],
        "smoke": [float(form_data['smoke'])]
    }

# Prediction route
@predict_bp.route('/predict', methods=['POST'])
@cache.cached(timeout=30, query_string=True)
def get_prediction():
    try:
        # Clean the data
        baby_data_cleaned = get_cleaned_data(request.form)

        # Convert to DataFrame
        baby_df = pd.DataFrame(baby_data_cleaned)[EXPECTED_COLUMNS]

        # Predict
        prediction = model.predict(baby_df)
        prediction = round(float(prediction), 2)

        # Return prediction in the HTML
        return render_template("index.html", prediction=prediction)

    except Exception as e:
        return jsonify({"error": str(e)}), 400
