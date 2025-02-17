import sqlite3
import pandas as pd

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect("C:\\DICOM_Project\\dicom_metadata.db")
cursor = conn.cursor()

# Create a table for DICOM metadata if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS dicom_metadata (
        PatientID TEXT,
        StudyInstanceUID TEXT,
        SeriesInstanceUID TEXT,
        FilePath TEXT,
        SliceThickness TEXT,
        PixelSpacing TEXT,
        AcquisitionDate TEXT
    )
''')

# Read metadata from CSV
df = pd.read_csv("C:\\DICOM_Project\\metadata.csv")

# Insert metadata into the database
df.to_sql("dicom_metadata", conn, if_exists="replace", index=False)

print("✅ Metadata successfully stored in SQLite database!")

# Query and display basic statistics
cursor.execute("SELECT COUNT(*) FROM dicom_metadata")
total_records = cursor.fetchone()[0]

print(f"📊 Total records in the database: {total_records}")

# Close database connection
conn.close()
