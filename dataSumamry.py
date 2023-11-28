#Import the required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# Importing data from using the API endpoint
import pandas as pd
from sodapy import Socrata
def data_summary(file_path):
    print("Data Summary Starts here ...")
    print("""Data set is taken from NYC Open Data.

            Data set contains 106 million records and 19 columns.
            
            \nPlate : Vehicle plate number
            \nState : State where violation took place
            \nLicense Type : type of license
            \nSummons Number : Violation number to identify each violation
            \nIssue Date : Date on which violation took place
            \nViolation Time : time at which violation took place
            \nViolation : Type of violation
            \nJudgment Entry Date : Date of hearing by judge
            \nFine Amount : Fine that need to be paid
            \nPenalty Amount : Penality
            \nInterest Amount : interest on levied amount
            \nReduction Amount : reductions in any amount
            \nPayment Amount : Total amount to be paid
            \nAmount Due : Due amount
            \nPrecinct : District code
            \nCounty : County name
            \nIssuing Agency : Issuing authority or agency
            \nViolation Status : Status of the violation
            \nSummons Image : Images of the violation incident
            \nData set contains the 106 Million observation, here I am fetching the data using the API where we need to specify 
            the number of observations has to be retrieved.If we dont specify the number of observation to be retrieved by default 
            the API returns the 1000 observation randomly so we get different observation for each call of API .I tried to load the
            entire data but as the data is more than 100GB for which high configuration system is needed.Even Google Colab provides 
            RAM of around 12GB so here I am going to fetch the 1 million records by passing the parameter to the API which takes the 
            1 million observations as sample from the population randomly.""")
    print("Fetching the data from API..")
    # Unauthenticated client only works with public data sets. Note 'None'
    client = Socrata(file_path, None)
    # First 1 million results, returned as JSON from API / converted to Python list of
    # dictionaries by sodapy.
    results = client.get("nc67-uf89", limit=1000000)
    # Convert to pandas DataFrame
    results_df = pd.DataFrame.from_records(results)
    #results_df=pd.read_csv(file_path)
    print("Displaying the data:\n")
    print(results_df)
    print("checking the shape of the data")
    print(results_df.shape)
    print("Displaying data types of all attributes in the dataset")
    print(results_df.info())
    print(f"From the above data we can say that there were {results_df.shape[1]} attributes in the data set with different data types like float, integer and object(text)")
    return results_df
