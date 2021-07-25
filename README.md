# ocr camera
A python application that scans images from the webcam and prints out the recorded text on the image.

## Required Packages

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the following packages:

Note: installations were all tested on Linux only.

OpenCV: for accessing and using the webcam from the application
```bash
pip install opencv-python
```

Tesseract: library for Optical Character Recognition
```bash
sudo-get install tesseract-ocr
```

Pytesseract: python wrapper for Tesseract-OCR
```bash
pip install pytesseract
```

## Usage
Start up the application using this command:
```python
$ python main.py
```
This will open a window that will display the webcam input. Bring anything with text in front of the camera and press SPACEBAR to take a photo. The text will then appear in the terminal. Press ESC to quit.