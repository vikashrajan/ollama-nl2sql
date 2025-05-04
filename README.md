# ollama-nl2sql
1.
Ollama NL2SQL – Natural Language to SQL with LLaMA 2 and Azure MS Sql
Open VS Code and create a new folder called:
nl2sql-llama2

2.Inside VS Code terminal, initialize a virtual environment:
python -m venv venv
venv\Scripts\activate  # On Windows
3
Install Required Packages
pip install pyodbc faker python-dotenv requests
4.
Create a file named requirements.txt in the root of your project folder with the following content:
5.
Install all dependencies from it:
pip install -r requirements.txt
6.
Run Ollama with LLaMA 2
In a separate terminal window, install and start the LLaMA 2 model locally:
bash
CopyEdit
ollama run llama2
7.
Create .env File (for DB credentials)
Inside your project folder, create a .env file:
env
SERVER=your_sql_server.database.windows.net
DATABASE=weather
USERNAME=your_user
PASSWORD=your_password
8.
Create a Python script for data loading in SQL weather database table WeatherData
9.
Create Python Script nl2sql.py
10.
Run python .\WeatherRandomdataGenerator.py to insert the data in sql table.
