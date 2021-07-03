#split the Raw data
#save it in data/processed folder

import os
import argparse
import pandas as pd
from sklearn.model_selection import train_test_split
from get_data import read_params
from data_getter import data_load
def split_and_save_data(config_path):
    config = read_params(config_path)
    data = data_load(config_path)
    train_path = config['split_data']['train_path']
    test_path = config['split_data']['test_path']

    split_ratio = config['split_data']['test_size']
    random_state = config['base']['random_state']

    #df = pd.read_csv(data,sep=",")

    train_df, test_df = train_test_split(data,test_size=0.2,random_state=random_state)

    # storing the train test deta set in respective folder
    train_df.to_csv(train_path,sep=",",index=False,encoding="utf-8")
    test_df.to_csv(test_path, sep=",", index=False, encoding="utf-8")


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    default_config_path = os.path.join("params.yaml")
    args.add_argument("--config", default=default_config_path)
    parsed_args = args.parse_args()
    split_and_save_data(config_path=parsed_args.config)
