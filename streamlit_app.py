# Example: Fetch data from a remote server using requests"http://216.48.183.9:3030/companies/"
# app.py
import streamlit as st
import requests
import pandas as pd  

def get_remote_data():
    try:
        url = "http://216.48.183.9:3030/companies/"
        response = requests.get(url)

        response.raise_for_status()

        data = response.json()

        # Edit the data as needed
        edited_data = process_data(data)

        return edited_data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

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

        # Visualize the edited data in a styled DataFrame
        st.write("Edited data from the remote server:")
        st.dataframe(df.style.set_properties(**{'text-align': 'center'}).set_table_styles([{
            'selector': 'th',
            'props': [('text-align', 'center')]
        }]))

        # Example: Display a line chart
        # Note: This assumes 'sl.num:' is a key in your JSON data; adjust accordingly
        if 'sl.num:' in df.columns:  # Checking for the existence of the column
            st.line_chart(df['sl.num:'])

if __name__ == "__main__":
    main()
