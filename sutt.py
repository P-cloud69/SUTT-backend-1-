import pandas as pd
import json

df = pd.read_excel('C:\\Users\\the47\\Downloads\\Mess Menu Sample.xlsx', header=None)

dates = df.iloc[1]
dates = pd.to_datetime(dates).dt.date 

messmenu = {}

indices_1 = [3,4,5,6,7,8,9,10,11]
indices_2 = [14,15,16,17,18,19,20,21]
indices_3 = [24,25,26,27,28,29,30]



for col in df.columns:
  
    date = str(dates[col])
    breakfast = df.loc[indices_1, col].astype(str).tolist()
    lunch = df.loc[indices_2, col].astype(str).tolist()
    dinner = df.loc[indices_3, col].astype(str).tolist()
    
    breakfast = [item if "**************" not in item else None for item in breakfast]
    lunch = [item if "**************" not in item else None for item in lunch]
    dinner = [item if "**************" not in item else None for item in dinner]
    breakfast = [item for item in breakfast if item not in [None, 'nan']]
    lunch = [item for item in lunch if item not in [None, 'nan']]
    dinner = [item for item in dinner if item not in [None, 'nan']]
    messmenu[date] = {
        "BREAKFAST": breakfast,
        "LUNCH": lunch,
        "DINNER": dinner
    }
df_mess_menu = pd.DataFrame.from_dict(messmenu, orient="index")

df_mess_menu.to_json('messmenutask.json', orient='index', indent=4)
jsonmenu = json.dumps(messmenu, indent=2)
print(jsonmenu)
