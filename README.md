# Webcam Filter Application

This project applies various filters to a webcam feed using Python and Flask.

**Linux**
- to create dependency file use `pip freeze > requirements.txt`
- to install environment run  `chmod +x setup_env.sh` then `./setup_env.sh`

**Windows**
- Double-click the `setup_env.bat` file or run it from the command line

## Features
- Grayscale filter with adjustable intensity
- Canny edge detection with adjustable thresholds
- Gaussian blur with adjustable kernel size
- Laplacian filter with adjustable scale
- Sobel filter with adjustable kernel size

### Video
https://github.com/user-attachments/assets/7971fb5e-eca2-4373-b257-77fc56e1d810

### Grayscale Filter
![Grayscale Filter](images/Grayscale%20Filter.png)

### Canny Edge Detection
![Canny Edge Detection](images/Canny%20Edge%20Detection.png)

### Gaussian Blur
![Gaussian Blur](images/Gaussian%20Blur.png)

### Laplacian Filter
![Laplacian Filter](images/Laplacian%20Filter.png)

### Sobel Filter
![Sobel Filter](images/Sobel%20Filter.png)

## How to Run
1. Clone the repository
2. Create a virtual environment and install dependencies
3. Run the Flask app
4. Open your browser and go to `http://127.0.0.1:5000/`
