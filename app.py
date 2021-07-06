from flask import Flask,render_template,request,jsonify
import os
import yaml
import joblib
import numpy as np
#from src.get_data import read_params
params_path = "params.yaml"
webapp_root = "webapp"

static_dir = os.path.join(webapp_root, "static")
template_dir = os.path.join(webapp_root, "templates")

app = Flask(__name__)

def read_params(config_path):
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config


def predict(data):
    config = read_params(params_path)
    model_dir_path = config['webapp_model_dir']
    model = joblib.load(model_dir_path)
    prediction = model.predict(data)
    print("tttt")
    print(prediction[0])
    print(type(prediction[0]))
    return str(prediction[0])

def api_response(request):
    try:
        data = np.array([list(request.json.values())])
        response = predict(data)
        response = {"response":response}
        return response
    except Exception as e:
        print(e)
        error= {"error": "something went wrong!!! Try again"}
        return error

    @app.route("/",methods=["GET","POST"])
    def index():
        if request.method=="POST":
            try:
                if request.form:
                    data = dict(request.form).values()
                    data = [list(map(float, data))]
                    response = predict(data)
                    return render_template("index.html", response=response)

                # If Request is coming from API
                elif request.json:
                    response= api_response(request)
                    return jsonify(response)

            except Exception as e:
                print(e)
                error = {"error": "something went wrong!!! Try again"}
                return error

        else:
            return "RenderIndexTemplate"



if __name__=="__main__":
    app.run(host="0.0.0.0", port=6000, debug=True)
