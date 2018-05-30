import pandas as pd
if __name__ == "__main__":
    data = pd.read_csv('data/CRDC2013_14.csv',encoding="Latin-1")
    data['total_enrollment'] = data['TOT_ENR_M'] + data['TOT_ENR_F']
    all_enrollment = data['total_enrollment'].sum()
    r_g = ['SCH_ENR_HI_M','SCH_ENR_HI_F','SCH_ENR_AM_M','SCH_ENR_AM_F','SCH_ENR_AS_M','SCH_ENR_AS_F','SCH_ENR_HP_M','SCH_ENR_HP_F','SCH_ENR_BL_M','SCH_ENR_BL_F','SCH_ENR_WH_M','SCH_ENR_WH_F','SCH_ENR_TR_M','SCH_ENR_TR_F']
    def count_sum_col(df):
        a = df.sum()
        return a
    sum_r_g = data[r_g].apply(count_sum_col)
    propotion_r_g = sum_r_g/all_enrollment
    print(propotion_r_g)

    
        