#!/usr/bin/env python
# coding: utf-8

# ### Note
# * Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# ## Player Count

# * Display the total number of players
# 

# In[47]:


# Dependencies and Setup
import pandas as pd
file_to_load = "Resources/purchase_data.csv"
# Read Purchasing File and store into Pandas data frame
purchase_df = pd.read_csv(file_to_load)
uniqueplayers=purchase_df.loc[:, ["SN","Gender","Age"]]
uniqueplayers=uniqueplayers.drop_duplicates()
TotalNumberOfPlayers=uniqueplayers.count()[0]
pd.DataFrame({"Total Players": [TotalNumberOfPlayers]})


# ## Purchasing Analysis (Total)

# * Run basic calculations to obtain number of unique items, average price, etc.
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame
# 

# In[48]:


#Price Mean
Pricemean =purchase_df["Price"].mean()
pd.DataFrame({"Average Price": [Pricemean]}).round(2).style.format('${0:}')
#Unique Items
uniqueitems=purchase_df.loc[:, ["Item Name"]]
uniqueitems=uniqueitems.drop_duplicates()
uniqueitems=uniqueitems.count()[0]
pd.DataFrame({"Number of Unique Items": [uniqueitems]})
#Number of Purchases
TotalPurchases=purchase_df.loc[:, ["Purchase ID"]]
TotalPurchases=TotalPurchases.count()[0]
pd.DataFrame({"Number of Purchases": [TotalPurchases]})
#Total Revenue
TotalRevenue=purchase_df.loc[:,"Price"].sum()
pd.DataFrame({"Total Revenue": [TotalRevenue]}).style.format('${0:,}')
#create summary df 
Summary_df=pd.DataFrame({"Number of Unique Items": [uniqueitems],
                   "Average Price": [Pricemean],
                   "Number of Purchases": [TotalPurchases],
                   "Total Revenue": [TotalRevenue]}).round(2)
# Style Average Price and Tootal Revnue
Summary_df[["Average Price","Total Revenue"]]=Summary_df[["Average Price","Total Revenue"]].applymap("${:,.2f}".format)
Summary_df


# ## Gender Demographics

# * Percentage and Count of Male Players
# 
# 
# * Percentage and Count of Female Players
# 
# 
# * Percentage and Count of Other / Non-Disclosed
# 
# 
# 

# In[49]:


# Calculate the Number and Percentage by Gender
gender_count =uniqueplayers["Gender"].value_counts()
gender_percentage =gender_count / TotalNumberOfPlayers *100
Gender_Demographics =pd.DataFrame({"Total Count": gender_count,
                                   "Percentage of Players": gender_percentage})
Gender_Demographics[["Percentage of Players"]]=Gender_Demographics[["Percentage of Players"]].applymap("{:,.2f}".format)+'%'
Gender_Demographics


# 
# ## Purchasing Analysis (Gender)

# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. by gender
# 
# 
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[50]:


groupedGender_df=purchase_df.groupby(["Gender"])
# Total purchase Value
Total_Purchase_Value =groupedGender_df.sum()["Price"]                                       
# Average Purchase Price
Average_Purchase_Price =groupedGender_df.mean()["Price"]
# Purchase Count
Purchase_Count =groupedGender_df.count()["Price"]
# Avg Total Purchase per Person
Avg_Total_Purchase_Per_Person=Total_Purchase_Value /Gender_Demographics["Total Count"]
#Summary
Summary_df_Analysis=pd.DataFrame({"Purchase Count": Purchase_Count,
                                  "Average Purchase Price": Average_Purchase_Price,
                                  "Total Purchase Value": Total_Purchase_Value,
                                  "Avg Total Purchase Per Person": Avg_Total_Purchase_Per_Person})

Summary_df_Analysis["Total Purchase Value"]=Summary_df_Analysis["Total Purchase Value"].map("${:,.2f}".format)
Summary_df_Analysis["Average Purchase Price"]=Summary_df_Analysis["Average Purchase Price"].map("${:,.2f}".format)
Summary_df_Analysis["Avg Total Purchase Per Person"]=Summary_df_Analysis["Avg Total Purchase Per Person"].map("${:,.2f}".format)
Summary_df_Analysis


# ## Age Demographics

# * Establish bins for ages
# 
# 
# * Categorize the existing players using the age bins. Hint: use pd.cut()
# 
# 
# * Calculate the numbers and percentages by age group
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: round the percentage column to two decimal points
# 
# 
# * Display Age Demographics Table
# 

# In[51]:


bins = [0,9.9, 14.9, 19.9, 24.9, 29.9, 34.9,39.9,50]
# Create the names for the bins
group_names = ["<10", "10-14","15-19","20-24","25-29","30-34","35-39","40+"]
uniqueplayers["AgeRange"]=pd.cut(uniqueplayers["Age"],bins,labels=group_names)
Age_count = uniqueplayers["AgeRange"].value_counts()
Percentage=Age_count /TotalNumberOfPlayers * 100
Age_demographics=pd.DataFrame({"Total Count": Age_count,
                               "Percentage of Players": Percentage
                                })
