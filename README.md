create env
```bash
conda create -n EHR_Analysis_new python=3.6 -y
```
activate the env
```bash
conda activate EHR_Analysis_new
```
create requirements.txt
install the Requirements
```bash
pip install -r requirements.txt
```
download the data from 

patient = pd.read_csv('https://raw.githubusercontent.com/kthouz/Diabetes-PracticeFusion/master/agg_data/patient.csv')
diagnosis = pd.read_csv('https://raw.githubusercontent.com/kthouz/Diabetes-PracticeFusion/master/agg_data/diagnosis.csv')
medication = pd.read_csv('https://raw.githubusercontent.com/kthouz/Diabetes-PracticeFusion/master/agg_data/medication.csv')
phy_sp = pd.read_csv('https://raw.githubusercontent.com/kthouz/Diabetes-PracticeFusion/master/agg_data/physician_specialty.csv')
transcript = pd.read_csv('https://raw.githubusercontent.com/kthouz/Diabetes-PracticeFusion/master/agg_data/transcript.csv')

bash

```buildoutcfg
git init
```
```buildoutcfg
dvc init
```

```buildoutcfg
dvc add data_given/*.csv
```
```buildoutcfg
dvc add data_given/*.csv
```
```buildoutcfg
git add .
```
