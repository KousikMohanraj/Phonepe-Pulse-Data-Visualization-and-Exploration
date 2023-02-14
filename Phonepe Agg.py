import json
import pandas as pd
##############################################################################################################################################
# Phonepe AGG Transaction
# Load the JSON file into a Python object for the map data - 2022
with open(
        "C:/Users/mithu/OneDrive/Desktop/Python/Guvi Assignments/Phonepe_Pulse/data/aggregated/transaction/country/india/2022/1.json") as f:
    data_2022_Agg_Trans_1 = json.load(f)
with open(
        "C:/Users/mithu/OneDrive/Desktop/Python/Guvi Assignments/Phonepe_Pulse/data/aggregated/transaction/country/india/2022/2.json") as f:
    data_2022_Agg_Trans_2 = json.load(f)
with open(
        "C:/Users/mithu/OneDrive/Desktop/Python/Guvi Assignments/Phonepe_Pulse/data/aggregated/transaction/country/india/2022/3.json") as f:
    data_2022_Agg_Trans_3 = json.load(f)
with open(
        "C:/Users/mithu/OneDrive/Desktop/Python/Guvi Assignments/Phonepe_Pulse/data/aggregated/transaction/country/india/2022/4.json") as f:
    data_2022_Agg_Trans_4 = json.load(f)

# Load the JSON file into a Python object for the map data - 2021
with open(
        "C:/Users/mithu/OneDrive/Desktop/Python/Guvi Assignments/Phonepe_Pulse/data/aggregated/transaction/country/india/2021/1.json") as f:
    data_2021_Agg_Trans_1 = json.load(f)
with open(
        "C:/Users/mithu/OneDrive/Desktop/Python/Guvi Assignments/Phonepe_Pulse/data/aggregated/transaction/country/india/2021/2.json") as f:
    data_2021_Agg_Trans_2 = json.load(f)
with open(
        "C:/Users/mithu/OneDrive/Desktop/Python/Guvi Assignments/Phonepe_Pulse/data/aggregated/transaction/country/india/2021/3.json") as f:
    data_2021_Agg_Trans_3 = json.load(f)
with open(
        "C:/Users/mithu/OneDrive/Desktop/Python/Guvi Assignments/Phonepe_Pulse/data/aggregated/transaction/country/india/2021/4.json") as f:
    data_2021_Agg_Trans_4 = json.load(f)

# Load the JSON file into a Python object for the map data - 2020
with open(
        "C:/Users/mithu/OneDrive/Desktop/Python/Guvi Assignments/Phonepe_Pulse/data/aggregated/transaction/country/india/2020/1.json") as f:
    data_2020_Agg_Trans_1 = json.load(f)
with open(
        "C:/Users/mithu/OneDrive/Desktop/Python/Guvi Assignments/Phonepe_Pulse/data/aggregated/transaction/country/india/2020/2.json") as f:
    data_2020_Agg_Trans_2 = json.load(f)
with open(
        "C:/Users/mithu/OneDrive/Desktop/Python/Guvi Assignments/Phonepe_Pulse/data/aggregated/transaction/country/india/2020/3.json") as f:
    data_2020_Agg_Trans_3 = json.load(f)
with open(
        "C:/Users/mithu/OneDrive/Desktop/Python/Guvi Assignments/Phonepe_Pulse/data/aggregated/transaction/country/india/2020/4.json") as f:
    data_2020_Agg_Trans_4 = json.load(f)

# Load the JSON file into a Python object for the map data - 2019
with open(
        "C:/Users/mithu/OneDrive/Desktop/Python/Guvi Assignments/Phonepe_Pulse/data/aggregated/transaction/country/india/2019/1.json") as f:
    data_2019_Agg_Trans_1 = json.load(f)
with open(
        "C:/Users/mithu/OneDrive/Desktop/Python/Guvi Assignments/Phonepe_Pulse/data/aggregated/transaction/country/india/2019/2.json") as f:
    data_2019_Agg_Trans_2 = json.load(f)
