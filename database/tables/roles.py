from database.Database import db

try:
    db.execute("CREATE TABLE IF NOT EXISTS roles (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))")
except Exception as e:
    raise Exception(f"Error creating table: {e}")