import pandas as pd
if __name__ == "__main__":
    data = pd.read_csv('data/CRDC2013_14.csv',encoding="Latin-1")
    def value_counts(df):
        pivot_table1 = pd.pivot_table(data, values=["TOT_ENR_M", "TOT_ENR_F"], index="JJ", aggfunc="sum")
        print('pivot_table on JJ')
        print(pivot_table1)
        pivot_table2 = pd.pivot_table(data, values=["TOT_ENR_M", "TOT_ENR_F"], index="SCH_STATUS_MAGNET", aggfunc="sum")
        print('pivot_table on SCH_STATUS_MAGNET')
        print(pivot_table2)
        return 0
    value_counts(data)
    