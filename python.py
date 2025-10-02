import pandas as pd
import matplotlib.pyplot as mp
datas=pd.read_csv("C:/Users/Admin/OneDrive/Desktop/narmathadevi/gender_submission.csv")
print(datas)
datas.rename(columns={"PassengerId":"Id","Survived":"Status for clarity"},inplace=True),
print("Renamed column name:",datas)
print("The Titanic data from the Top:",datas.head())
print("The Titanic data from the Bottom:",datas.tail())
print("Titanic dataset information:",datas.info())
print("Count:",datas.shape)
Non_survived=datas[datas["Status for clarity"]==0].head(10)
print("Top 10 Non-Survived:",Non_survived)
survived=datas[datas["Status for clarity"]==1].head(10)
print("Top 10 Survived:",survived)
Total_count=datas["Status for clarity"].value_counts()
survived_count=Total_count[1]
Nonsurvived_count=Total_count[0]
print("Total Survived:",survived_count)
print("Total Not Survived:",Nonsurvived_count)
Total_passengers=len(datas)
percentage_of_survived_passengers=(survived_count/Total_passengers)*100
percentage_of_Nonsurvived_passengers=(Nonsurvived_count/Total_passengers)*100
print("Percentage Survived:",percentage_of_survived_passengers)
print("Percentage Not Survived:",percentage_of_Nonsurvived_passengers)
Total_count.plot(kind='bar',color=["pink","skyblue"])
mp.xlabel("Status 0=Not survived,1=survived")
mp.ylabel("No of persons")
mp.title("Survived vs Not Survived")
mp.xticks(rotation=0)
mp.show()