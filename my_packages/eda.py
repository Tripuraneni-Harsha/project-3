import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
def exploratoryDataAnalysis(data):
    print("Exploratory data analysis starts here..")
    print("""To proceed with this section of the research, our initial steps involve conducting a summary statistics analysis for each of the variables, identifying any potential outliers or missing values that could influence our results. Following this, we will present graphical analyses for each attribute using both Matplotlib and Seaborn.""")
    print("Here I will drop some of the attributes that are not useful for my analysis")
    print("Dropping judgement_entry_date because I am not analysing on this data,also summons image also doesn't helps me in analysing it")
    data=data.drop(['judgment_entry_date','reduction_amount','precinct','violation_status','summons_image'],axis=1)
    print("Displaying the information after dropping the columns")
    print(data)
    print("""As we've successfully imported the data and removed the unwanted attributes from the data set, next 
    step is to carefully inspect the dataset for any missing values. Identifying and handling null values is crucial,
     as they can potentially affect the integrity and reliability of our research findings.""")
    print("checking the count of null values in each attribute")
    print(data.isnull().sum())
    print("According the above information, dataset contains missing.")
    print('''Here I am getting the day, month and year parts from the date attribute and assign the names to the days and months"
          using the calendar module splitted the column using split method delimited by "/" ''')
    data=pd.concat([data,data['issue_date'].str.split("/",expand=True)],axis=1)
    print("Renaming the columns")
    data=data.rename(columns={0:"Month",1:"Day",2:"Year"})
    print("Displaying the data")
    print("With the help of regular expression I am extracting the hour and AM/PM from the 'time' column")
    data['hour'] = data['violation_time'].str.extract(r'(\d{2}):\d{2}')
    data['AM/PM'] = data['violation_time'].str.extract(r'([AP])')
    print("Dropping the date and time columns as I dont need any more")
    data.drop(["issue_date","violation_time"],axis=1,inplace=True)
    print("Converting the data types of the numerical columns into float")
    data[['payment_amount','fine_amount','penalty_amount','interest_amount','amount_due']]=data[['payment_amount','fine_amount','penalty_amount','interest_amount','amount_due']].astype(float)
    print("lets see the statistical summary for the data")
    print(data.describe())
    print("Using describe method One can understand the data distribution like mean of that attribute and how much data falls below 25% of data similarly for 50% and 75% and also can see the standard deviation of the attributes.")
    print(data['fine_amount'].describe())
    print("The average amount paid for Open parking violation is 65.64 which is around 66$.")
    print("And the maximum amount can go as a fine will be around 515 USD so the range of the fine amount for violation lies between 11 to 515 $ mostly.")
    print("we will move forward with our exploratory analysis, addressing each attribute individually.")
    print("Map numeric month to month name using lambda function")
    month_name_mapping = {'01': 'January', '02': 'February', '03': 'March', '04': 'April', '05': 'May', '06': 'June',
                          '07': 'July', '08': 'August', '09': 'September', '10': 'October', '11': 'November', '12': 'December'}
    print("Converting the data type into integer")
    data['Day']=data['Day'].astype(int)
    data['Month']=data['Month'].astype(str)
    data['month_name'] = data['Month'].apply(lambda x: month_name_mapping.get(x))
    print("Map numeric day to day name using list comprehension")
    day_name_mapping = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}
    data['day_name'] = [day_name_mapping[x % 7] for x in data['Day']]
    print("""======================================================
                 No of Parking Violations by Month
             ======================================================""")
    graphPlotFun(data,"month_name","Number of Parking Violations by Month")
    print("""Findings:
            It shows that November and December months witnessed the large number of parking violations, might be due to the snow as it is a winter season.""")
    print("""======================================================
                 No of parking violations by Day
             ======================================================""")
    graphPlotFun(data,"day_name","Number of Parking Violations by Day")
    print("""Findings:
    It shows that Wednesday witnesses the large number of parking violations followed by Tuesday and Monday being the least.""")
    print("""======================================================
                 Parking violations by Time of the day
             ======================================================""")
    print("As the time is in 12hour format and the column has AM and PM timing we merge both columns")
    data["Time"]=data["hour"]+" "+data["AM/PM"]
    graphPlotFun(data,"Time","Number of Parking Violations by hour")
    print("""Findings:
    It shows that 1pm is the hour of the day which experiences more number of crashes in the day followed by 11am.

    9 AM to 2 PM witnessing the more number of parking violations in the day""")
    print("""======================================================
                 Parking Violations by Violation type
             ======================================================""")
    graphPlotFun(data,"violation","Number of Parking Violations by violation type")
    print("""Findings:
    \nThe three major reasons of the parking violations are as below:

    \n1. School Zone speed violation
    \n2. No Parking Street Cleaning
    \n3. Failed to display mini meter receipt""")
    print("""======================================================
                 Violations by State
             ======================================================""")
    graphPlotFun(data,"state","Number of Parking Violations by state")
    print("""Findings:
    Interestingly Newyork and New Jersey are the only states with highest number of parking violations occurred as per the dataset Newyork being the first followed by the New Jersey""")
    print("""======================================================
                 Parking violations by issuing agency
             ======================================================""")
    graphPlotFun(data,"issuing_agency","Number of Parking Violations by Issuing agency")
    print("""Findings:
    It shows that the majority of the violations as been charged by the transportation department followed by the Traffic department.""")
    print("""======================================================
                 Parking violations by license type
             ======================================================""")
    graphPlotFun(data,"license_type","Number of Parking Violations by License Type")
    print("""Findings:
    PAS license type is experiencing the majority of the violations and its very huge compared to others types of license.
    
    Note : "PAS" typically stands for "Passenger." It indicates that the driver's license type associated with the violation is for a passenger vehicle. This category often includes standard personal vehicles used for transportation, as opposed to commercial or special-use vehicles.
    
    "COM" indicates the commercial license type""")
    print("""======================================================
                 Parking Violations by County
             ======================================================""")
    graphPlotFun(data,"county","Number of Parking Violations by County")
    print("""Findings:
    Newyork County has highest number of the parking violations followed by county "Queens".""")
    print("""======================================================
                 Comparing the day across the months
             ======================================================""")
    print("Comparing the no of violations on Monday across the months")
    mondays_df = data[data['day_name'] == 'Monday']
    plt.figure(figsize=(15, 6))
    # Plot the value counts of Mondays in each month
    sns.countplot(x='month_name', data=mondays_df, order=mondays_df['month_name'].value_counts().index)
    plt.title('No of violations on  Mondays in Each Month')
    plt.show()
    print("""From the above plot we can say that the no of violations are not same throughout the year on monday, In january we have more number of violations on Monday followed by the August and December.""")
    print("Comparing the no of violations on Tuesday across the months")
    tuesday_df = data[data['day_name'] == 'Tuesday']
    plt.figure(figsize=(15, 6))
    # Plot the value counts of Tuesday in each month
    sns.countplot(x='month_name', data=tuesday_df, order=tuesday_df['month_name'].value_counts().index)
    plt.title('No of violations on Tuesday in Each Month')
    plt.show()
    print("On tuesday we have more violations in the month of December followed by the October")
    print("Comparing the no of violations on Wednesday across the months")
    wednesday_df = data[data['day_name'] == 'Wednesday']
    plt.figure(figsize=(15, 6))
    print("Plot the value counts of Wednesday in each month")
    sns.countplot(x='month_name', data=wednesday_df, order=wednesday_df['month_name'].value_counts().index)
    plt.title('No of violations on Wednesday in Each Month')
    plt.show()
    print("On Wednesday, we have more number of violations in the month of November followed by the March.")
    print("Comparing the no of violations on Thursday across the months")
    thursday_df = data[data['day_name'] == 'Thursday']
    plt.figure(figsize=(15, 6))
    # Plot the value counts of Thursday in each month
    sns.countplot(x='month_name', data=thursday_df, order=thursday_df['month_name'].value_counts().index)
    plt.title('No of violations on Thursday in Each Month')
    plt.show()
    print("On Thursday, we have more number of violations in the month of March followed by the December.")
    print("Comparing the no of violations on Friday across the months")
    friday_df = data[data['day_name'] == 'Friday']
    plt.figure(figsize=(15, 6))
    # Plot the value counts of Friday in each month
    sns.countplot(x='month_name', data=friday_df, order=friday_df['month_name'].value_counts().index)
    plt.title('No of violations on Friday in Each Month')
    plt.show()
    print("On Friday, we have more number of violations in the month of November followed by the December.")
    print("Comparing the no of violations on Saturday across the months")
    saturday_df = data[data['day_name'] == 'Saturday']
    plt.figure(figsize=(15, 6))
    # Plot the value counts of Saturday in each month
    sns.countplot(x='month_name', data=saturday_df, order=saturday_df['month_name'].value_counts().index)
    plt.title('No of violations on Saturday in Each Month')
    plt.show()
    print("On Saturday, we have more number of violations in the month of November followed by the March.")
    print("Comparing the no of violations on Sunday across the months")
    sunday_df = data[data['day_name'] == 'Wednesday']
    plt.figure(figsize=(15, 6))
    # Plot the value counts of Sunday in each month
    sns.countplot(x='month_name', data=sunday_df, order=sunday_df['month_name'].value_counts().index)
    plt.title('No of violations on Sunday in Each Month')
    plt.show()
    print("On Sunday, we have more number of violations in the month of November followed by the March and October with slightly varying in figures.")
    return data

def graphPlotFun(data, column_name, title):
        """This user defined function will plot the barcharts for the give input column and data set with the given title"""
        plt.figure(figsize=(25, 6))
        ax = data[column_name].value_counts().plot(kind="bar")
        ax.set_title(f'Matplotlib: {title}')
        plt.show()
        plt.figure(figsize=(25, 6))
        ax = sns.countplot(x=column_name, data=data)
        ax.set_title(f'Seaborn: {title}')
        plt.show()






