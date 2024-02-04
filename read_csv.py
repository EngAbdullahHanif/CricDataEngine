import pandas as pd
import psycopg2
from sqlalchemy import create_engine

db_config = {
    'host': 'localhost',
    'database': 'cricdataengine',
    'user': 'hanif',
    'password': 'test123',
    'port': 5432  
}

engine = create_engine(f'postgresql+psycopg2://{db_config["user"]}:{db_config["password"]}@{db_config["host"]}:{db_config["port"]}/{db_config["database"]}')

cricbuzz_data = pd.read_csv('data/cricbuzz_data.csv')
cricket_news_info = pd.read_csv('data/cricket_news_info.csv')
team_stats_data = pd.read_csv('data/team_stats_data.csv')
player_stats_data = pd.read_csv('data/player_stats_data.csv')

try:
    
    cricbuzz_data.to_sql('Match', con=engine, if_exists='replace', index=False)

    cricket_news_info.to_sql('NewsArticle', con=engine, if_exists='replace', index=False)

    team_stats_data.to_sql('Team', con=engine, if_exists='replace', index=False)

    player_stats_data.to_sql('Player', con=engine, if_exists='replace', index=False)

    print("Data inserted successfully!")

except Exception as e:
    print(f"Error: {e}")

finally:
    engine.dispose()