with open(
        "C:/Users/mithu/OneDrive/Desktop/Python/Guvi Assignments/Phonepe_Pulse/data/aggregated/transaction/country/india/2019/3.json") as f:
    data_2019_Agg_Trans_3 = json.load(f)
with open(
        "C:/Users/mithu/OneDrive/Desktop/Python/Guvi Assignments/Phonepe_Pulse/data/aggregated/transaction/country/india/2019/4.json") as f:
    data_2019_Agg_Trans_4 = json.load(f)

# Load the JSON file into a Python object for the map data - 2018
with open(
        "C:/Users/mithu/OneDrive/Desktop/Python/Guvi Assignments/Phonepe_Pulse/data/aggregated/transaction/country/india/2018/1.json") as f:
    data_2018_Agg_Trans_1 = json.load(f)
with open(
        "C:/Users/mithu/OneDrive/Desktop/Python/Guvi Assignments/Phonepe_Pulse/data/aggregated/transaction/country/india/2018/2.json") as f:
    data_2018_Agg_Trans_2 = json.load(f)
with open(
        "C:/Users/mithu/OneDrive/Desktop/Python/Guvi Assignments/Phonepe_Pulse/data/aggregated/transaction/country/india/2018/3.json") as f:
    data_2018_Agg_Trans_3 = json.load(f)
with open(
        "C:/Users/mithu/OneDrive/Desktop/Python/Guvi Assignments/Phonepe_Pulse/data/aggregated/transaction/country/india/2018/4.json") as f:
    data_2018_Agg_Trans_4 = json.load(f)

df_2022_Agg_Trans_1 = pd.json_normalize(data_2022_Agg_Trans_1['data']['transactionData'], 'paymentInstruments',
                                        ['name'])
df_2022_Agg_Trans_2 = pd.json_normalize(data_2022_Agg_Trans_2['data']['transactionData'], 'paymentInstruments',
                                        ['name'])
df_2022_Agg_Trans_3 = pd.json_normalize(data_2022_Agg_Trans_3['data']['transactionData'], 'paymentInstruments',
                                        ['name'])
df_2022_Agg_Trans_4 = pd.json_normalize(data_2022_Agg_Trans_4['data']['transactionData'], 'paymentInstruments',
                                        ['name'])

df_2021_Agg_Trans_1 = pd.json_normalize(data_2022_Agg_Trans_1['data']['transactionData'], 'paymentInstruments',
                                        ['name'])
df_2021_Agg_Trans_2 = pd.json_normalize(data_2022_Agg_Trans_2['data']['transactionData'], 'paymentInstruments',
                                        ['name'])
df_2021_Agg_Trans_3 = pd.json_normalize(data_2022_Agg_Trans_3['data']['transactionData'], 'paymentInstruments',
                                        ['name'])
df_2021_Agg_Trans_4 = pd.json_normalize(data_2022_Agg_Trans_4['data']['transactionData'], 'paymentInstruments',
                                        ['name'])

df_2020_Agg_Trans_1 = pd.json_normalize(data_2022_Agg_Trans_1['data']['transactionData'], 'paymentInstruments',
                                        ['name'])
df_2020_Agg_Trans_2 = pd.json_normalize(data_2022_Agg_Trans_2['data']['transactionData'], 'paymentInstruments',
                                        ['name'])
df_2020_Agg_Trans_3 = pd.json_normalize(data_2022_Agg_Trans_3['data']['transactionData'], 'paymentInstruments',
                                        ['name'])
df_2020_Agg_Trans_4 = pd.json_normalize(data_2022_Agg_Trans_4['data']['transactionData'], 'paymentInstruments',
                                        ['name'])

df_2019_Agg_Trans_1 = pd.json_normalize(data_2022_Agg_Trans_1['data']['transactionData'], 'paymentInstruments',
                                        ['name'])
df_2019_Agg_Trans_2 = pd.json_normalize(data_2022_Agg_Trans_2['data']['transactionData'], 'paymentInstruments',
                                        ['name'])
