import ctypes
import sqlite3

# Load C library
fastlog = ctypes.CDLL("c_lib/libfastlog.dylib")

# Define function input/output types
fastlog.count_chars.argtypes = [ctypes.c_char_p]
fastlog.count_chars.restype = ctypes.c_int

# Test string
text = b"FastLog Demo"

# Call C function
result = fastlog.count_chars(text)

print("Character Count:", result)

# Connect to SQLite database
conn = sqlite3.connect("../db/fastlog.db")
cursor = conn.cursor()

# Create table if it does not exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    text TEXT,
    char_count INTEGER
)
""")

# Insert result into database
cursor.execute(
    "INSERT INTO logs (text, char_count) VALUES (?, ?)",
    (text.decode(), result)
)

# Save changes
conn.commit()

print("Data stored in database.")

# Close database
conn.close()