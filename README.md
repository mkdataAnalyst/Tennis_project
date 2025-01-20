🎾 Tennis Dashboard - Streamlit Application
This project is a Streamlit application that visualizes tennis competition data stored in a MySQL database. The dashboard provides insights, search functionalities, and analysis related to competitions, categories, and venues.

📋 Features
Homepage Dashboard:

Displays summary statistics (e.g., total competitions, competitions by category).
Visualizes the distribution of competition types by category.
Search and Filter Competitions:

Search competitions by name.
Filter competitions by category.
Competition Details Viewer:

View detailed information about selected competitions.
Venue-Wise Analysis:

Analyze and display the number of competitions held at each venue.
⚙️ Setup Instructions
Follow these steps to set up and run the project:

Prerequisites
Python 3.10+ installed on your machine.
MySQL Database with the required schema and data (see below).
Install required Python libraries using pip.
Database Schema
The app uses the following MySQL tables:

Categories:

sql
Copy code
CREATE TABLE Categories (
    category_id VARCHAR(50) PRIMARY KEY,
    category_name VARCHAR(100) NOT NULL
);
Competitions:

sql
Copy code
CREATE TABLE Competitions (
    competition_id VARCHAR(50) PRIMARY KEY,
    competition_name VARCHAR(100) NOT NULL,
    parent_id VARCHAR(50),
    type VARCHAR(20) NOT NULL,
    gender VARCHAR(10) NOT NULL,
    category_id VARCHAR(50),
    FOREIGN KEY (category_id) REFERENCES Categories(category_id)
);
Complexes:

sql
Copy code
CREATE TABLE Complexes (
    complex_id VARCHAR(255) PRIMARY KEY,
    complex_name VARCHAR(255)
);
Venues:

sql
Copy code
CREATE TABLE Venues (
    id VARCHAR(255) PRIMARY KEY,
    name VARCHAR(255),
    city_name VARCHAR(255),
    country_name VARCHAR(255),
    country_code VARCHAR(10),
    timezone VARCHAR(50),
    complex_id VARCHAR(255),
    FOREIGN KEY (complex_id) REFERENCES Complexes(complex_id)
);
Ensure that these tables have been populated with sample data.

Installation
Clone this repository to your local machine:

bash
Copy code
git clone https://github.com/your-username/TennisDashboard.git
cd TennisDashboard
Create a Python virtual environment (optional but recommended):

bash
Copy code
python -m venv tennis_env
source tennis_env/bin/activate  # On Windows: tennis_env\Scripts\activate
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Running the Application
Make sure your MySQL database is running, and update the app.py file with your MySQL credentials:

python
Copy code
host = 'localhost'
user = 'root'  # Replace with your MySQL username
password = 'your_password'  # Replace with your MySQL password
database = 'Tennis'  # Replace with your database name
Start the Streamlit application:

bash
Copy code
streamlit run app.py
Open the app in your browser at:

arduino
Copy code
http://localhost:8501
📊 Sample Visualizations
Category-wise Analysis:

Venue-wise Distribution:

🛠️ Technologies Used
Frontend: Streamlit
Backend: MySQL Database
Programming Language: Python
Visualization: Matplotlib, Seaborn, Pandas
📝 Future Enhancements
Add user authentication for role-based access.
Enable export of reports in PDF or Excel formats.
Integrate real-time database updates for dynamic dashboards.
👨‍💻 Author
Manoj Moorthy
Data Analyst & Developer







