import pandas as pd 
import random
def get_list():
    header_list = ["categories"]
    df = pd.read_csv (r'list.csv', names = header_list)
    print(df)
    print(df.size)
    no_blanks = df[df["categories"].str.startswith("LIS") == False]
    print(no_blanks)
    print(no_blanks.size)
    return get_categories(no_blanks)

def get_categories(df):
    rows = df.size
    list = []
    for i in range(12):
        index = random.randint(0,rows)
        list.append(df.iloc[index,0])
    print(list)
    return process_list(list)

def process_list(list):
    for index in range(len(list)):
        list[index] = str(index + 1) + ": " + str(list[index])[3::]
    print(list)
    return list