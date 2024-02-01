import psycopg2
from psycopg2 import sql

def execute_query(query):
    connection = psycopg2.connect(
        host="localhost",
        database="cricdataengine", 
        user="hanif",
        password="test123"
    )
    cursor = connection.cursor()

    cursor.execute(query)

    result = cursor.fetchall()

    connection.commit()
    connection.close()

    return result



# Query 1: Get the top 10 teams by rating in Test format
query1 = '''
    SELECT * FROM Team
    WHERE game_type = 'TEST'
    ORDER BY rating DESC
    LIMIT 10;
'''

# Query 2: Get the latest 5 news articles
query2 = '''
    SELECT * FROM NewsArticle
    ORDER BY publication_date DESC
    LIMIT 5;
'''

# Query 3: Get the details of a specific match by ID
match_id = 1  
query3 = sql.SQL('''
    SELECT * FROM Match
    WHERE id = {match_id};
''').format(match_id=sql.Literal(match_id))

result1 = execute_query(query1)
print("Query 1 Result:")
print(result1)

result2 = execute_query(query2)
print("\nQuery 2 Result:")
print(result2)

result3 = execute_query(query3)
print("\nQuery 3 Result:")
print(result3)
