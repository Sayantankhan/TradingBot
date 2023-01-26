import psycopg2
import psycopg2.extras
import os

class DbConnection:
    
    def __init__(self):
        self.conn = psycopg2.connect(database=os.getenv('DB_NAME'),
                        host=os.getenv('DB_HOST'),
                        user=os.getenv('DB_USER'),
                        password=os.getenv('DB_PASSWORD'),
                        port=os.getenv('DB_PORT'))
        self.cursor = self.conn.cursor()

    def saveToDatabaseByBatch(self, data={}, keys=[], stock=""):
        values = []
        for key in keys:
            doc = data.get(key)
            open = doc.get("1. open")
            high = doc.get("2. high")
            low = doc.get("3. low")
            close = doc.get("4. close")
            volume = doc.get("5. volume")
            values.append([stock, open, close, high, low, key, volume])
            print(doc)
        
        # psycopg2.extras.execute_batch(self.cursor, "INSERT INTO {table} (stock_name, open, close, high, low, timestamp, volume) VALUES (%s, %s, %s, %s, %s, %s, %s)".format(table="t_real_time_stock_data"),
        #                                 values)
        # self.conn.commit()