import streamlit as st

# Title for the App
st.title("Search from List")

# List of locations and companies
search_list = [
    'Kormanagala', 'HSR layout', 'Ejipura', 'Venkatapura', 'Marathalli road', 'Silk road',
    'Tech mahindra', 'Siemens tech', 'TCS', 'Scalar at pvt ltd', 'Lavender tech', 
    'Xavier institute', 'Ajmera Nucleus', 'Think campus Globe', 'Semicon Park',
    'Tessolve Semiconductor Private Limited', 'ITC 5 path', 'Biocon academy',
    'Attra infotech', 'Gold Hill Supreme (GHS)', 'Gold Hill Excelsior Park'
]

# Input box to accept user search term
search_term = st.text_input("Enter a location or company to search:")

# If the user has entered a search term
if search_term:
    # Convert both search term and list items to lowercase for case-insensitive search
    search_term_lower = search_term.lower()
    search_results = [item for item in search_list if search_term_lower in item.lower()]
    
    if search_results:
        # Display matching results
        st.write("Found the following matches:")
        for result in search_results:
            st.write(f"- {result}")
    else:
        # If no matches are found
        st.write("Not found")
