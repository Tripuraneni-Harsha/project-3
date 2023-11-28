import dataSumamry as ds
import eda as ed
import inferences as inf
file_path="data.cityofnewyork.us"
print("Introduction")
print("""The Open Parking and Camera Violations dataset contains information related to parking and camera violations, 
including details such as state, license type, issue date, violation time, violation type, fine amount, penalty amount, 
payment amount, amount due, county, and issuing agency. This dataset provides an opportunity to gain insights into parking 
and camera violations, potentially helping to optimize traffic enforcement, improve compliance, and enhance the overall parking 
and traffic management system.""")
print("""Research Questions :
\n1. Are there any spatial patterns in violations, and how do the violation types vary across different counties?

\n2. Which states or regions have the highest number of parking and camera violations?

\n3. Are there significant differences in violation frequencies among different issuing agencies?

\n4. Is there any pattern in due amount and the payment amount acorss the counties?

\n5. Are there any noticeable trends in violation occurrences over time?

\n6. What are the most common types of parking and camera violations?

\n7. Do specific violation types tend to be associated with higher charges?

\n8. What is the average payment amount, and amount due for these violations?""")
data_sumamry=ds.data_summary("file_path")
data_eda=ed.exploratoryDataAnalysis(data_sumamry)
inf.inferences(data_eda)
print("Conclusion:")
print("""The Data Analysis of the "Open Parking and Camera Violations" dataset reveals that New York and New Jersey have the 
highest number of parking violations, with New York and the Bronx counties showing the most violations. Peak violation times 
occur between 7 AM to 8 AM and 1 PM to 11 PM, and July and August experience heightened violations, possibly due to seasonal factors.
 The Traffic Department and the Department of Transportation are the primary enforcers. These findings offer valuable insights 
 to government agencies, enabling more efficient resource allocation, informed policy adjustments, revenue generation, 
 increased public awareness, and improved traffic flow, ultimately contributing to more effective parking regulation and 
 transportation management.""")
print("References")
print("""
1. https://data.cityofnewyork.us/City-Government/Open-Parking-and-Camera-Violations/nc67-uf89

2. https://towardsdatascience.com/an-extensive-guide-to-exploratory-data-analysis-ddd99a03199e

3. https://medium.com/towardsdev/320-python-and-data-science-tips-covering-pandas-numpy-ml-basics-sklearn-jupyter-and-more-83e870b5f0e4

4. https://medium.com/@michael71314/python-lesson-29-more-things-you-can-do-with-matplotlib-bar-charts-matplotlib-pt-2-6db863ffb864

5. https://www.analyticsvidhya.com/blog/2021/07/eda-exploratory-data-analysis-using-python-pandas-and-sql/

6. https://dzone.com/articles/how-to-use-pandas-and-matplotlib-to-perform-explor""")


