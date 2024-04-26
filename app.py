# app.py
import streamlit as st
from data_loader import load_data
from visuals import plot_player_ratings, wage_vs_value_scatter, age_distribution, national_team_analysis
from components import filter_players
from performance_index import calculate_ppi

# Load data
df = load_data(r'fifa_players.csv')

# Calculate Performance Index
df = calculate_ppi(df)

# Setting Streamlit page configuration for a wide layout and page title.
st.set_page_config(layout="wide", page_title="FIFA Players Dashboard")

def main():
    
    st.sidebar.markdown("### Presenter: Bhavana")
    st.sidebar.markdown("Contact: lingareddy.c@northeastern.edu")

    # Dashboard Title
    st.title('FIFA Players Dashboard')

    # Filtered Data based on sidebar selection
    filtered_data = filter_players(df)

    # Display Filtered Data
    st.write("### Detailed Data View based on the filters", filtered_data)

    st.write("### Player Performance Index (PPI)", filtered_data[['name', 'ppi']] \
             .sort_values('ppi', ascending=False) \
             .reset_index(drop=True))
    st.write("NOTE: More the Player Performance Index better the player")

    # Layout for Visualizations
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("#### Distribution of Player Ratings")
        st.pyplot(plot_player_ratings(filtered_data))
    
    with col2:
        st.write("#### Age Distribution")
        st.pyplot(age_distribution(filtered_data))
        
    with col3:
        st.write("#### Wage vs. Value Analysis")
        st.pyplot(wage_vs_value_scatter(filtered_data))
        
    # Additional Features Section
    st.write("### Club Value Analysis")
    # st.pyplot(club_value_analysis(filtered_data))
    
    st.write("### National Team Analysis")
    st.pyplot(national_team_analysis(filtered_data))

    

if __name__ == "__main__":
    main()
