Telco Churn Project Readme

Goal: The goals of the project is to figure out why customers are churning, and to create a model that will accurately predict whether or not a customer will churn. 

For this project we use the telco database from our sql server. 

Questions answered:

Could the month in which they signed up influence churn? i.e. if a cohort is identified by tenure, is there a cohort or cohorts who have a higher rate of churn than other cohorts? (Plot the rate of churn on a line chart where x is the tenure and y is the rate of churn (customers churned/total customers))
Are there features that indicate a higher propensity to churn? like type of internet service, type of phone service, online security and backup, senior citizens, paying more than x% of customers with the same services, etc.?
Is there a price threshold for specific services where the likelihood of churn increases once price for those services goes past that point? If so, what is that point for what service(s)?
If we looked at churn rate for month-to-month customers after the 12th month and that of 1-year contract customers after the 12th month, are those rates comparable?

Deliverables:

Jupyter notebook showing all work. Data exploration, model evaluation, etc.

Csv file with the customer_id, probability of churn, and the prediction of churn (1=churn, 0=not_churn).

Google slides presentation which explains how model was created and evaluates its accuracy

5 min presentation to team

.py files with functions used throughout project. This helps pathway for future data to be ran or model or for project to be recreated by someone else.

.py script instructions:

There are only two .py scripts used for this project.

split_scale.py is a file that includes two functions:
split_my_data function does a train, test split where train = .80 and sets a random state = 123
standard_scaler function takes in a dataframe and scales it using the standard scaler. It returns a dataframe with the scaled data.

acquire.py is a file with one function:
get_telco_data function reads in the database from sql. It returns all columns and joins all tables to ensure all data is brought in. This function does not require an input and will return a single dataframe that includes all data from the telco database.

prepare.py is a file with one function:
prep_telco_data function takes in the telco data and preps it for exploration. it does so by removing columns customer_id,contract_type, internet_service_type,and payment_type. These columns will not be useful in exploration. The function also converts the data type of the total_charges column from a string to a float. Lastly, this function encodes the following columns into 0's and 1's: gender, partner, dependents, phone_service,multiple_lines, online_security, online_backup,device_protection,tech_support,streaming_tv, streaming_movies, paperless_billing, and churn