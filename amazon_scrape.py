import io

import streamlit as st
import pandas as pd
from pymongo import MongoClient

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000000000)

mongodb_client = 'mongodb://localhost:27017'
mongodb_server = 'localhost'
mongodb_port = 27017
username = 'admin'
pwd = '123456'

database = "amazon_scrape"
collection_name = "products"

df = pd.read_csv('dataset_free-amazon-product-scraper_2023-08-06_04-44-51-057.csv')
df = df[['brand', 'title', 'price/value', 'inStock', 'description', 'stars', 'seller/name', 'reviewsCount','reviewsLink','url', 'thumbnailImage']]
# print(df)
df.to_csv("sorted_products.csv")

# TO IMPORT :
# mongoimport --type csv -d amazon_scrape -c products --headerline --drop products.csv

# Connection to Mongodb :
# client = MongoClient(mongodb_server, mongodb_port)
# db = client.admin
# # db.command(username, pwd, roles=['readWrite'])
# connection_string = f"mongodb://{username}:{pwd}@localhost/{database}"
# client = MongoClient(connection_string)
# db = client[database]

connection_string = "mongodb://localhost:27017/"
client = MongoClient(connection_string)
db = client[database]
collection = db[collection_name]

datas = collection.find()
df = pd.DataFrame(datas)

st.title("Amazon Products Scrapped")

#filtering
filtered_df = df
for column in df.columns:
    unique_values = df[column].unique()
    selected_values = st.multiselect(f"Filter by {column}", unique_values)
    if selected_values:
        filtered_df = filtered_df[filtered_df[column].isin(selected_values)]

st.dataframe(filtered_df)

# download buttons for different format :
st.header('Download Data')

filtered_csv = filtered_df.to_csv().encode('utf-8')


#CSV DOWNLOAD :
csv_df = df.to_csv().encode('utf-8')
st.download_button(label='DOWNLOAD CSV', data=csv_df, file_name='amazon_product_data.csv', mime='text/csv')

#EXCEL DOWNLOAD :
output = io.BytesIO()
writer = pd.ExcelWriter(output, engine='xlsxwriter')
df.to_excel(writer, index=False, sheet_name='amazon products')
writer.save()
output.seek(0)
st.download_button(
    label='DOWNLOAD EXCEL',
    data=output,
    file_name='amazon_product_data.xlsx',
    mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
)














# st.download_button(
#     label='Download Excel',
#     data=df,
#     file_name='excel.xlsx',
#     mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
#     args=None,
#     kwargs=df
# )

# header = df.columns
# selected_value = st.selectbox("select header name", header)
# column_values = df[selected_value]
# selected_column = st.selectbox("select filter", filtered_df[selected_value].unique())
# filtered_df = filtered_df[filtered_df[selected_value] == selected_column]









#
# filtered_excel = filtered_df.to_excel('filtered_excel.xlsx', sheet_name="amazon products", index=False)
# excel_df = df.to_excel('all_data_excel.xlsx', sheet_name="amazon products", index=False)
# st.download_button(label='Download Filtered Excel', data=filtered_excel, file_name="filtered_excel.xlsx" ,mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")



#
# if st.download_button("Download CSV"):
#     csv_file = filtered_df.to_csv(index=False)
#
#
# if st.button("Download Excel"):
#     excel_file = df.to_excel(index=False)
#     st.download_button(label="Download Excel", data=excel_file, file_name="data.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
#
# if st.button("Download JSON"):
#     json_file = df.to_json(orient="records")
#     st.download_button(label="Download JSON", data=json_file, file_name="filtered.json", mime="application/json")


















#filtering column
# for column in df.columns:
#     unique_values = df[column].unique()
#     selected_value = st.multiselect(f"Filter by {column}", unique_values)
#     if selected_value:
#         filtered_df = filtered_df[filtered_df[column].isin(selected_value)]












#
# client = MongoClient(mongodb_client)
# db = client['amazon_scrape']
# products = db["products"]
















# class MongoDBPipeline(object):
#     def __int__(self):
#         connection = pymongo.MongoClient(
#             get_project_settings['mongodb_server'],
#             get_project_settings['mongodb_port']
#         )
#         db = connection[get_project_settings['mongodb_db']]
#         self.collection = db[get_project_settings['mongodb_collection']]
#
#
#
#
#
#






















# f = open('dataset_free-amazon-product-scraper_2023-08-06_04-44-51-057.json')
# data = json.load(f)

# with open('dataset_free-amazon-product-scraper_2023-08-06_04-44-51-057.csv', mode= 'r') as file: