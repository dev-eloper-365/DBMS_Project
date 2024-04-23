import mysql.connector
import streamlit as st

#Establish a connection to mysql server
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='9924988290',
    database='crypto'
)

mycursor = mydb.cursor()


# Create Streamlit App
def main():
    st.title("Courier Company Database")

    # Display options for operations
    option = st.sidebar.selectbox("Select Operation",("Shipment","Client","Vehicle","Delete","View"))

    # Shipment
    if option=="Shipment":
        st.subheader("Enter Shipment Details")
        shipId=st.number_input("Enter ID")
        shipFrom=st.text_input("From")
        shipTo=st.text_input("To")
        shipStatus=st.text_input("Enter status")
        if st.button("Shipment"):
            sql = "insert into shipment(ship_id,ship_from,ship_to,ship_status) values (%s,%s,%s,%s)"
            val = (shipId,shipFrom,shipTo,shipStatus)
            mycursor.execute(sql,val)
            mydb.commit()
            st.success("Shipment Successfully!!!")

    # Client
    elif option=="Client":
        st.subheader("Enter Client Details")
        clientId=st.number_input("Enter ID")
        shipId=clientId
        clientName=st.text_input("Name")
        clientPhone=st.text_input("Phone")
        clientAdd=st.text_input("Address")
        if st.button("Client"):
            sql = "insert into client(client_id,ship_id,client_name,client_phone,client_address) values (%s,%s,%s,%s,%s)"
            val = (clientId,shipId,clientName,clientPhone,clientAdd)
            mycursor.execute(sql,val)
            mydb.commit()
            st.success("Client Added Successfully!!!")

    # Vehicle
    elif option=="Vehicle":
        st.subheader("Enter Vehicle Details")
        vehicleId=st.number_input("Enter ID")
        vehicleName=st.text_input("Name")
        vehicleType=st.text_input("Type")
        if st.button("Vehicle"):
            sql = "insert into vehicles(vehicle_id,vehicle_name,vehicle_type) values (%s,%s,%s)"
            val = (vehicleId,vehicleName,vehicleType)
            mycursor.execute(sql,val)
            mydb.commit()
            st.success("Vehicle Added Successfully!!!")

    # View Database
    elif option=="View":
        st.subheader("Shipment History")
        temp="select shipment.ship_id, client.client_name, client.client_phone, client.client_address, shipment.ship_status, shipment.ship_from, shipment.ship_to from shipment inner join client on shipment.ship_id = client.ship_id"
        mycursor.execute(temp)
        result = mycursor.fetchall()
        mydb.commit()
        for row in result:
            st.write(row)

    # Delete tuple
    elif option=="Delete":
        st.subheader("Delete a Record")
        # vehid = st.number_input("Enter Vehicle ID")
        vehid = st.number_input("Enter ID")
        # clid = st.number_input("Enter Client ID")
        clid = vehid
        # shipid = st.number_input("Enter Shipement ID")
        shipid = vehid
        if st.button("Delete"):
            sql1 = "delete from vehicles where vehicle_id=%s"
            val1 = (vehid,)
            mycursor.execute(sql1,val1)
            sql2 = "delete from client where client_id=%s"
            val2 = (clid,)
            mycursor.execute(sql2,val2)
            sql3 = "delete from shipment where ship_id=%s"
            val3 =(shipid,)
            mycursor.execute(sql3,val3)
            mydb.commit()
            st.success("Record Deleted Successfully!!!")


if __name__ == "__main__":
    main()
