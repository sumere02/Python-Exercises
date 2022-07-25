import pandas as pd

"""
dataset = pd.read_csv("USvideos.csv")
print(dataset)

newdataset = dataset.drop(["video_id","trending_date"],axis=1)
print(newdataset)

newdataset.to_csv("NewVideos.csv",index = False)
"""
"""
excelset = pd.read_excel("excelfile.xlsx")
print(excelset)
excelset["Column5"] = ["Recep","Emir","Sümer","Udemy"]
excelset.to_excel("newexcelfile.xlsx")
"""
dataset = pd.read_html("http://www.contextures.com/xlSampleData01.html",header = 0)
print(dataset)

