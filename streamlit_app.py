# app.py
import streamlit as st
import requests
import pandas as pd

def get_remote_data():
    try:
        url = "http://0.0.0.0:3030/companies/"
        response = requests.get(url)

        response.raise_for_status()

        data = response.json()

        # Edit the data as needed
        edited_data = process_data(data)

        return edited_data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def update_remote_data(updated_data):
    try:
        url = "http://0.0.0.0:3030/companies/"
        headers = {"Content-Type": "application/json"}
        response = requests.put(url, json=updated_data, headers=headers)

        response.raise_for_status()

        print("Data updated successfully")
    except requests.exceptions.RequestException as e:
        print(f"Error updating data: {e}")

def process_data(data):
    # Example: Add a new column to the data
    for entry in data:
        # Check if 'existing_column' exists in the entry before performing the multiplication
        if 'existing_column' in entry:
            entry['new_column'] = entry['existing_column'] * 2
        else:
            # Handle the case where 'existing_column' is not present
            entry['new_column'] = None  # or perform any other action based on your requirements

    return data

def main():
    st.title("Remote Data Visualization")

    # Fetch and process data
    remote_data = get_remote_data()

    if remote_data is not None:
        # Convert the data to a DataFrame for better formatting
        df = pd.DataFrame(remote_data)
        st.data_editor(
            df,
            column_config={
                "logo_url": st.column_config.ImageColumn(
                    "logo_url", help="Streamlit app preview screenshots"
                )
            },
            hide_index=True,
        )

        # Add an update button to modify and update the data
        if st.button("Update Data"):
            # Modify the data as needed
            updated_data = process_data(remote_data)

            # Update the remote data
            update_remote_data(updated_data)

            # Display a success message
            st.success("Data updated successfully!")

if __name__ == "__main__":
    main()
