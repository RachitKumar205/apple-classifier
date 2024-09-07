# Apple-Classifier - Computer Vision Module

This module is a critical component of our comprehensive drone-based apple orchard management system. It employs sophisticated image processing and machine learning techniques to meticulously monitor the health of apple trees, detect diseases at an early stage, and provide actionable insights to optimize orchard management.

## Features

- **Advanced Image Processing**: Utilizes high-resolution images captured by drones to perform detailed assessments of tree health.
- **Early Disease Detection**: Implements state-of-the-art machine learning models to identify early signs of diseases in apple trees, enabling timely intervention.
- **Bounding Box Visualization**: Provides clear visualizations of detected regions of interest on images, aiding in precise analysis.
- **Dense Region Captioning**: Generates comprehensive captions for specific regions in the images, offering detailed descriptions and insights.

## Technologies Used

- **Python**: The core programming language for the module, chosen for its versatility and extensive libraries.
- **PyTorch**: A powerful deep learning framework used for model inference, ensuring high performance and accuracy.
- **Transformers**: A library for processing and generating text using pre-trained models, crucial for our captioning tasks.
- **Pillow (PIL)**: An image processing library used for handling and manipulating image data.
- **Matplotlib**: A plotting library used for visualizing images and bounding boxes, enhancing the interpretability of results.

## Code Overview

- `main.py`: The main script that orchestrates the entire process, from image processing to caption generation and optional visualization of bounding boxes.

### Key Components

- **Model Loading**: Efficiently loads the pre-trained Florence-2-large model and processor, ensuring readiness for inference tasks.
- **Image Processing**: Downloads and processes images from provided URLs, preparing them for analysis.
- **Caption Generation**: Utilizes the model to generate dense region captions for the images, providing detailed insights.
- **Visualization**: (Commented out) Optionally visualizes the bounding boxes on the image, aiding in the interpretation of results.

## Example Use Cases

- **Early Disease Detection**: Enables the identification and treatment of diseases before they spread, significantly reducing crop loss.
- **Tree Health Assessment**: Provides a comprehensive overview of the health of apple trees using detailed aerial imagery.
- **Detailed Reporting**: Generates detailed captions and visualizations for specific regions of interest, facilitating informed decision-making.

## Future Enhancements

- **Enhanced Visualization**: Plans to improve the visualization of detected regions and captions, making the results more intuitive.
- **Model Optimization**: Aims to optimize the model for faster inference on edge devices, increasing efficiency.
- **Integration with Other Modules**: Seeks to seamlessly integrate with other modules for a holistic orchard management solution.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.