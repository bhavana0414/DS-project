# visuals.py
import matplotlib.pyplot as plt
import seaborn as sns

def plot_player_ratings(data):
    if data.empty:
        plt.figure(figsize=(10, 6))
        plt.text(0.5, 0.5, 'No data available', horizontalalignment='center', verticalalignment='center')
        plt.title('Distribution of Player Ratings')
        plt.xlabel('Ratings')
        plt.ylabel('Number of Players')
        plt.grid(True)
        plt.tight_layout()
        return plt.gcf()
    
    plt.figure(figsize=(10, 6))
    unique_ratings = data['overall_rating'].nunique()
    bins = max(10, unique_ratings)  # Ensure at least 10 bins or as many as unique ratings
    sns.histplot(data['overall_rating'], kde=False, color='blue', bins=bins)
    plt.title('Distribution of Player Ratings')
    plt.xlabel('Ratings')
    plt.ylabel('Number of Players')
    plt.grid(True)
    plt.tight_layout()
    return plt.gcf()

def wage_vs_value_scatter(data):
    if data.empty:
        plt.figure(figsize=(10, 6))
        plt.text(0.5, 0.5, 'No data available', horizontalalignment='center', verticalalignment='center')
        plt.title('Player Wage vs. Value')
        plt.xlabel('Market Value (Euro)')
        plt.ylabel('Wage (Euro)')
        plt.grid(True)
        plt.tight_layout()
        return plt.gcf()
    
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='value_euro', y='wage_euro', hue='preferred_foot', data=data, alpha=0.6)
    plt.title('Player Wage vs. Value')
    plt.xlabel('Market Value (Euro)')
    plt.ylabel('Wage (Euro)')
    plt.grid(True)
    plt.tight_layout()
    return plt.gcf()

def age_distribution(data):
    if data.empty:
        plt.figure(figsize=(10, 6))
        plt.text(0.5, 0.5, 'No data available', horizontalalignment='center', verticalalignment='center')
        plt.title('Age Distribution of Players')
        plt.xlabel('Age')
        plt.ylabel('Count')
        plt.grid(True)
        plt.tight_layout()
        return plt.gcf()
    
    plt.figure(figsize=(10, 6))
    bins = max(10, data['age'].nunique())  # Ensure at least 10 bins or as many as unique ages
    sns.histplot(data['age'], bins=bins, kde=True, color='green')
    plt.title('Age Distribution of Players')
    plt.xlabel('Age')
    plt.ylabel('Count')
    plt.grid(True)
    plt.tight_layout()
    return plt.gcf()


def national_team_analysis(data):
    national_teams = data[data['national_team'] != 'Not Applicable']
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.boxplot(x='national_team', y='overall_rating', data=national_teams)
    ax.set_title('National Team Performance Ratings')
    ax.set_xlabel('National Team')
    ax.set_ylabel('Overall Rating')
    plt.xticks(rotation=45)
    return fig

