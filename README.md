# Image Filter App

The Image Filter App is a web application that allows users to upload an image and apply various filters to enhance or modify it. It is built using JavaScript and Python, providing an easy-to-use interface for image processing tasks.

### Video
https://github.com/user-attachments/assets/7971fb5e-eca2-4373-b257-77fc56e1d810

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Filter Details](#filter-details)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Installation

### Prerequisites

**Linux**
- to create dependency file use `pip freeze > requirements.txt`
- to install environment run  `chmod +x setup_env.sh` then `./setup_env.sh`

**Windows**
- Double-click the `setup_env.bat` file or run it from the command line

List any software, packages, or tools that are required before installing the project:

- Python 3.x
- Node.js
- Flask
- Any other dependencies...

### Steps

To install this project, clone the repository and install the necessary dependencies:

```bash
# Clone this repository
git clone https://github.com/rkarmaka98/Image-filter-app.git

# Navigate to the project directory
cd Image-filter-app

# Install dependencies for the frontend
npm install

# Install Python dependencies
pip install -r requirements.txt
```


## Usage

To start the application, follow these steps:

```bash
# Start the backend server
python app.py

# Start the frontend application
npm start
```

After running the above commands, the application will be accessible at `http://localhost:3000`. Users can upload an image and apply different filters from the provided interface.

## Features

- **Image Upload**: Upload images from your local device.
- **Filter Effects**: Apply various filters such as grayscale, sepia, blur, and more.
- **Download Processed Image**: Download the filtered image after processing.

## Filter Details

This section provides details about each filter used in the application, including their scientific background and visual effects represented by curves.

### Grayscale Filter

![Grayscale Filter](images/Grayscale%20Filter.png)
The grayscale filter converts a colored image into shades of gray by removing the hue and saturation information while retaining the luminance. This is typically done by calculating a weighted average of the red, green, and blue channels. The transformation function can be represented as:

`Y = 0.299R + 0.587G + 0.114B`

Where `Y` represents the resulting grayscale intensity, and `R`, `G`, and `B` are the red, green, and blue color values, respectively. This weighted combination ensures a perceptually balanced representation of the original image.

### Laplacian Filter

![Laplacian Filter](images/Laplacian%20Filter.png)

The Laplacian filter is another edge detection filter that uses a single convolution kernel to highlight areas of rapid intensity change. It is often used after smoothing the image with a Gaussian filter to reduce noise. The Laplacian kernel is typically represented as:

```L = [[0, 1, 0], [1, -4, 1], [0, 1, 0]]```

The Laplacian filter is useful for detecting edges in all directions simultaneously.


### Sobel Filter

![Sobel Filter](images/Sobel%20Filter.png)

The Sobel filter is used for edge detection by calculating the gradient of the image intensity in both horizontal and vertical directions. It uses two 3x3 convolution kernels to detect changes in intensity, highlighting edges in the image. The convolution kernels are represented as:

```Gx = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], Gy = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]```

The magnitude of the gradient can be calculated as:

```G = sqrt(Gx^2 + Gy^2)```

This helps in identifying edges where there are rapid changes in intensity, making the objects within the image more distinct.


### Gaussian Blur Filter

![Gaussian Blur](images/Gaussian%20Blur.png)
The Gaussian function for blurring can be represented as:

```G(x, y) = (1 / (2 * pi * sigma^2)) * exp(-(x^2 + y^2) / (2 * sigma^2))```

Where G(x, y) is the value of the Gaussian function at point (x, y), and σ is the standard deviation that controls the amount of blur. The larger the value of σ, the greater the blurring effect.

### Brightness Adjustment

The brightness adjustment filter modifies the overall lightness of an image by adding a constant value to all pixel intensities. This can be represented as:

`I' = I + B`

Where `I` is the original intensity of the pixel, and `B` is the brightness adjustment value. Positive values increase brightness, while negative values darken the image.

### Canny Edge Detection Filter

![Canny Edge Detection](images/Canny%20Edge%20Detection.png)
The Canny Edge Detection filter is a multi-stage algorithm that aims to extract meaningful edges from an image while minimizing noise. The process involves the following steps:

Gaussian Blurring: Smooth the image to reduce noise using a Gaussian filter.

The Gaussian blur function can be represented as:

`G(x, y) = (1 / (2 * pi * sigma^2)) * exp(-(x^2 + y^2) / (2 * sigma^2))`
where sigma is the standard deviation, which determines the extent of the blur.

Gradient Calculation: Compute the intensity gradients in both horizontal and vertical directions using Sobel operators.

The gradients in the x and y directions are represented by:

`Gx = [[-1, 0, 1],
      [-2, 0, 2],
      [-1, 0, 1]]`

`Gy = [[-1, -2, -1],
      [0, 0, 0],
      [1, 2, 1]]`
The magnitude of the gradient G can be calculated as:

`G = sqrt(Gx^2 + Gy^2)`
Non-Maximum Suppression: Suppress pixels that are not part of an edge by comparing the gradient magnitude of a pixel with its neighbors along the direction of the gradient.

Double Thresholding: Apply a double threshold to distinguish between strong, weak, and non-relevant pixels. Strong pixels are considered edges, while weak pixels are evaluated based on connectivity to strong pixels.

Edge Tracking by Hysteresis: Finalize edges by tracing weak pixels that are connected to strong pixels, thus retaining the meaningful edges and discarding noise.
## Configuration

The project can be configured using environment variables or configuration files. Example configuration includes:

- Setting the port for the backend server.

Example:

```env
# .env file
FLASK_APP=app.py
PORT=5000
```

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

Feel free to suggest improvements or report bugs via issues.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
