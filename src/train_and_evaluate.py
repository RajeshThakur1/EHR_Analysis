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
import json

def train_and_evaluate(config_path):
    config = read_params(config_path)
    patient_train_path = config['split_data']['patient_train_path']
    patient_test_path= config['split_data']['patient_test_path']
    diagnosis_train_path= config['split_data']['diagnosis_train_path']
    diagnosis_test_path= config['split_data']['diagnosis_test_path']
    medication_train_path= config['split_data']['medication_train_path']
    medication_test_path= config['split_data']['medication_test_path']
    phy_sp_train_path = config['split_data']['phy_sp_train_path']
    phy_sp_test_path= config['split_data']['phy_sp_test_path']
    transcript_train_path= config['split_data']['transcript_train_path']
    transcript_test_path= config['split_data']['transcript_test_path']
    random_state= config['base']['random_state']
    model_dir =config['model_dir']
    max_depth=config['estimators']['DecisionTreeClassifier']['params']['max_depth']
    criterion =config['estimators']['DecisionTreeClassifier']['params']['criterion']
    target_col=config['base']['target_col']

    patient_train_df = pd.read_csv(patient_train_path,sep=',')
    patient_test_df = pd.read_csv(patient_test_path, sep=',')
    transcript_train_df = pd.read_csv(transcript_train_path, sep=',')
    transcript_test_df = pd.read_csv(transcript_test_path, sep=',')

if __name__ == "__main__":
    if __name__ == "__main__":
        args = argparse.ArgumentParser()
        default_config_path = os.path.join("params.yaml")
        args.add_argument("--config", default=default_config_path)
        parsed_args = args.parse_args()
        train_and_evaluate(config_path=parsed_args.config)