df_2019_Agg_Trans_3 = pd.json_normalize(data_2022_Agg_Trans_3['data']['transactionData'], 'paymentInstruments',
                                        ['name'])
df_2019_Agg_Trans_4 = pd.json_normalize(data_2022_Agg_Trans_4['data']['transactionData'], 'paymentInstruments',
                                        ['name'])

df_2018_Agg_Trans_1 = pd.json_normalize(data_2022_Agg_Trans_1['data']['transactionData'], 'paymentInstruments',
                                        ['name'])
df_2018_Agg_Trans_2 = pd.json_normalize(data_2022_Agg_Trans_2['data']['transactionData'], 'paymentInstruments',
                                        ['name'])
df_2018_Agg_Trans_3 = pd.json_normalize(data_2022_Agg_Trans_3['data']['transactionData'], 'paymentInstruments',
                                        ['name'])
df_2018_Agg_Trans_4 = pd.json_normalize(data_2022_Agg_Trans_4['data']['transactionData'], 'paymentInstruments',
                                        ['name'])

#display(df_2022_Agg_Trans_1)
#display(df_2022_Agg_Trans_2)
#display(df_2022_Agg_Trans_3)
#display(df_2022_Agg_Trans_4)

#display(df_2018_Agg_Trans_1)
#display(df_2018_Agg_Trans_2)
#display(df_2018_Agg_Trans_3)
#display(df_2018_Agg_Trans_4)
# to Merge the data frame
df_Agg_Trans_2022 = pd.concat([df_2022_Agg_Trans_1, df_2022_Agg_Trans_2, df_2022_Agg_Trans_3, df_2022_Agg_Trans_4], axis=0)
df_Agg_Trans_2021 = pd.concat([df_2021_Agg_Trans_1, df_2021_Agg_Trans_2, df_2021_Agg_Trans_3, df_2021_Agg_Trans_4], axis=0)
df_Agg_Trans_2020 = pd.concat([df_2020_Agg_Trans_1, df_2020_Agg_Trans_2, df_2020_Agg_Trans_3, df_2020_Agg_Trans_4], axis=0)
df_Agg_Trans_2019 = pd.concat([df_2019_Agg_Trans_1, df_2019_Agg_Trans_2, df_2019_Agg_Trans_3, df_2019_Agg_Trans_4], axis=0)
df_Agg_Trans_2018 = pd.concat([df_2018_Agg_Trans_1, df_2018_Agg_Trans_2, df_2018_Agg_Trans_3, df_2018_Agg_Trans_4], axis=0)

df_Agg_Trans = pd.concat([df_Agg_Trans_2022,df_Agg_Trans_2021,df_Agg_Trans_2020,df_Agg_Trans_2019,df_Agg_Trans_2018], axis=0)

#df_Agg_Trans.to_excel("df_Agg_Transaction.xlsx")

display(df_Agg_Trans)

################################################################################################################################################

# Load the JSON file into a Python object for the aggregated\user data - 2022
# Json file is empty for 2022 2nd,3rd and 4th quarter
with open("C:/Users/mithu/OneDrive/Desktop/Python/Guvi Assignments/Phonepe_Pulse/data/aggregated/user/country/india/2022/1.json") as f:
    data_Agg_User_2022_1 = json.load(f)
with open("C:/Users/mithu/OneDrive/Desktop/Python/Guvi Assignments/Phonepe_Pulse/data/aggregated/user/country/india/2022/2.json") as f:
    data_Agg_User_2022_2 = json.load(f)
with open("C:/Users/mithu/OneDrive/Desktop/Python/Guvi Assignments/Phonepe_Pulse/data/aggregated/user/country/india/2022/3.json") as f:
    data_Agg_User_2022_3 = json.load(f)
with open("C:/Users/mithu/OneDrive/Desktop/Python/Guvi Assignments/Phonepe_Pulse/data/aggregated/user/country/india/2022/4.json") as f:
    data_Agg_User_2022_4 = json.load(f)