Age_demographics[["Percentage of Players"]]=Age_demographics[["Percentage of Players"]].applymap("{:,.2f}".format)+'%'
Age_demographics.sort_index()


# ## Purchasing Analysis (Age)

# * Bin the purchase_data data frame by age
# 
# 
# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[56]:


purchase_df["AgeRange"] = pd.cut(purchase_df["Age"], bins, labels=group_names)
grpbyAgedf=purchase_df.groupby(["AgeRange"])
Total_Purchase_Price_Age = grpbyAgedf.sum()["Price"]
Average_Purchase_Price_Age = grpbyAgedf.mean()["Price"]
Purchase_Count_Age = grpbyAgedf.count()["Price"]
Avg_Total_Purchase_Per_Person_Age = Total_Purchase_Price_Age / Age_demographics["Total Count"]
Summary_Puchasing_Analysis=pd.DataFrame({"Purchase Count": Purchase_Count_Age,
                                          "Average Purchase Price": Average_Purchase_Price_Age,
                                           "Total Purchase Price": Total_Purchase_Price_Age,
                                           "Avg Total Purchase Per Person": Avg_Total_Purchase_Per_Person_Age})

Summary_Puchasing_Analysis["Average Purchase Price"]=Summary_Puchasing_Analysis["Average Purchase Price"].map("${:,.2f}".format)
Summary_Puchasing_Analysis["Total Purchase Price"]=Summary_Puchasing_Analysis["Total Purchase Price"].map("${:,.2f}".format)
Summary_Puchasing_Analysis["Avg Total Purchase Per Person"]=Summary_Puchasing_Analysis["Avg Total Purchase Per Person"].map("${:,.2f}".format)
Summary_Puchasing_Analysis


# ## Top Spenders

# * Run basic calculations to obtain the results in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the total purchase value column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[53]:


grpbySNdf=purchase_df.groupby(["SN"])
Purchase_Count_SN =grpbySNdf.count()["Price"]
Average_Purchase_Price_SN =grpbySNdf.mean()["Price"]
Total_Purchase_Values_SN =grpbySNdf.sum()["Price"]

Summary_Top_Spenders=pd.DataFrame({"Purchase Count": Purchase_Count_SN,
                                   "Average Purchase Price": Average_Purchase_Price_SN,
                                   "Total Purchase Value": Total_Purchase_Values_SN})

Summary_Top_Spenders=Summary_Top_Spenders.sort_values("Total Purchase Value",ascending=False)
Summary_Top_Spenders["Average Purchase Price"]=Summary_Top_Spenders["Average Purchase Price"].map("${:,.2f}".format)
Summary_Top_Spenders["Total Purchase Value"]=Summary_Top_Spenders["Total Purchase Value"].map("${:,.2f}".format)
Summary_Top_Spenders.head()


# ## Most Popular Items

# * Retrieve the Item ID, Item Name, and Item Price columns
# 
# 
# * Group by Item ID and Item Name. Perform calculations to obtain purchase count, average item price, and total purchase value
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the purchase count column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[54]:


grpbyItemID=purchase_df.groupby(["Item ID","Item Name"])
Purchase_Countp =grpbyItemID.count()["Price"]
Item_Price=grpbyItemID.mean()["Price"]
Total_Purchase_Values =grpbyItemID.sum()["Price"] 

Summary_Popular_Items=pd.DataFrame({"Purchase Count": Purchase_Countp,
                                   "Item Price": Item_Price,
                                   "Total Purchase Value": Total_Purchase_Values})
Summary_Popular_Items=Summary_Popular_Items.sort_values("Purchase Count",ascending=False)
Summary_Popular_Items[["Item Price"]]=Summary_Popular_Items[["Item Price"]].applymap("${:,.2f}".format)
Summary_Popular_Items[["Total Purchase Value"]]=Summary_Popular_Items[["Total Purchase Value"]].applymap("${:,.2f}".format)
Summary_Popular_Items.head()


# ## Most Profitable Items

# * Sort the above table by total purchase value in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the data frame
# 
# 

# In[55]:


grpbyItemID=purchase_df.groupby(["Item ID","Item Name"])
Purchase_Countp =grpbyItemID.count()["Price"]
Item_Price=grpbyItemID.mean()["Price"]
Total_Purchase_Values =grpbyItemID.sum()["Price"] 

Summary_Popular_Items=pd.DataFrame({"Purchase Count": Purchase_Countp,
                                   "Item Price": Item_Price,
                                   "Total Purchase Value": Total_Purchase_Values})
Summary_Popular_Items=Summary_Popular_Items.sort_values("Total Purchase Value",ascending=False)
Summary_Popular_Items[["Item Price"]]=Summary_Popular_Items[["Item Price"]].applymap("${:,.2f}".format)
Summary_Popular_Items[["Total Purchase Value"]]=Summary_Popular_Items[["Total Purchase Value"]].applymap("${:,.2f}".format)
Summary_Popular_Items.head()


# In[ ]:




