import psycopg2
from psycopg2 import sql

def create_tables():
    connection = psycopg2.connect(
        host="localhost",
        port= 5432,
        database="cricdataengine",
        user="hanif",
        password="test123"
    )
    cursor = connection.cursor()

    # Create Team table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Team (
            id SERIAL PRIMARY KEY,
            name TEXT,
            rating INTEGER,
            points INTEGER,
            game_type TEXT
        );
    ''')

    # Create Player table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Player (
            id SERIAL PRIMARY KEY,
            name TEXT,
            country TEXT,
            rating INTEGER,
            game_type TEXT,
            category TEXT
        );
    ''')

    # Create Match table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Match (
            id SERIAL PRIMARY KEY,
            match_name TEXT,
            venue TEXT,
            result TEXT
        );
    ''')

    # Create NewsArticle table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS NewsArticle (
            id SERIAL PRIMARY KEY,
            headline TEXT,
            content TEXT,
            author TEXT,
            publication_date DATE
        );
    ''')

    connection.commit()
    connection.close()

def main():
    create_tables()
    print("Tables created successfully.")

if __name__ == "__main__":
    main()


# psql -d cricdataengine -U hanif