# Load the JSON file into a Python object for the aggregated\user data - 2021
with open("C:/Users/mithu/OneDrive/Desktop/Python/Guvi Assignments/Phonepe_Pulse/data/aggregated/user/country/india/2021/1.json") as f:
    data_Agg_User_2021_1 = json.load(f)
with open("C:/Users/mithu/OneDrive/Desktop/Python/Guvi Assignments/Phonepe_Pulse/data/aggregated/user/country/india/2021/2.json") as f:
    data_Agg_User_2021_2 = json.load(f)
with open("C:/Users/mithu/OneDrive/Desktop/Python/Guvi Assignments/Phonepe_Pulse/data/aggregated/user/country/india/2021/3.json") as f:
    data_Agg_User_2021_3 = json.load(f)
with open("C:/Users/mithu/OneDrive/Desktop/Python/Guvi Assignments/Phonepe_Pulse/data/aggregated/user/country/india/2021/4.json") as f:
    data_Agg_User_2021_4 = json.load(f)

# Load the JSON file into a Python object for the aggregated\user data - 2020
with open("C:/Users/mithu/OneDrive/Desktop/Python/Guvi Assignments/Phonepe_Pulse/data/aggregated/user/country/india/2020/1.json") as f:
    data_Agg_User_2020_1 = json.load(f)
with open("C:/Users/mithu/OneDrive/Desktop/Python/Guvi Assignments/Phonepe_Pulse/data/aggregated/user/country/india/2020/2.json") as f:
    data_Agg_User_2020_2 = json.load(f)
with open("C:/Users/mithu/OneDrive/Desktop/Python/Guvi Assignments/Phonepe_Pulse/data/aggregated/user/country/india/2020/3.json") as f:
    data_Agg_User_2020_3 = json.load(f)
with open("C:/Users/mithu/OneDrive/Desktop/Python/Guvi Assignments/Phonepe_Pulse/data/aggregated/user/country/india/2020/4.json") as f:
    data_Agg_User_2020_4 = json.load(f)

# Load the JSON file into a Python object for the aggregated\user data - 2019
with open("C:/Users/mithu/OneDrive/Desktop/Python/Guvi Assignments/Phonepe_Pulse/data/aggregated/user/country/india/2019/1.json") as f:
    data_Agg_User_2019_1 = json.load(f)
with open("C:/Users/mithu/OneDrive/Desktop/Python/Guvi Assignments/Phonepe_Pulse/data/aggregated/user/country/india/2019/2.json") as f:
    data_Agg_User_2019_2 = json.load(f)
with open("C:/Users/mithu/OneDrive/Desktop/Python/Guvi Assignments/Phonepe_Pulse/data/aggregated/user/country/india/2019/3.json") as f:
    data_Agg_User_2019_3 = json.load(f)
with open("C:/Users/mithu/OneDrive/Desktop/Python/Guvi Assignments/Phonepe_Pulse/data/aggregated/user/country/india/2019/4.json") as f:
    data_Agg_User_2019_4 = json.load(f)

# Load the JSON file into a Python object for the aggregated\user data - 2018
with open("C:/Users/mithu/OneDrive/Desktop/Python/Guvi Assignments/Phonepe_Pulse/data/aggregated/user/country/india/2018/1.json") as f:
    data_Agg_User_2018_1 = json.load(f)
with open("C:/Users/mithu/OneDrive/Desktop/Python/Guvi Assignments/Phonepe_Pulse/data/aggregated/user/country/india/2018/2.json") as f:
    data_Agg_User_2018_2 = json.load(f)
with open("C:/Users/mithu/OneDrive/Desktop/Python/Guvi Assignments/Phonepe_Pulse/data/aggregated/user/country/india/2018/3.json") as f:
    data_Agg_User_2018_3 = json.load(f)
with open("C:/Users/mithu/OneDrive/Desktop/Python/Guvi Assignments/Phonepe_Pulse/data/aggregated/user/country/india/2018/4.json") as f:
    data_Agg_User_2018_4 = json.load(f)

