import pandas as pd
from sklearn.model_selection import train_test_split

def process_florida_voter_dataset(df, 
    cat_race_map = {1: "aian", 2: "api", 3: "nh_black", 4: "hispanic", 5: "nh_white", 6: "other", 7: "multi_racial", 9: "unknown"}
    include_race=['aian', 'api', 'nh_black', 'hispanic', 'nh_white']):
    
    df['race'] = df['race_cat'].map(cat_race_map)
    df = df[df['race'].isin(include_race)]

    # 0 = Asian, 1 = Black, 2=Hispanic, 3=White
    label_race_map = dict((enumerate(df["race"].value_counts().index)))
    race_label_map = {v: k for k, v in label_race_map.items()}
    
    df["label"] = df.loc[:, "race"].map(race_label_map)
    # df['label'].value_counts()

    df = df[["first_name", "last_name", "race", "label"]]

    df["first_last"] = df["first_name"].str.lower() + "_" + df["last_name"].str.lower()

    df = df[df["first_last"].notnull()]

    df_train, df_holdout = train_test_split(df, train_size=0.9, test_size=0.1)
    
    # return df_train, df_holdout
    df_train.to_parquet(f"data/florida_{len(include_race)}label_train.parquet")
    df_holdout.to_pickle(f"data/florida_{len(include_race)}label_test.parquet")
    
if __name__ == "__main__":
    import sys
    
    data_file = sys.argv[1]
    
    df = pd.read_csv(data_file)
    df = df.drop(columns=['Unnamed: 0', 'zip5', 'sex', 'age'])
    df.columns = ['first_name', 'last_name', 'race_cat']
    
    process_florida_voter_dataset(df)
    
    