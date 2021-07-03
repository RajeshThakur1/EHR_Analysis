import pandas as pd
from get_data import read_params
from sklearn.preprocessing import StandardScaler
from statsmodels.stats.outliers_influence import variance_inflation_factor
import argparse
import os
import numpy as np


def get_highly_correlated_cols( dataframe, threshol_vif=5):
    scaler = StandardScaler()
    dataframe = dataframe.select_dtypes(exclude=['object'])
    X_scaled = scaler.fit_transform(dataframe)

    variables = X_scaled

    # we create a new data frame which will include all the VIFs
    # note that each variable has its own variance inflation factor as this measure is variable specific (not model specific)
    # we do not include categorical values for mulitcollinearity as they do not provide much information as numerical ones do
    vif = pd.DataFrame()

    # here we make use of the variance_inflation_factor, which will basically output the respective VIFs
    vif["VIF"] = [variance_inflation_factor(variables, i) for i in range(variables.shape[1])]
    # Finally, I like to include names so it is easier to explore the result
    vif["Features"] = dataframe.columns
    highly_corelated_features = list(vif[vif['VIF'] > threshol_vif]['Features'])
    return highly_corelated_features


def drop_highly_corelated_cols(dataframe, col_list):
    return dataframe.drop(col_list, axis=1)

def data_load(config_path):
    '''
                        Method Name: data_load
                            Description: This method loads the data from the file and convert into a pandas dataframe
                            Output: Returns a Dataframes, which is our data for training
                            On Failure: Raise Exception .
        '''
    try:

        config = read_params(config_path)
        transcript_raw_data_path = config['load_data']['transcript']
        transcript = pd.read_csv(transcript_raw_data_path,sep=",")
        highly_corelated_cols = get_highly_correlated_cols(transcript)
        non_corelated_df = drop_highly_corelated_cols(transcript, highly_corelated_cols)
        transcript_df_without_PatientGuide = transcript.drop(['PatientGuid'], axis=1)

        #fetching the Target column
        target_var = config['base']['target_col']

        patient_raw_data_path = config['load_data']['patient']
        patient = pd.read_csv(patient_raw_data_path,sep=",")
        target = patient[target_var]
        assert non_corelated_df.shape[0] == target.shape[0], 'Target column and dataset shapes are not matching'
        non_corelated_df.drop(['PatientGuid'], axis=1, inplace=True)
        concatenated_df = pd.concat([patient[['Age', 'Gender',target_var]], non_corelated_df], axis=1)
        #print(concatenated_df.head())
        concatenated_df_path = config['split_data']['concatenated_df']
        concatenated_df.to_csv(concatenated_df_path,index=False,encoding='utf-8')
        return concatenated_df

    except Exception as e:
        raise e







if __name__ == "__main__":
    args = argparse.ArgumentParser()
    default_config_path = os.path.join("params.yaml")
    args.add_argument("--config", default=default_config_path)
    parsed_args = args.parse_args()
    #data = data_getter()
    data_load(config_path=parsed_args.config)


