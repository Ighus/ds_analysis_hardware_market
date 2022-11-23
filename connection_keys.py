# import pyodbc as pydb
import os
from sqlalchemy import create_engine, event
from urllib.parse import quote_plus
import json

GCP_PROJECT_ID = os.environ['GCP_PROJECT_ID']
GCP_SERVICE_ACCOUNT_FILE = os.environ['GCP_SERVICE_ACCOUNT_FILE']

from google.cloud import bigquery
from google.oauth2 import service_account

#=====================================================
# Chaves de conexão com Banco de dados
#------------------------------------------------------ 
server_bd_corporativo = 'localhost'
username_bd_corporativo = 'sa'
password_bd_corporativo = 'P4ssw0rd'
driver = '{ODBC Driver 17 for SQL Server}'


# def connection(database):
#     connection = string_connection_odbc(database)
#     return pydb.connect(connection)


def alchemy_connection(database):
    con = 'mssql+pyodbc:///?odbc_connect={}'.format(string_connection(database))
    return create_engine(con)


def string_connection_odbc(database):
    con = 'DRIVER='+driver+';SERVER='+server_bd_corporativo+';PORT=1433;DATABASE='+database+';UID='+username_bd_corporativo+';PWD='+password_bd_corporativo
    return con


def string_connection(database):
    return quote_plus('DRIVER='+driver+';SERVER='+server_bd_corporativo+';DATABASE='+database+';UID='+username_bd_corporativo+';PWD='+password_bd_corporativo)


def connect_bq_client():
    credentials = service_account.Credentials.from_service_account_info(json.loads(GCP_SERVICE_ACCOUNT_FILE))
    client = bigquery.Client(credentials=credentials, project=GCP_PROJECT_ID)
    return client