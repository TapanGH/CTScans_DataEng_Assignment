import os
import shutil
import pydicom

# Define source and destination directories
source_dir = "C:\\DICOM_Project\\dicom_files\\lidc_small_dset"
dest_dir = "C:\\DICOM_Project\\processed_data"

# Ensure destination directory exists
os.makedirs(dest_dir, exist_ok=True)

# Traverse through all DICOM files
for root, _, files in os.walk(source_dir):
    for file in files:
        if file.endswith(".dcm"):
            file_path = os.path.join(root, file)

            # Read DICOM file metadata
            dicom_data = pydicom.dcmread(file_path)
            patient_id = dicom_data.PatientID
            study_uid = dicom_data.StudyInstanceUID
            series_uid = dicom_data.SeriesInstanceUID

            # Create target directory structure
            target_dir = os.path.join(dest_dir, patient_id, study_uid, series_uid)
            os.makedirs(target_dir, exist_ok=True)

            # Move the file to its respective folder
            shutil.copy(file_path, os.path.join(target_dir, file))
            print(f"Moved: {file_path} → {target_dir}")
