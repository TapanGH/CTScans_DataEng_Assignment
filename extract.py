import os
import pandas as pd
import pydicom

dest_dir = "C:\\DICOM_Project\\processed_data"

metadata_list = []
file_count = 0  # Track number of files processed

for root, _, files in os.walk(dest_dir):
    for file in files:
        if file.endswith(".dcm"):
            file_count += 1
            file_path = os.path.join(root, file)
            dicom_data = pydicom.dcmread(file_path)

            # Extract metadata
            metadata = {
                "PatientID": dicom_data.get("PatientID", "Unknown"),
                "StudyInstanceUID": dicom_data.get("StudyInstanceUID", "Unknown"),
                "SeriesInstanceUID": dicom_data.get("SeriesInstanceUID", "Unknown"),
                "FilePath": file_path,
                "SliceThickness": dicom_data.get("SliceThickness", "N/A"),
                "PixelSpacing": dicom_data.get("PixelSpacing", "N/A"),
                "AcquisitionDate": dicom_data.get("AcquisitionDate", "N/A"),
            }
            metadata_list.append(metadata)

print(f"Processed {file_count} DICOM files.")

# Convert to Pandas DataFrame
df = pd.DataFrame(metadata_list)

if not df.empty:
    # Save to CSV
    df.to_csv("C:\\DICOM_Project\\metadata.csv", index=False)
    print("✅ Metadata successfully saved to metadata.csv!")
else:
    print("⚠ No metadata extracted. Check if DICOM files are valid.")
