#split the Raw data
#save it in data/processed folder

import os
import argparse
import pandas as pd
from sklearn.model_selection import train_test_split
from get_data import read_params

def split_and_save_data(config_path):
    config = read_params(config_path)
    patient_train_path = config['split_data']['patient_train_path']
    patient_test_path = config['split_data']['patient_test_path']

    diagnosis_train_path = config['split_data']['diagnosis_train_path']
    diagnosis_test_path = config['split_data']['diagnosis_test_path']

    medication_train_path = config['split_data']['medication_train_path']
    medication_test_path = config['split_data']['medication_test_path']

    phy_sp_train_path = config['split_data']['phy_sp_train_path']
    phy_sp_test_path = config['split_data']['phy_sp_test_path']

    transcript_train_path = config['split_data']['transcript_train_path']
    transcript_test_path = config['split_data']['transcript_test_path']

    patient_raw_data_path = config['load_data']['patient']
    diagnosis_raw_data_path = config['load_data']['diagnosis']
    medication_raw_data_path = config['load_data']['medication']
    phy_sp_raw_data_path = config['load_data']['phy_sp']
    transcript_raw_data_path = config['load_data']['transcript']

    split_ratio = config['split_data']['test_size']
    random_state = config['base']['random_state']

    patient_df = pd.read_csv(patient_raw_data_path,sep=",")
    diagnosis_df = pd.read_csv(diagnosis_raw_data_path, sep=",")
    medication_df = pd.read_csv(medication_raw_data_path, sep=",")
    phy_sp_df = pd.read_csv(phy_sp_raw_data_path, sep=",")
    transcript_df = pd.read_csv(transcript_raw_data_path, sep=",")

    patient_df_train, patient_df_test = train_test_split(patient_df,test_size=0.2,random_state=random_state)
    diagnosis_df_train, diagnosis_df_test = train_test_split(diagnosis_df, test_size=0.2, random_state=random_state)
    medication_df_train, medication_df_test = train_test_split(medication_df, test_size=0.2, random_state=random_state)
    phy_sp_df_train, phy_sp_df_test = train_test_split(phy_sp_df, test_size=0.2, random_state=random_state)
    transcript_df_train, transcript_df_test = train_test_split(transcript_df, test_size=0.2, random_state=random_state)

    # storing the train test deta set in respective folder
    patient_df_train.to_csv(patient_train_path,sep=",",index=False,encoding="utf-8")
    patient_df_test.to_csv(patient_test_path, sep=",", index=False, encoding="utf-8")
    diagnosis_df_train.to_csv(diagnosis_train_path, sep=",", index=False, encoding="utf-8")
    diagnosis_df_test.to_csv(diagnosis_test_path, sep=",", index=False, encoding="utf-8")
    medication_df_train.to_csv(medication_train_path, sep=",", index=False, encoding="utf-8")
    medication_df_test.to_csv(medication_test_path, sep=",", index=False, encoding="utf-8")
    phy_sp_df_train.to_csv(phy_sp_train_path, sep=",", index=False, encoding="utf-8")
    phy_sp_df_test.to_csv(phy_sp_test_path, sep=",", index=False, encoding="utf-8")
    transcript_df_train.to_csv(transcript_train_path, sep=",", index=False, encoding="utf-8")
    transcript_df_test.to_csv(transcript_test_path, sep=",", index=False, encoding="utf-8")

if __name__ == "__main__":
    args = argparse.ArgumentParser()
    default_config_path = os.path.join("params.yaml")
    args.add_argument("--config", default=default_config_path)
    parsed_args = args.parse_args()
    split_and_save_data(config_path=parsed_args.config)
