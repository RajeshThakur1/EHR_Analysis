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

```bash
git init
```
```bash
dvc init
```

```bash
dvc add data_given/*.csv
```
```bash
dvc add data_given/*.csv
```
```bash
git add .
```
```bash
git commit -m "first commit"
```
```bash
git add . && git commit -m "updated README.md"
```
<p> How to push the code in gitHub</p>
```buildoutcfg
git remote add origin https://github.com/RajeshThakur1/EHR_Analysis.git
```
<p> Rename your Current branch main</p>

```bash
git branch -M main
```
<p> Now push your Entire code to the main branch</p>

```bash
git push -u origin main
```

