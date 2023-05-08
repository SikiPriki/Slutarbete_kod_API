import os
from flask import Flask, jsonify,request
from dotenv import load_dotenv
from flask_cors import CORS

# Load variables from .env
load_dotenv()
print(os.environ.get('HELLO'))

# Create Flask instance
app = Flask(__name__)

#Allowing acess for our localhost only 
CORS(app, resources={r'/*':{'origins':'http://127.0.0.1:5500'}})

#Allows UTF-8 in JSON
app.config['JSON_AS_ASCII']=False


#Test data
face_data=[
    {
        'id':0,
        'name':"smile",
        'mouth':"M94.872 212.333c19.031 12.602 48.523 48.825 103.565 1.134",
        'eb_right':"M169.9 126.155c12.29-15.431 23.867-13.79 35.152 0",
        'eb_left':"M85.423 126.155c11.717-15.672 23.434-14.558 35.151 0",
        'eye_left':"M121.33 159.606a34.71 34.71 0 0 1-.667 6.821c-2.036 10.144-8.497 17.558-16.153 17.558-7.81 0-14.376-7.715-16.27-18.174a34.864 34.864 0 0 1-.55-6.205c0-13.465 7.531-24.38 16.82-24.38 9.29 0 16.82 10.915 16.82 24.38z",
        'eye_right':"M203.918 159.795a34.81 34.81 0 0 1-.59 6.421c-1.944 10.349-8.474 17.958-16.23 17.958-7.498 0-13.85-7.111-16.021-16.935a34.547 34.547 0 0 1-.799-7.444c0-13.465 7.53-24.38 16.82-24.38s16.82 10.915 16.82 24.38z",
    },
    {
        'id':1,
        'name':"neutral",
        'mouth':"M94.872 212.333c22.127-1.937 59.462 4.567 104.321 4.914",
        'eb_left':"M85.423 126.155c11.717-15.672 23.434-14.558 35.151 0",
        'eb_right':"M169.9 126.155c12.85 1.53 25.29 2.454 35.152 0",#"M169.9 126.155h35.152",
        'eye_left':"M121.33 159.606a34.71 34.71 0 0 1-.667 6.821c-2.036 10.144-8.497 17.558-16.153 17.558-7.81 0-14.376-7.715-16.27-18.174a34.864 34.864 0 0 1-.55-6.205c0-13.465 7.531-24.38 16.82-24.38 9.29 0 16.82 10.915 16.82 24.38z",
        'eye_right':"M203.918 159.795a34.81 34.81 0 0 1-.59 6.421c-1.944 10.349-8.474 17.958-16.23 17.958-7.498 0-13.85-7.111-16.021-16.935a34.547 34.547 0 0 1-.799-7.444c0-13.465 7.53-24.38 16.82-24.38s16.82 10.915 16.82 24.38z",
    },
    {
        'id':2,
        'name':"sad",
        'mouth':"M94.872 212.333c19.771-10.327 51.52-44.077 103.565 1.134",
        'eb_left':"M85.423 126.155c8.83 3.298 19.312 12.53 35.151 0",
        'eb_right':"M169.9 126.155c10.616 6.973 21.556 11.896 35.152 0",
        'eye_left':"M121.33 159.606a34.71 34.71 0 0 1-.667 6.821c-2.036 10.144-8.497 17.558-16.153 17.558-7.81 0-14.376-7.715-16.27-18.174a34.864 34.864 0 0 1-.55-6.205c0-13.465 7.531 8.762 16.82 8.762 9.29 0 16.82-22.227 16.82-8.762z",
        'eye_right':"M203.918 159.795a34.81 34.81 0 0 1-.59 6.421c-1.944 10.349-8.474 17.958-16.23 17.958-7.498 0-13.85-7.111-16.021-16.935a34.547 34.547 0 0 1-.799-7.444c0-13.465 7.247 9.207 16.537 9.207s17.103-22.672 17.103-9.207z",
    }
    
]
# Default route to /
@app.route("/")
def index():
    return "Hello Flask!"

#Getting all the API data in face/all
@app.route('/face/all', methods=['GET'])
def faces():
    return jsonify(face_data)



#http://127.0.0.1:5000/face?name=smile
@app.route('/face',methods=['GET']) 
def get_name():
    if 'name' in request.args:
        name=str(request.args['name'])
    else:
        return "ERROR: Name needed"

    results = []
    for face in face_data:
        if face['name'] == name:
            results.append(face)

    # convert list of Python dictionaries to the JSON format
    return jsonify(results)


if __name__ == "__main__":
        app.run()