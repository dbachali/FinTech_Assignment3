import pandas as pd

# Read in data, format and combine
companies = pd.read_excel("D:\Dan\Stevens\Fin Tech\Companies.xlsx")
data2 = pd.read_excel("D:\Dan\Stevens\Fin Tech\company name_wenbo.xlsx")
data2.columns = companies.columns
companies = companies.append(data2, ignore_index = True)
data3 = pd.read_excel("D:\Dan\Stevens\Fin Tech\company_data.xlsx")
data3.columns = companies.columns
companies = companies.append(data3, ignore_index = True)
