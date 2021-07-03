#load the train and test file
#train the algo
# save the metrices,params

import os
import pandas as pd
import warnings
import sys
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import roc_auc_score,plot_confusion_matrix
import argparse
import joblib
import json
from urllib.parse import urlparse
from get_data import read_params
from sklearn.metrics import roc_auc_score,accuracy_score
import json

def train_and_evaluate(config_path):
    config = read_params(config_path)
    patient_train_path = config['split_data']['train_path']
    patient_test_path= config['split_data']['test_path']

    model_dir =config['model_dir']
    max_depth=config['estimators']['DecisionTreeClassifier']['params']['max_depth']
    criterion =config['estimators']['DecisionTreeClassifier']['params']['criterion']
    target_col=config['base']['target_col']

    train_df = pd.read_csv(patient_train_path,sep=',')
    test_df = pd.read_csv(patient_test_path, sep=',')
    print(train_df.head(5))

    train_y = train_df[target_col]
    test_y = test_df[target_col]

    train_x = train_df.drop(target_col, axis=1)
    test_x = test_df.drop(target_col, axis=1)

    model = DecisionTreeClassifier(max_depth=max_depth, criterion=criterion)
    model.fit(train_x, train_y)
    predict_DMIndicator = model.predict(test_x)
    roc_score = roc_auc_score(test_y,predict_DMIndicator)
    accuracy = accuracy_score(test_y,predict_DMIndicator)
    print("ROC score without Normalization is {}".format(roc_score))
    print("Accuracy is {}".format(accuracy))
    score_file = config['reports']["scores"]
    params_file = config['reports']['params']

    with open(score_file,"w") as f:
        scores = {
            "roc_score": roc_score,
            "accuracy" : accuracy
        }
        json.dump(scores,f,indent=4)

    with open(params_file,"w") as f:
        params = {
            "max_depth": max_depth,
            "criterion" : criterion
        }
        json.dump(params,f,indent=4)

    os.makedirs(model_dir, exist_ok=True)
    model_path = os.path.join(model_dir, "model.joblib")

    joblib.dump(model,model_path)




if __name__ == "__main__":
    args = argparse.ArgumentParser()
    default_config_path = os.path.join("params.yaml")
    args.add_argument("--config", default=default_config_path)
    parsed_args = args.parse_args()
    train_and_evaluate(config_path=parsed_args.config)
