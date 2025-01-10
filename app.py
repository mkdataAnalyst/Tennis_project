import streamlit as st
import pandas as pd
import mysql.connector  # MySQL connection
import plotly.express as px

# Database connection (MySQL)
def get_connection():
    conn = mysql.connector.connect(
        host='localhost',      # Replace with your MySQL host
        user='root',  # Replace with your MySQL username
        password='Bb$alws90m!',  # Replace with your MySQL password
        database='Tennis'      # Database name
    )
    return conn

def load_data(query):
    conn = get_connection()
    df = pd.read_sql(query, conn)
    conn.close()
    return df

def main():
    st.title("Tennis Competitions Dashboard")

    # Sidebar filters
    st.sidebar.header("Filters")
    categories = load_data("SELECT DISTINCT category_name FROM Categories")
    types = load_data("SELECT DISTINCT type FROM Competitions")
    genders = load_data("SELECT DISTINCT gender FROM Competitions")

    selected_category = st.sidebar.multiselect("Select Category", categories['category_name'])
    selected_type = st.sidebar.multiselect("Select Type", types['type'])
    selected_gender = st.sidebar.multiselect("Select Gender", genders['gender'])

    # Dynamic query based on filters
    query = """
        SELECT c.competition_id, c.competition_name, c.type, c.gender, cat.category_name
        FROM Competitions c
        JOIN Categories cat ON c.category_id = cat.category_id
        WHERE 1=1
    """

    if selected_category:
        query += f" AND cat.category_name IN ({','.join(['\'' + cat + '\'' for cat in selected_category])})"
    if selected_type:
        query += f" AND c.type IN ({','.join(['\'' + typ + '\'' for typ in selected_type])})"
    if selected_gender:
        query += f" AND c.gender IN ({','.join(['\'' + gen + '\'' for gen in selected_gender])})"

    df = load_data(query)

    # Display data
    st.subheader("Filtered Competitions")
    st.dataframe(df)

    # Visualization
    if not df.empty:
        fig = px.bar(df, x='competition_name', color='gender', barmode='group',
                     title='Competitions by Gender')
        st.plotly_chart(fig)
    else:
        st.info("No data available for the selected filters.")

if __name__ == '__main__':
    main()
