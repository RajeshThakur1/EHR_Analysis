## read the parameters
# processed
# return the dataframe
import os
import yaml
import pandas as pd
import argparse
def read_params(config_path):
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config

def get_data(config_path):
    config = read_params(config_path)
    patient_raw_datapath = config['data_source']["s3_bucket_patient"]
    patient_df = pd.read_csv(patient_raw_datapath, sep=',', encoding='utf-8')
    dignosis_raw_datapath = config['data_source']["s3_bucket_diagnosis"]
    dignosis_df = pd.read_csv(dignosis_raw_datapath, sep=',', encoding='utf-8')
    medication_raw_datapath = config['data_source']["s3_bucket_medication"]
    medication_df = pd.read_csv(medication_raw_datapath, sep=',', encoding='utf-8')
    phy_raw_datapath = config['data_source']["s3_bucket_phy_sp"]
    phy_df = pd.read_csv(phy_raw_datapath, sep=',', encoding='utf-8')
    transcript_raw_datapath = config['data_source']["s3_bucket_transcript"]
    transcript_df = pd.read_csv(transcript_raw_datapath, sep=',', encoding='utf-8')
    #print(patient_df.head())
    #extra comments
    return patient_df,dignosis_df,medication_df,phy_df,transcript_df


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    default_config_path = os.path.join("params.yaml")
    args.add_argument("--config", default=default_config_path)
    parsed_args = args.parse_args()
    get_data(config_path=parsed_args.config)
    #args.add_argument("--datasource", default=None)
