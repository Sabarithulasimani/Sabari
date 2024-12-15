import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# Load the dataset
Untitled = pd.read_csv("Untitled.csv")  # Replace with your dataset path
# Preview the data
print("\nDataset Preview:\n", Untitled.head())
print("\nDataset Info:\n")
Untitled.info()
# Check for missing values
missing_values = Untitled.isnull().sum()
print("\nMissing Values:\n", missing_values)
# Drop unnecessary columns (example: 'umpire3', which has many missing values)
Untitled.drop(columns=['umpire3'], inplace=True)
# Basic statistics
print("\nBasic Statistics:\n", Untitled.describe())
# Number of Untitled played each season
matches_per_season = Untitled['season'].value_counts()
print("\nMatches Played Each Season:\n", matches_per_season)
# Visualization: Untitled per season
plt.figure(figsize=(10, 5))
matches_per_season.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Number of Untitled Played Each Season', fontsize=16)
plt.xlabel('Season', fontsize=12)
plt.ylabel('Number of Untitled', fontsize=12)
plt.xticks(rotation=45)
plt.show()
# Most successful teams (Untitled won)
wins_per_team = Untitled['winner'].value_counts()
print("\nMatches Won by Each Team:\n", wins_per_team)
# Visualization: Untitled won by each team
plt.figure(figsize=(12, 6))
wins_per_team.plot(kind='bar', color='orange', edgecolor='black')
plt.title('Total Untitled Won by Each Team', fontsize=16)
plt.xlabel('Team', fontsize=12)
plt.ylabel('Untitled Won', fontsize=12)
plt.xticks(rotation=45)
plt.show()
# Toss impact analysis
toss_winner_match_winner = Untitled[Untitled['toss_winner'] == Untitled['winner']]
toss_impact = (len(toss_winner_match_winner) / len(Untitled)) * 100
print(f"\nPercentage of Untitled Won by Toss Winners: {toss_impact:.2f}%")
# Visualization: Toss decisions
plt.figure(figsize=(8, 4))
toss_decisions = Untitled['toss_decision'].value_counts()
# Calculate the total matches played by each team
matches_played = Untitled['team1'].value_counts().add(Untitled['team2'].value_counts(), fill_value=0)
plt.title('Toss Decisions (Bat or Field)', fontsize=16)
plt.xlabel('Decision', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.show()
# Player of the Match analysis
most_player_of_match = Untitled['player_of_match'].value_counts().head(10)
print("\nTop 10 Players with Most Player of the Match Awards:\n", most_player_of_match)
# Visualization: Top players
plt.figure(figsize=(12, 6))
most_player_of_match.plot(kind='bar', color='purple', edgecolor='black')
plt.title('Top 10 Players with Most Player of the Match Awards', fontsize=16)
plt.xlabel('Player', fontsize=12)
plt.ylabel('Awards', fontsize=12)
plt.xticks(rotation=45)
plt.show()
# Win percentage of teams
matches_played = Untitled['team1'].value_counts() + Untitled['team2'].value_counts()
win_percentage = (wins_per_team / matches_played) * 100
win_percentage = win_percentage.sort_values(ascending=False)
print("\nWin Percentage of Teams:\n", win_percentage)
# Visualization: Win percentage
plt.figure(figsize=(12, 6))
win_percentage.plot(kind='bar', color='green', edgecolor='black')
plt.title('Win Percentage of Teams', fontsize=16)
plt.xlabel('Team', fontsize=12)
plt.ylabel('Win Percentage', fontsize=12)
plt.xticks(rotation=45)
plt.show()
# Save cleaned data for further analysis
Untitled.to_csv("cleaned_matches.csv", index=False)
print("\nCleaned data saved as 'cleaned_matches.csv'.")
