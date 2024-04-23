import streamlit as st
import mysql.connector as connector

# Connect to MySQL database
def connect_to_database():
    try:
        connection = connector.connect(
            host="localhost",  # Replace with your host
            user="root",       # Replace with your username
            password="9924988290",   # Replace with your password
            database="crypt"    # Replace with your database name
        )
        if connection.is_connected():
            st.success("Connected to MySQL Server")
            return connection
    except connector.Error as e:
        st.error(f"Error connecting to MySQL: {e}")
        return None

# Streamlit app
def main():
    st.title("MySQL Database Connection")

    # Connect to database
    connection = connect_to_database()
    if connection is not None:
        # Perform database operations here
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM your_table")  # Replace your_table with your actual table name
        data = cursor.fetchall()
        st.write("Data from MySQL Database:")
        st.write(data)

        connection.close()  # Close the connection when done

if __name__ == "__main__":
    main()
