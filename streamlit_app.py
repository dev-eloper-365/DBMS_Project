
import streamlit as st
import mysql.connector

# Connect to MySQL database
def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="9924988290",
            database="crypto"
        )
        if connection.is_connected():
            db_info = connection.get_server_info()
            st.success(f"Connected to MySQL Server version {db_info}")
            return connection
    except mysql.connector.Error as e:
        st.error(f"Error connecting to MySQL: {e}")
        return None

# Function to execute SQL query
def execute_query(connection, query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        return cursor
    except mysql.connector.Error as e:
        st.error(f"Error executing query: {e}")
        return None

# Streamlit app
def main():
    st.title("MySQL Database App")

    # Connect to database
    connection = connect_to_database()
    if connection is not None:
        # Display data from the database
        st.subheader("Display Data from MySQL Database")
        cursor = execute_query(connection, "SELECT * FROM example_table")
        if cursor is not None:
            data = cursor.fetchall()
            for row in data:
                st.write(row)

        # Insert new data into the database
        st.subheader("Insert Data into MySQL Database")
        name = st.text_input("Enter Name:")
        age = st.number_input("Enter Age:")
        if st.button("Insert"):
            query = f"INSERT INTO example_table (name, age) VALUES ('{name}', {age})"
            execute_query(connection, query)
            st.success("Data inserted successfully!")

if __name__ == "__main__":
    main()
