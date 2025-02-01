from database.Database import cursor,connect


class Tables:
    def __init__(self, table_name):
        self.table_name = table_name

    def __str__(self):
        return f"""
            Table: {self.table_name}
        """
    
    def create(self, schema):
        query = f"CREATE TABLE IF NOT EXISTS {self.table_name} ({schema})"
        try:
            cursor.execute(query)
            connect.commit()
        except Exception as e:
            raise Exception(f"Error creating table: {e}")



