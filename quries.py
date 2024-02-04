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
    SELECT * FROM "Team" t
    WHERE game_type = 'TEST'
    ORDER BY rating DESC
    LIMIT 10;
'''

# Query 2: Get the latest 5 news articles
query2 = '''
    SELECT * FROM "NewsArticle"
    ORDER BY publication_date DESC
    LIMIT 5;
'''

# Query 3: Get the details of a specific match by ID
match_id = 1  
query3 = sql.SQL('''
    SELECT * FROM Match
    WHERE id = {match_id};
''').format(match_id=sql.Literal(match_id))

# Query 4: Select all teams in descending order of ratings for a specific game type
query4 = sql.SQL('''
    SELECT * FROM "Team" WHERE game_type = 'ODI' ORDER BY rating DESC;
''')

# Query 5: Find the top-rated player in Tests
query5 = sql.SQL('''
    SELECT * FROM "Player" WHERE game_type = 'TEST' ORDER BY rating DESC LIMIT 1;
''')

# query 6: Count the number of matches with a specific result
query6 = sql.SQL('''
    SELECT result, COUNT(*) FROM "Match" GROUP BY result;
''')
# query 7: Find the latest news articles
query7 = sql.SQL('''
    SELECT * FROM "NewsArticle" ORDER BY publication_date DESC LIMIT 5;
''')
# query 8: Get the average rating for all players in T20s
query8 = sql.SQL('''
    SELECT AVG(rating) FROM "Player" WHERE game_type = 'T20';
''')
# query 9: Find players with a rating above a certain threshold
query9 = sql.SQL('''
    SELECT * FROM Player WHERE rating > 800;
''')
# query 10: List players from a India 
query10 = sql.SQL('''
    SELECT * FROM "Player" WHERE country = 'India';
''')

# query 11: Find the total number of matches played
query11 = sql.SQL('''
    SELECT COUNT(*) FROM "Match";
''')
# query 12: Get the highest-rated team in each game type
query12 = sql.SQL('''
    SELECT DISTINCT ON (game_type) * FROM "Team" ORDER BY game_type, rating DESC;
''')
# query 13: Find matches where the venue is a specific location
query13 = sql.SQL('''
   SELECT * FROM "Match" WHERE venue = 'Eden Gardens';
''')


result1 = execute_query(query1)
print("Query 1 Result:")
print(result1)

result2 = execute_query(query2)
print("\nQuery 2 Result:")
print(result2)

result3 = execute_query(query3)
print("\nQuery 3 Result:")
print(result3)

result4 = execute_query(query4)
print("\nQuery 4 Result:")
print(result4)

result5 = execute_query(query5)
print("\nQuery 5 Result:")
print(result5)


result6 = execute_query(query6)
print("\nQuery 6 Result:")
print(result6)


result7 = execute_query(query7)
print("\nQuery 7 Result:")
print(result7)


result8 = execute_query(query8)
print("\nQuery 8 Result:")
print(result8)

result9 = execute_query(query9)
print("\nQuery 9 Result:")
print(result9)

result10 = execute_query(query10)
print("\nQuery 10 Result:")
print(result10)

result11 = execute_query(query11)
print("\nQuery 11 Result:")
print(result11)

result12 = execute_query(query12)
print("\nQuery 12 Result:")
print(result12)


result13 = execute_query(query13)
print("\nQuery 13 Result:")
print(result13)










