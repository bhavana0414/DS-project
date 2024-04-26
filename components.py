# components.py
import streamlit as st

def filter_players(data):
    st.sidebar.header('Filter Options')
    # Existing filters
    nationality = st.sidebar.multiselect('Nationality', options=data['nationality'].unique(), default=data['nationality'].unique()[0])
    positions = st.sidebar.multiselect('Position', options=data['positions'].unique(), default=data['positions'].unique()[0])
    heading_accuracy = st.sidebar.slider('Heading Accuracy', int(data['heading_accuracy'].min()), int(data['heading_accuracy'].max()), (int(data['heading_accuracy'].min()), int(data['heading_accuracy'].max())))
    freekick_accuracy = st.sidebar.slider('Freekick Accuracy', int(data['freekick_accuracy'].min()), int(data['freekick_accuracy'].max()), (int(data['freekick_accuracy'].min()), int(data['freekick_accuracy'].max())))

    # New filter for preferred_foot
    preferred_foot_options = ['Both', 'Left', 'Right']
    preferred_foot = st.sidebar.radio('Preferred Foot', options=preferred_foot_options, index=0)

    # Filter logic
    if preferred_foot != 'Both':
        filtered_data = data[
            (data['nationality'].isin(nationality)) & 
            (data['positions'].str.contains('|'.join(positions))) &
            (data['heading_accuracy'].between(heading_accuracy[0], heading_accuracy[1])) &
            (data['freekick_accuracy'].between(freekick_accuracy[0], freekick_accuracy[1])) &
            (data['preferred_foot'] == preferred_foot)
        ]
    else:
        filtered_data = data[
            (data['nationality'].isin(nationality)) & 
            (data['positions'].str.contains('|'.join(positions))) &
            (data['heading_accuracy'].between(heading_accuracy[0], heading_accuracy[1])) &
            (data['freekick_accuracy'].between(freekick_accuracy[0], freekick_accuracy[1]))
        ]
    
    return filtered_data
