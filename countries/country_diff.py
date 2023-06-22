import pandas as pd

def normalize_online_data(filename : str) -> pd.DataFrame:
    df = pd.read_csv(filename)
    return df[['name']]

def normalize_my_list(filenam : str) -> pd.DataFrame:
    with open('mylist.txt', 'r') as f:
        country_list = f.read()

        # read a file and put each row into a pandas dataframe under a column named "name"
        df = pd.DataFrame(country_list.split('\n'), columns=['name'])
        return df

def get_difference(df1 : pd.DataFrame, df2 : pd.DataFrame) -> pd.DataFrame:
    # convert the dataframe to a set to remove duplicates
    df1_set = set(df1['name'])
    df2_set = set(df2['name'])

    # get the difference between the two sets
    diff = df1_set.difference(df2_set)

    # convert the set back to a dataframe
    return pd.DataFrame(list(diff), columns=['name'])

def main():
    df1 = normalize_online_data('countries_online.csv')
    df2 = normalize_my_list('mylist.txt')
    df3 = get_difference(df1, df2)

    #Output the difference to a file
    df3.to_csv('difference.txt', index=False)
    


if __name__ == "__main__":
    main()