import psycopg2
import time
from db.config.config import Config

class DatabaseConnection:
    MAX_RETRY = 3
    TIME_RETRY_BETWEEN_RETRY_SEC = 10

    def __init__(self):
        print('Connect to the PostgreSQL database server')
        self.config = Config()
        self.db_connection = self.connect(self.config.load_config())
    # END __init__(self)

    def connect(self, config):
        i = 1
        while i <= DatabaseConnection.MAX_RETRY:            
            print('Connect to the PostgreSQL database server. Try: ' + str(i))
            try:
                # connecting to the PostgreSQL server
                with psycopg2.connect(**config) as conn:
                    print('Connected to the PostgreSQL server.')
                    return conn
            except (psycopg2.DatabaseError, Exception) as error:
                print(error)
            time.sleep(DatabaseConnection.TIME_RETRY_BETWEEN_RETRY_SEC)
            i += 1
    # END connect(config)

# END class DatabaseConnection