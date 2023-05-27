import pandas as pd
import numpy as np
import sklearn 

df=pd.read_csv("C:/Users/robin/Downloads/corona (2).csv") 

f=df['corona_result']=='negative' 

neg=df[f] 
neg.sample(frac=1) 
neg=neg.iloc[:10000,:] 


f=df['corona_result']=='positive'

pos=df[f]
pos.sample(frac=1)
pos=pos.iloc[:10000,:]

final=pd.concat([pos,neg],axis=0).reset_index(drop=True) 

# V = final["corona_result"].value_counts() 
# print(V)


final.to_csv("covid2.csv")

for x in final.columns:
    f=final[x]!='None'
    final=final.loc[f,:]


final['test_date']=pd.to_datetime(final['test_date'])
final['month']=final['test_date'].dt.month
final['day']=final['test_date'].dt.day


final=final.drop(["test_date"],axis=1)
x=final.iloc[:, 0:]
x=x.drop(columns=["corona_result"])
y=final["corona_result"]


x['cough']=x['cough'].astype('int32')
x['fever']=x['fever'].astype('int32')
x['sore_throat']=x['sore_throat'].astype('int32')
x['shortness_of_breath']=x['shortness_of_breath'].astype('int32')
x['head_ache']=x['head_ache'].astype('int32')


from sklearn.preprocessing import LabelEncoder
la=LabelEncoder()
y=la.fit_transform(y)

lo=LabelEncoder()
x["gender"]=lo.fit_transform(x["gender"])

le=LabelEncoder()
x["test_indication"]=le.fit_transform(x["test_indication"])

li=LabelEncoder()
x["age_60_and_above"]=li.fit_transform(x["age_60_and_above"])

from matplotlib import pyplot as plt

plt.plot(y,x["fever"],marker="o",color="gold")
plt.xlabel("Coronavirus Result")
plt.ylabel("fever")
plt.title("Coronavirus result VS fever")
plt.show()

plt.plot(y,x["cough"],marker="o",color="blue")
plt.xlabel("Coronavirus Result")
plt.ylabel("Cough")
plt.title("Coronavirus result VS Cough")
plt.show()

plt.plot(y,x["sore_throat"],marker="o",color="red")
plt.xlabel("Coronavirus Result")
plt.ylabel("Sore Throat")
plt.title("Coronavirus result VS sore throat")
plt.show()

plt.plot(y,x["shortness_of_breath"],marker="o",color="yellow")
plt.xlabel("Coronavirus Result")
plt.ylabel("Shortness Of Breath")
plt.title("Coronavirus result VS Shortness of Breath")
plt.show()

plt.plot(y,x["head_ache"],marker="o",color="pink")
plt.xlabel("Coronavirus Result")
plt.ylabel("Head Ache")
plt.title("Coronavirus result VS Head Ache")
plt.show()

plt.plot(y,x["age_60_and_above"],marker="o",color="green")
plt.xlabel("Coronavirus Result")
plt.ylabel("Age > 60")
plt.title("Coronavirus result VS Age > 60")
plt.show()

plt.plot(y,x["gender"],marker="o",color="orange")
plt.xlabel("Coronavirus Result")
plt.ylabel("Gender")
plt.title("Coronavirus result VS Gender")
plt.show()

plt.plot(y,x["test_indication"],marker="o",color="purple")
plt.xlabel("Coronavirus Result")
plt.ylabel("Test Indication")
plt.title("Coronavirus result VS Test Indication")
plt.show()

plt.plot(y,x["month"],marker="o",color="grey")
plt.xlabel("Coronavirus Result")
plt.ylabel("Month")
plt.title("Coronavirus result VS Month")
plt.show()

plt.plot(y,x["day"],marker="o",color="skyblue")
plt.xlabel("Coronavirus Result")
plt.ylabel("Day")
plt.title("Coronavirus result VS Day")
plt.show()

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
x=sc.fit_transform(x)
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)

from sklearn.ensemble import RandomForestClassifier
Classifier=RandomForestClassifier(random_state=0)
Classifier.fit(x_train,y_train)
y_pred=Classifier.predict(x_test)

from sklearn.metrics import accuracy_score
print("Accuracy: ",end="")
print(accuracy_score(y_test,y_pred))


from joblib import dump,load

dump(lo,"gender.joblib")
dump(le,"test_indication.joblib")
dump(li,"age_60_and_above.joblib")
# dump(ly,"cough.joblib")
# dump(si,"simpleimputer.joblib")
dump(sc,"scaling.joblib")
dump(Classifier,"Classifier.joblib")

new = load("gender.joblib")
new = load("test_indication.joblib")
new = load("age_60_and_above.joblib")
# new = load("cough.joblib")
# new = load("simpleimputer.joblib")
new = load("scaling.joblib")
new = load("classifier.joblib")

# new=pd.DataFrame({"cough":[(input("Do you have cough (YES = 1, NO = 0): "))],"fever":[(input("Do you have fever (YES = 1, NO = 0): "))],"sore_throat":[(input("Do you have sore throat (YES = 1, NO = 0): "))],"shortness_of_breathe":[(input("Do you have shortness of breathe (YES = 1, NO = 0): "))],"headache":[(input("Do you have headache (YES = 1, NO = 0): "))],"age_60_and_above":(input("Is your age 60 or above (YES = 1, NO = 0): ")),"gender":(input("Enter male/female: ")),"test_indication":(input("Enter what your test indicates (Other/ Abroad/ Contact with confirmed): ")),"month":[(input("Enter your month of vaccination (in number): "))],"day":[(input("enter your day of vaccination: "))]})

