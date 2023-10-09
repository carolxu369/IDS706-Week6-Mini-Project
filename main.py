import mysql.connector

def create_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="db"
    )

def execute_complex_query(connection):
    cursor = connection.cursor(dictionary=True)
    query = """
    SELECT category, SUM(sales_amount) AS total_sales
    FROM products
    JOIN sales ON products.product_id = sales.product_id
    GROUP BY category
    ORDER BY total_sales DESC;
    """
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    return results

if __name__ == "__main__":
    connection = create_connection()

    query_results = execute_complex_query(connection)

    print("Category\tTotal Sales")
    for row in query_results:
        print(f"{row['category']}\t\t{row['total_sales']}")

    connection.close()
