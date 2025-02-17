import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to the SQLite database
conn = sqlite3.connect("C:\\DICOM_Project\\dicom_metadata.db")

# Load metadata into a Pandas DataFrame
df = pd.read_sql("SELECT * FROM dicom_metadata", conn)

# Close the database connection
conn.close()

# Check if data is available
if df.empty:
    print("⚠ No data found in the database. Ensure extraction and storage steps were successful.")
else:
    # Summary statistics
    print(f"Total studies: {df['StudyInstanceUID'].nunique()}")
    print(f"Total slices: {len(df)}")
    print(f"Average slices per study: {df.groupby('StudyInstanceUID').size().mean():.2f}")

    # Visualization - Histogram of Slice Thickness
    df["SliceThickness"] = pd.to_numeric(df["SliceThickness"], errors="coerce")
    df.dropna(subset=["SliceThickness"], inplace=True)

    plt.figure(figsize=(8, 5))
    plt.hist(df["SliceThickness"], bins=10, color="blue", alpha=0.7)
    plt.xlabel("Slice Thickness (mm)")
    plt.ylabel("Frequency")
    plt.title("Distribution of Slice Thickness")
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()
