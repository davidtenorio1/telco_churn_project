import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns
sns.set_style('whitegrid')
import env
from env import user, password, host
import warnings
warnings.filterwarnings("ignore")
from sklearn.preprocessing import LabelEncoder

def get_telco_data():
    url = f'mysql+pymysql://{user}:{password}@{host}/telco_churn'
    data = pd.read_sql('''select * from customers
join contract_types using (contract_type_id)
join internet_service_types using (internet_service_type_id)
join payment_types using (payment_type_id)
where total_charges not like " "
''',url)
    return data


def prep_telco_data(data):
    encoder = LabelEncoder()
    data = data.drop(columns=['customer_id','contract_type', 'internet_service_type','payment_type'])
    data['total_charges'] = pd.to_numeric(data['total_charges'],errors='coerce')
    encode_list = ['gender','partner', 'dependents', 'phone_service','multiple_lines', 'online_security', 'online_backup','device_protection','tech_support','streaming_tv', \
                  'streaming_movies', 'paperless_billing', 'churn']
    for c in encode_list:
        data[c] = encoder.fit_transform(data[c])
    return data

data=get_telco_data()
data.head(20)
data=prep_telco_data(data)








