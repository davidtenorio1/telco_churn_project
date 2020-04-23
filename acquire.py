import pandas as pd
import numpy as np
import env
from env import user, password, host
import warnings
warnings.filterwarnings("ignore")

def get_telco_data():
    url = f'mysql+pymysql://{user}:{password}@{host}/telco_churn'
    data = pd.read_sql('''select * from customers
join contract_types using (contract_type_id)
join internet_service_types using (internet_service_type_id)
join payment_types using (payment_type_id)
where total_charges not like " "
''',url)
    return data



