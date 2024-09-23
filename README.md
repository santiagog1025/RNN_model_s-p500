<b>S&P 500 Data Collection and Statistical Analysis Project</b>

Project Overview

This project aims to perform a comprehensive statistical analysis of the S&P 500 index and its constituents. The goal is to gather historical data for the S&P 500 companies and the S&P 500 index itself, and then apply various statistical and financial analysis techniques to understand market trends, company performance, and the overall health of the index over time.

The project is in its initial stage, focusing on:

Data Collection:

We are fetching historical data for all the companies that are part of the S&P 500 using the Yahoo Finance API (yfinance).
The data is collected for each company's ticker symbol, along with the main S&P 500 index (^GSPC).
Data includes daily closing prices, volumes, and other key financial metrics.
The current period of focus is the last 5 years, with plans to expand to a 10-year analysis.

Storage:

Data is being stored in both CSV format for immediate access (prueba.csv, syp500.csv) and in a SQL Server database for long-term storage and more complex querying.
The connection to SQL Server is established using pyodbc to facilitate future data processing and querying needs.
Next Steps:

<b>Data Cleaning:</b> Ensure that the data is properly cleaned, formatted, and normalized.
<b>Descriptive Statistics:</b> Compute basic statistics like mean, median, variance, standard deviation for each stock and the overall S&P 500 index.

<b>Visualization:</b> Create interactive charts and visualizations to represent stock performance over time.

<b>Predictive Analysis:</b> Explore predictive modeling using machine learning techniques to forecast stock movements.

Key Files

main.py:

This Python script is responsible for fetching and processing the data from Yahoo Finance using yfinance.

It collects the data of the S&P 500 companies and stores it in a CSV file (prueba.csv).

It also downloads the historical data for the main S&P 500 index (^GSPC) and stores it in another CSV file (syp500.csv).


How to Run the Code

Prerequisites:

Install the required Python libraries:
pandas
yfinance
pyodbc
sqlalchemy
webdriver_manager (if you need to automate fetching data from websites)
bash
Copia codice
pip install pandas yfinance pyodbc sqlalchemy webdriver_manager
Ensure that you have an ODBC connection configured for SQL Server, and the necessary drivers installed (ODBC Driver 17 for SQL Server).
Running the Script
Run the Python script (main.py):

This will connect to Yahoo Finance, fetch the required data, and store it in both CSV format and a SQL Server database.

SQL Server:

Once the connection is set up, you can query the data from the SQL Server database for further analysis and visualization.

Future Plans

Extend the time frame to 10 years for more comprehensive analysis.
Automate the regular updating of data.
Perform deeper analysis, including volatility, momentum indicators, moving averages, and correlation analysis among S&P 500 companies.
Integrate interactive visualizations using libraries such as matplotlib, seaborn, plotly, or Power BI/Tableau.
Apply machine learning models to forecast stock trends and simulate portfolio strategies.

Author

This project is part of an ongoing initiative to develop advanced statistical and financial analysis skills, starting with the S&P 500 as a case study. Stay tuned for more updates and features as the project evolves.