# Data Frames for 2022
df_Agg_User_2022_1 = pd.DataFrame(data_Agg_User_2022_1["data"]["usersByDevice"])
df_Agg_User_2022_2 = pd.DataFrame(data_Agg_User_2022_2["data"]["usersByDevice"])
df_Agg_User_2022_3 = pd.DataFrame(data_Agg_User_2022_3["data"]["usersByDevice"])
df_Agg_User_2022_4 = pd.DataFrame(data_Agg_User_2022_4["data"]["usersByDevice"])

# Data Frames for 2021
df_Agg_User_2021_1 = pd.DataFrame(data_Agg_User_2021_1["data"]["usersByDevice"])
df_Agg_User_2021_2 = pd.DataFrame(data_Agg_User_2021_2["data"]["usersByDevice"])
df_Agg_User_2021_3 = pd.DataFrame(data_Agg_User_2021_3["data"]["usersByDevice"])
df_Agg_User_2021_4 = pd.DataFrame(data_Agg_User_2021_4["data"]["usersByDevice"])

# Data Frames for 2020
df_Agg_User_2020_1 = pd.DataFrame(data_Agg_User_2020_1["data"]["usersByDevice"])
df_Agg_User_2020_2 = pd.DataFrame(data_Agg_User_2020_2["data"]["usersByDevice"])
df_Agg_User_2020_3 = pd.DataFrame(data_Agg_User_2020_3["data"]["usersByDevice"])
df_Agg_User_2020_4 = pd.DataFrame(data_Agg_User_2020_4["data"]["usersByDevice"])

# Data Frames for 2019
df_Agg_User_2019_1 = pd.DataFrame(data_Agg_User_2019_1["data"]["usersByDevice"])
df_Agg_User_2019_2 = pd.DataFrame(data_Agg_User_2019_2["data"]["usersByDevice"])
df_Agg_User_2019_3 = pd.DataFrame(data_Agg_User_2019_3["data"]["usersByDevice"])
df_Agg_User_2019_4 = pd.DataFrame(data_Agg_User_2019_4["data"]["usersByDevice"])

# Data Frames for 2018
df_Agg_User_2018_1 = pd.DataFrame(data_Agg_User_2018_1["data"]["usersByDevice"])
df_Agg_User_2018_2 = pd.DataFrame(data_Agg_User_2018_2["data"]["usersByDevice"])
df_Agg_User_2018_3 = pd.DataFrame(data_Agg_User_2018_3["data"]["usersByDevice"])
df_Agg_User_2018_4 = pd.DataFrame(data_Agg_User_2018_4["data"]["usersByDevice"])

# to merge the Dataframe in to one
df_Agg_User_2022 = pd.concat([df_Agg_User_2022_1, df_Agg_User_2022_2, df_Agg_User_2022_3, df_Agg_User_2022_4], axis=0)
df_Agg_User_2021 = pd.concat([df_Agg_User_2021_1, df_Agg_User_2021_2, df_Agg_User_2021_3, df_Agg_User_2021_4], axis=0)
df_Agg_User_2020 = pd.concat([df_Agg_User_2020_1, df_Agg_User_2020_2, df_Agg_User_2020_3, df_Agg_User_2020_4], axis=0)
df_Agg_User_2019 = pd.concat([df_Agg_User_2019_1, df_Agg_User_2019_2, df_Agg_User_2019_3, df_Agg_User_2019_4], axis=0)
df_Agg_User_2018 = pd.concat([df_Agg_User_2018_1, df_Agg_User_2018_2, df_Agg_User_2018_3, df_Agg_User_2018_4], axis=0)


df_Agg_User = pd.concat([df_Agg_User_2022,df_Agg_User_2021,df_Agg_User_2020,df_Agg_User_2019,df_Agg_User_2018], axis=0)

#df_Agg_User.to_excel("df_Agg_User.xlsx")

display(df_Agg_User)