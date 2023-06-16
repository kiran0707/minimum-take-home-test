import pandas as pd
import emission as em
import activity_data as ad

# e_fact = em.Emission('CSV-Emission-Factors-and-Activity-Data-Emission-Factors.csv')
# act1 = ad.Activity_data('CSV-Emission-Factors-and-Activity-Data-Purchased-Goods-Services.csv')

def calculate_df(em_file, act_file, lookup_field):
    e_fact = em.Emission(em_file)
    act1 = ad.Activity_data(act_file)

    act1.rename_col_lookup('Supplier category', 'Lookup identifiers')

    act1_df = act1.df
    e_fact_df = e_fact.df

    result = pd.merge(act1_df, e_fact_df,how="inner", on=["Activity","Lookup identifiers"])
    result['co2e value'] = result.apply(lambda x: x['CO2e'] * x[lookup_field], axis=1)
    return result

def calculate_sort(em_file, act_file, lookup_field, sort_field):
    result_df = calculate_df(em_file, act_file, lookup_field)
    result = result_df.sort_values(by=[sort_field], ascending=False)
    return result

def calculate_group(em_file, act_file, lookup_field, group_field):
    result_df = calculate_df(em_file, act_file, lookup_field)
    
    result = result_df.groupby(by=[group_field]).agg({'co2e value': ['sum','count']})
    return result

def calculate_filter(em_file, act_file, lookup_field, filter_field, filter_value):
    result_df = calculate_df(em_file, act_file, lookup_field)
    return result_df.loc[result_df[filter_field] == filter_value ]    







