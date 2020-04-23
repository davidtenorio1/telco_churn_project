import pandas as pd
import numpy as np
import env
from env import user, password, host
import warnings
warnings.filterwarnings("ignore")
from sklearn.preprocessing import LabelEncoder


def prep_telco_data(data):
    encoder = LabelEncoder()
    data = data.drop(columns=['customer_id','contract_type', 'internet_service_type','payment_type'])
    data['total_charges'] = pd.to_numeric(data['total_charges'],errors='coerce')
    encode_list = ['gender','partner', 'dependents', 'phone_service','multiple_lines', 'online_security', 'online_backup','device_protection','tech_support','streaming_tv', \
                  'streaming_movies', 'paperless_billing', 'churn']
    for c in encode_list:
        data[c] = encoder.fit_transform(data[c])
    return data






