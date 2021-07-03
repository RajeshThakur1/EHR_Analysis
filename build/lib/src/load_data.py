# read the data from the data source
# save it in the data/raw for the further process

import os
from get_data import read_params,get_data
import argparse

def load_and_save(config_path):
    config = read_params(config_path)
    patient_df, dignosis_df, medication_df, phy_df, transcript_df = get_data(config_path)
    new_col = [col for col in patient_df.columns]
    patient_raw_data_path = config['load_data']['patient']
    diagnosis_raw_data_path = config['load_data']['diagnosis']
    medication_raw_data_path = config['load_data']['medication']
    phy_sp_raw_data_path = config['load_data']['phy_sp']
    transcript_raw_data_path = config['load_data']['transcript']
    patient_df.to_csv(patient_raw_data_path,sep=",", index=False)
    dignosis_df.to_csv(diagnosis_raw_data_path, sep=",", index=False)
    medication_df.to_csv(medication_raw_data_path, sep=",", index=False)
    phy_df.to_csv(phy_sp_raw_data_path, sep=",", index=False)
    transcript_df.to_csv(transcript_raw_data_path, sep=",", index=False)

    print(new_col)


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    default_config_path = os.path.join("params.yaml")
    args.add_argument("--config", default=default_config_path)
    parsed_args = args.parse_args()
    load_and_save(config_path=parsed_args.config)