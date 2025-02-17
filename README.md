# CTScans_DataEng_Assignment

# **DICOM Metadata Extraction Pipeline**  

## **📖 Overview**  
This project processes **LIDC-IDRI CT scans (DICOM format)** by extracting metadata, storing it in a database, and generating summary statistics and visualizations.  

### **🚀 Key Features**
- **DICOM Ingestion**: Reads and organizes CT scan files.  
- **Metadata Extraction**: Extracts key metadata from DICOM headers.  
- **Storage & Querying**: Stores extracted metadata in a **SQLite database**.  
- **Basic Reporting**: Computes dataset statistics.  
- **Visualization**: Generates histograms of slice thickness distribution.  

---

## **📂 Project Structure**
```
C:\DICOM_Project\
│── dicom_files\                 # Raw DICOM files (unable to load into github due to extreme size)
│── metadata.csv                  # Extracted metadata (CSV format)
│── dicom_metadata.db             # SQLite database storing metadata (unable to load into github due to extreme size)
│── extract.py                     # Extracts metadata from DICOM files
│── analysis.py                    # Stores metadata in SQLite and runs queries
│── visualize.py                   # Generates summary statistics and charts
│── README.md                      # Project documentation
```

---

## **📥 Installation & Setup**
### **1️⃣ Install Dependencies**
Ensure **Python 3.8+** is installed, then install required libraries:
```sh
pip install pydicom pandas matplotlib sqlite3
```

### **2️⃣ Clone the Repository**
```sh
git clone https://github.com/your-username/DICOM_Metadata_Pipeline.git
cd DICOM_Metadata_Pipeline
```

---

## **🛠 Steps to Run the Project**

### **1️⃣ Extract Metadata from DICOM Files**
Run the extraction script to process **DICOM files** and save metadata as **CSV**.
```sh
python extract.py
```
✅ **Output:** `metadata.csv` is created in `C:\DICOM_Project\`

---

### **2️⃣ Store Metadata in SQLite Database**
Run this script to **store extracted metadata** into a SQLite database.
```sh
python analysis.py
```
✅ **Output:** Metadata is inserted into `dicom_metadata.db`.

---

### **3️⃣ Generate Summary Statistics & Visualization**
Run the visualization script to compute **statistics** and **plot slice thickness distribution**.
```sh
python visualize.py
```
✅ **Output:**  
- **Total studies and slices** count displayed.  
- **Histogram of slice thickness** is plotted.

---

## **📊 Sample Results**
| Metric | Value |
|--------|-------|
| Total Studies | 10 |
| Total Slices | ~1400 |
| Avg Slices per Study | 140 |
| Slice Thickness Range | 1mm – 5mm |

📌 **Visualization:**  
 ![Figure_1](https://github.com/user-attachments/assets/7248f048-5f67-414d-9020-f925a2e52315)


---

## **⚡ Scalability & Future Improvements**
- **Parallel Processing:** Use **multiprocessing** to process DICOM files faster.  
- **Cloud Integration:** Store files in **Amazon S3** and process with **AWS Lambda**.  
- **Database Optimization:** Switch to **PostgreSQL** for handling large datasets.  
- **Logging & Monitoring:** Integrate **Prometheus + Grafana** for real-time monitoring.  

---
