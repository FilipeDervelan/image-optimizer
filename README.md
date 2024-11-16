
# 📷 Image Optimizer  

## Overview  
The **Image Optimizer** is a Python script designed to reduce the file size of images to under 1 MB while maintaining an acceptable level of quality. It's particularly effective for compressing JPEG images but can also handle other formats with some limitations.  

The script works by progressively lowering the image quality until the desired file size is achieved or a minimum quality threshold is reached. It also preserves the image's correct orientation using metadata.  

---

## Requirements  
- **Python** 3.6 or higher  
- **Pillow** library  

### Installation  
To install the required dependencies, use:  
```bash
python -m venv venv # To create a virtual environment
source venv/bin/activate  # On Linux/Mac
venv\Scripts\activate     # On Windows

pip install -r requeriments.txt
```  

---

## Usage  

1. **Set up a virtual environment (optional):**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Linux/Mac
   venv\Scripts\activate     # On Windows
   ```  

2. **Prepare your script and images:**  
   - Place the script and the image you want to compress in the same directory.  
   - Update the script to reflect the input image file name (e.g., `image.jpg`) and optionally the output file name (e.g., `image_output.jpg`).  

3. **Run the script:**  
   ```bash
   python main.py
   ```  

---

## How It Works  

1. **Loads the Input Image:**  
   The script opens the specified image file (e.g., `image.jpg`).  

2. **Compresses the Image:**  
   - Iteratively reduces the quality by 5% until the image size is below 1 MB.  
   - Optimizes the image further to reduce its size.  

3. **Saves the Result:**  
   - If successful, the compressed image is saved with the specified output file name (default: `image_output.jpg`).  
   - The script outputs the final quality and size of the compressed file.  

---

## Script Parameters  

- **`max_size`**  
  - Maximum allowed size for the output image (in bytes).  
  - **Default:** `1 * 1024 * 1024` (1 MB)  

- **`quality`**  
  - Initial quality for the image (range: 1–95). The script reduces this value iteratively.  
  - **Default:** `95`  

---

## Supported Formats  

- **JPEG/JPG:** Fully supported, with quality adjustment and optimization.  
- **PNG:** Compression without quality adjustment (only `optimize=True` is applied).  
- **Other formats (e.g., GIF, BMP, TIFF):** Processing is possible, but results may vary.  

---

## Example Output  
### Successful Compression:  
```  
Original image size: 2.34 MB  
Image saved with quality 80% and size 980.45 KB  
```  

### Failure to Meet the Size Requirement:  
```  
Unable to reduce image below 1 MB with acceptable quality.  
```  

---

## Customizations  

- **Change the Maximum Size:**  
  Modify the `max_size` parameter in the script to set your desired limit (in bytes).  

