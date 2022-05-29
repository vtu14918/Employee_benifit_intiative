# importing the necessary libraries
from django.shortcuts import render
from .models import upload
from django.http import HttpResponse
import pandas as pd 
import json
def home(request):
      if request.method =="POST":
            file=request.FILES["myfile"]
            d=pd.read_csv(file)
            df=pd.DataFrame(d)
            json_records = df.reset_index().to_json(orient ='records')
            data = []
            data = json.loads(json_records)
            context = {'d': data}
            t=df["Target"]
            b=df["Actual"]
            df=df
            a1=list(t)
            a2=list(b)
            dev=[]
            for item1, item2 in zip(a1, a2):
                  item = item1 - item2
                  dev.append(item)
            Dailyproduction=list(df["Timestamp"]*a2)
            DT=[]
            WT=[]
            MT=[]
           

            for Id in range (len(df)):
                  if(Dailyproduction[Id]==a1[Id] or Dailyproduction[Id]>=90):
                        goodpoints=10
                        bonuspoints=10
                        Dailytotal=goodpoints+bonuspoints
                        Weeklytotal=Dailytotal*7
                        Montlytotal=Dailytotal*30
                        DT.append(Dailytotal)
                        WT.append(Weeklytotal)
                        MT.append(Montlytotal)
                  elif(Dailyproduction[Id]<90 or Dailyproduction[Id]>=80):
                        goodpoints=9
                        bonuspoints=5
                        Dailytotal=goodpoints+bonuspoints
                        Weeklytotal=Dailytotal*7
                        Montlytotal=Dailytotal*30
                        DT.append(Dailytotal)
                        WT.append(Weeklytotal)
                        MT.append(Montlytotal)
                        
                  else:
                        goodpoints=8
                        bonuspoints=0
                        Dailytotal=goodpoints+bonuspoints
                        Weeklytotal=Dailytotal*7
                        Montlytotal=Dailytotal*30
                        DT.append(Dailytotal)
                        WT.append(Weeklytotal)
                        MT.append(Montlytotal)
            return render(request,'validate.html',{"abc":False,"head":DT,"head1":WT,"head2":MT})
                  
      
      else:
            return render(request,'validate.html')
      
def upload(request):
      return render(request,'upload.html')



