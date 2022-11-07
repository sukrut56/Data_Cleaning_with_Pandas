import pandas as pd
import numpy as np

#Importing data 
flights_data = pd.read_csv("C:/Kaggle Data/data/flights.csv")
flights_data.head(10)
weather_data_pd = pd.read_csv("C:/Kaggle Data/data/weather.csv")
weather_data_np = weather_data_pd.to_numpy()
#print(flights_data.columns)

#Question 1 How many flights were there from JFK to SLC? Int
direct = flights_data.groupby(['origin', 'dest']).size()				#using groupby to get the two columns and calculating the frequency of occurance 
q_1 = direct.loc[[('JFK','SLC')]]										#using loc method to get JFK to SLC column only 
#print(q_1)

#Question 2 How many airlines fly to SLC? Should be int
q_2 = (flights_data.groupby(flights_data['dest'] == 'SLC').apply(lambda x: pd.Series({'carrier': len(x['carrier'])})).reset_index())		#using groupby method to get carrier specific for SLC 
q_2 = q_2.iloc[1]				#using iloc to get only true values 
#print(q_2)

#Question 3 What is the average arrival delay for flights to RDU? float
q_3 = flights_data[flights_data.dest == 'RDU'].arr_delay				#Using slicing to select destination as RDU and select arrival delay column
mean = q_3.mean()														# caluculating mean of q_3
#print(mean)

#Question 4 What proportion of flights to SEA come from the two NYC airports (LGA and JFK)?  float
q_4 = flights_data[flights_data['dest'] == 'SEA'].origin				
df = pd.DataFrame(q_4)								#converting q_4 to dataframe 
total = df.count()									#counting the entries from dataframe 
JFK = (df['origin'].value_counts()['JFK'])			#count the values for flight origin from JFK to SEA 
#LGA = (df['origin'].value_counts()['LGA'])			#since there are no flights from LGA to SEA, we get error 
proportion = JFK / total							#calculating the proportion of flights from JFK 
#print(proportion)


#Question 5 Which date has the largest average depature delay? Pd slice  with date and float
#please make date a column. Preferred format is 2013/1/1 (y/m/d)
year = flights_data['year']
month = flights_data['month']
day = flights_data['day']
date = pd.concat([year,month,day], axis= 1)					#concatinating year, month and day into single column 
date_df = pd.to_datetime(date).dt.strftime('%Y/%m/%d')		#converting the format 
flights_data['Date'] = date_df		#adding column date into the flights_data dataframe 

mean = flights_data.groupby('Date')['dep_delay'].mean()		#calculating the mean of departure delay on each day 
#print(mean.max())											#printing the maximum of delay 

#Question 6 Which date has the largest average arrival delay? pd slice with date and float
q_6 = flights_data.groupby('Date')['arr_delay'].mean()		#calculating the mean of arrival delay on each day 
#print(q_6.max())

#Question 7 Which flight departing LGA or JFK in 2013 flew the fastest? pd slice with tailnumber and speed
#speed = distance/airtime
dept = flights_data[(flights_data['origin'] == 'LGA') | (flights_data['origin'] == 'JFK')].tailnum			#slicing flight origin from LGA or JFK based on flight tailnumber 
flights_data['Dept'] = dept																					#adding the above line to dataframe 

distance = flights_data['distance']
airtime = flights_data['air_time']
speed = distance/airtime						#calculating the speed based on distance and time 
flights_data['Speed'] = speed					#adding speed to dataframe 

q_7 = flights_data[['Dept', 'Speed']]			#selecting column Dept and Speed from the dataframe 
maximum = q_7.loc[q_7['Speed'].idxmax()]		#returns maximum value in the column 
#print(maximum)


#Question 8 Replace all nans in the weather pd dataframe with 0s. Pd with no nans
q_8 = weather_data_pd.fillna(0)					#filling nan values in dataframe with 0
#print(q_8)

#%% Numpy Data Filtering/Sorting Question Answering

#Use weather_data_np
#Question 9 How many observations were made in Feburary? Int
q_9= [weather_data_np[:, 3] == 2.0]				#selecting month column and selecting value 2 i.e February 
#print(np.count_nonzero(q_9))					#counting the number of times value has occured to get the number of observations made in February 


#Question 10 What was the mean for humidity in February? Float
q_10 = np.split(weather_data_np[:,8], np.unique(weather_data_np[:, 3], return_index=True)[1][1:])		#selecting column month and humidity to get values based on months 
selection = q_10[1]					#selecting february column 
#print(np.mean(selection))			#calculating mean of the february column 

#Question 11 What was the std for humidity in February? Float
q_11 = np.split(weather_data_np[:,8], np.unique(weather_data_np[:, 3], return_index=True)[1][1:])		#selecting month and humidity to get values based on month 
select = q_11[1]				
#print(np.std(select))				#calculating standard deviation for month february 