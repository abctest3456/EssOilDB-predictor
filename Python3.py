#!/usr/bin/python

from collections import defaultdict


#paper_code#compund_name#CAS#quant#plant_part#technique#formula#classification#activity#plant_type#condition#IUPAC_name
f1 = "info_compound_final_upload_01082017.csv"


#paper_code#plant_name#geolocation#year#vol#title#plant_family#plant_type
f2 = "info_plant_final_upload_01082017.csv"

data1 = open(f1).read().splitlines()
data1 = list(set(data1))
data2 = open(f2).read().splitlines()
data2 = list(set(data2))

dic2 = defaultdict(list)

for i in data2:
    t = i.split("#")[1:]
    key = t[0]
    #print(key)
    dic2[key].append(i)

fh = open("out.csv","w")
print("paper_code#compund_name#CAS#quant#plant_part#technique#formula#classification#activity#plant_type#condition#IUPAC_name","#paper_code#plant_name#geolocation#year#vol#title#authors#journal#plant_family#plant_type",sep="#",file=fh)
for i in data1:
    t = i.split("#")[1:]
    key = t[0]
    i = "#".join(t)
    app = []

    if key in dic2:
        print(key)
        app = dic2[key]
        for n in app:
            print(i,n,sep="#",file=fh)
    else:print(i," ",sep="#",file=fh)
    
    


