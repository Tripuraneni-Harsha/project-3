import eda as ed
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
def inferences(data):
    print("Inferences Starts here..")
    print("With the Exploratory Data Analysis phase concluded, we will now proceed with the analysis necessary to address our research questions.")
    print(""">>>>>>>Inference 1: Are there any spatial patterns in violations, and how do the violation types vary across different counties?""")
    violations_by_state = data.groupby(['county', 'violation']).size().reset_index(name='count')
    # Find the top 5 violations in each state
    print(violations_by_state.groupby('county').apply(lambda x: x.nlargest(5, 'count')).reset_index(drop=True))
    print("""In the above code, we are fetching the top 5 violation types in each county.\n
    Observations : As per the above information, I Can observe an interesting pattern across the different
     counties that No Parking-Street cleaning is the major violation type that we can observe very often across the counties.""")
    print(""">>>>>>>Inference 2: Which states or regions have the highest number of parking and camera violations?""")
    print("State")
    print(data['state'].value_counts())
    ed.graphPlotFun(data,"state","Number of Parking Violations by State")
    print("County")
    data['county'].value_counts()
    ed.graphPlotFun(data,"county","Number of Parking Violations by County")
    print("Observations : So State New York stood at first with large number of parking violations followed by New Jersey. In terms of county Newyork stands at first followed by Queens.")
    print(">>>>>>>>Inference 3: Are there significant differences in violation frequencies among different issuing agencies?")
    print(data['issuing_agency'].value_counts())
    ed.graphPlotFun(data,"issuing_agency","Number of Parking Violations by Issuing Agency")
    print("Observations : Yes, most of the tickets were being issued bt the Traffic department and Department of Transportation with almost similiar figures.")
    print(">>>>>>>>>Inference 4: Is there any pattern in due amount and the payment amount across the counties?")
    violations_data = data
    # Group by county and calculate the total payment amount and total amount due for each county
    county_summary = violations_data.groupby('county').agg({'payment_amount': 'sum', 'amount_due': 'sum'}).reset_index()
    # Find the top 5 counties based on total payment amount
    top_counties = county_summary.nlargest(5, 'payment_amount')
    # Plot the data using matplotlib and seaborn
    plt.figure(figsize=(12, 8))
    # Bar plot for total payment amount
    plt.subplot(2, 1, 1)
    sns.barplot(x='county', y='payment_amount', data=top_counties, palette='viridis')
    plt.title('Total Payment Amount for Top 5 Counties')
    plt.xlabel('County')
    plt.ylabel('Total Payment Amount')
    # Bar plot for total amount due
    plt.subplot(2, 1, 2)
    sns.barplot(x='county', y='amount_due', data=top_counties, palette='viridis')
    plt.title('Total Amount Due for Top 5 Counties')
    plt.xlabel('County')
    plt.ylabel('Total Amount Due')
    plt.tight_layout()
    plt.show()
    print("Here we can see the top 5 counties with highest amount to be paid ,NY has is in the top and the due amount is also high in Newyork. And next in Bronx can see that there is less due amount.")
    print(">>>>>>>>>Inference 5: Are there any noticeable trends in violation occurrences over time?")
    print("As the time is in 12hour format and the column has AM and PM timing we merge both columns")
    data["Time"]=data["hour"]+" "+data["AM/PM"]
    print(data['Time'].value_counts())
    ed.graphPlotFun(data,"Time","Number of Parking Violations by hour")
    print("Observations : Especially time from 9 AM to 2 PM is experiencing the large number of parking violations")
    print(">>>>>>>Inference 6: What are the most common types of parking and camera violations?")
    print(data['violation'].value_counts())
    ed.graphPlotFun(data,"violation","Number of Parking Violations by Violation Type")
    print("""Observations : The three common types of violations are as below:
        \n1. PHTO SCHOOL ZN SPEED VIOLATION
        \n2. NO PARKING-STREET CLEANING
        \n3. FAILED TO DISPLAY MINI METER RECEIPT""")
    print(">>>>>>>>Inference 7: Do specific violation types tend to be associated with higher charges for violations?")
    result = data.groupby('violation').agg({'payment_amount': ['count', 'mean'], 'amount_due': 'mean'}).reset_index()
    print("Rename the columns for clarity")
    result.columns = ['Violation Type', 'Count of Violations', 'Average Payment Amount', 'Average Due Amount']
    print("Sort the result by the count of violations in descending order")
    print(result.sort_values(by='Count of Violations', ascending=False))
    print("""Observations : From the above it is clear that larger fine are not associated with common type of violations.
    Larger fines associated with the below type of violations:
    \n1. ALTERING INTERCITY BUS PERMIT
    \n2. ANGLE PARKING
    \n3. ANGLE PARKING-COMM VEHICLE
    \n4. Also their frequency is also less""")
    print(">>>>>>>>>Inference 6: What is the average payment amount, and amount due for these violations?")
    print(data.groupby('violation').agg({'payment_amount': ['count', 'mean']}).reset_index().sort_values(by=('payment_amount','mean'), ascending=False))
    print(">>>>>>>>Inference 8: What is the average payment amount, and amount due for these violations?")
    print(data.groupby('violation').agg({'payment_amount': ['count', 'mean']}).reset_index().sort_values(by=('payment_amount','mean'), ascending=False))

