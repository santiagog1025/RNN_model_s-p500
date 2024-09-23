import pandas as pd
import yfinance as yf
import pyodbc
from keys import server,database

# Obtener la lista de constituyentes del S&P 500 desde Wikipedia
url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
sp500_table = pd.read_html(url)

# La primera tabla contiene los datos que queremos
sp500_df = sp500_table[0]

# Extraer solo los tickers
tickers = sp500_df['Symbol'].tolist()

# Conectarse a la base de datos de SQL server, para esto importa los datos de un .py llamado keys
try:    
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes')
    print('Conexión exitosa')
except:
    print('Error')
    # Crear una lista para almacenar los datos de las empresas
data = []
# Función para obtener información de cada ticker
def obtener_datos_ticker(ticker):
    empresa = yf.Ticker(ticker)
    datos = empresa.history(period="1d")  # Datos diarios
    return datos
# Establecer el máximo periodo posible y frecuencia diaria (1d)
period = "max"
interval = "1d"

# Función para obtener información de cada ticker
def obtener_datos_daily(ticker):
    empresa = yf.Ticker(ticker)
    datos = empresa.history(period=period, interval=interval)  # Datos de los últimos 5 años diarios
    datos['Ticker'] = ticker  # Agregar columna con el ticker
    return datos

# Recorrer los tickers y obtener sus datos
for ticker in tickers:
    try:
        datos_empresa = obtener_datos_ticker(ticker)
        datos_empresa['Ticker'] = ticker  # Agregar ticker a los datos
        data.append(datos_empresa)  # Almacenar los datos de la empresa
    except Exception as e:
        print(f"Error al obtener datos para {ticker}: {e}")

# Concatenar todos los DataFrames en uno solo
df_datos_empresas = pd.concat(data)
# Cerrar la conexión
conn.close()
df_datos_empresas.to_csv('prueba.csv')
# Cojemos el S&p500 de vanguard y lo llevamos a 10 años
df_syp500 = obtener_datos_daily("SPY")
df_syp500.to_csv('syp500.csv')
