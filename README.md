![image](https://github.com/user-attachments/assets/d4feee07-43a0-43d0-bd42-8f9c2b6e7074)


Open VS Code and create a new folder called:
nl2sql-llama2
 ![image](https://github.com/user-attachments/assets/ed803a28-a250-4950-801a-a5a0bb101578)


Inside VS Code terminal, initialize a virtual environment:
python -m venv venv
venv\Scripts\activate  # On Windows
 ![image](https://github.com/user-attachments/assets/a2694c79-fa9c-46b4-b00c-f1287567e076)
![image](https://github.com/user-attachments/assets/9673c75b-fca4-46e9-b375-e08f337fc1d0)

 
Install Required Packages
pip install pyodbc faker python-dotenv requests
 ![image](https://github.com/user-attachments/assets/2a78c2ce-3e49-48a3-9e65-d0e75e25261c)

Create a file named requirements.txt in the root of your project folder with the following content:
 ![image](https://github.com/user-attachments/assets/e06cd0d6-1286-4e84-a362-4fa92e3319bb)

Install all dependencies from it:
pip install -r requirements.txt
 ![image](https://github.com/user-attachments/assets/c2932824-f2be-4ebb-b93b-ddedde845b3a)


Run Ollama with LLaMA 2
In a separate terminal window, install and start the LLaMA 2 model locally:
bash
CopyEdit
ollama run llama2


Create .env File (for DB credentials)
Inside your project folder, create a .env file:
env
SERVER=your_sql_server.database.windows.net
DATABASE=weather
USERNAME=your_user
PASSWORD=your_password
 
![image](https://github.com/user-attachments/assets/8c6f3e89-f80a-433a-9546-e39bd1090718)
Create a Python script for data loading in SQL weather database table WeatherData
![image](https://github.com/user-attachments/assets/9fe6b03d-292e-4ae1-be20-6ba3245a5e11)



Create Python Script nl2sql.py
 ![image](https://github.com/user-attachments/assets/2533d5af-6061-4776-8eef-a03b11fc9169)

Run python .\WeatherRandomdataGenerator.py to insert the data in sql table.
 ![image](https://github.com/user-attachments/assets/94b96fe8-999d-4aa5-bc1c-41afed8070bc)

Ask the Questions "How many records available in table weather" As per the below:
![image](https://github.com/user-attachments/assets/545eae4b-058f-450a-9e31-13081c054a37)


