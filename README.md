# RE-VISION Eyewear: Assistive OCR System for the Visually Impaired

"RE-VISION Eyewear" is a modular Python-based assistive technology prototype that captures visual content through a webcam (or camera module), processes the image to extract text using OCR, and optionally converts it to speech using Text-to-Speech (TTS) engines. This project was developed with the aim of helping visually impaired users understand printed or handwritten text through audio feedback.

---

## About the Project

RE-VISION Eyewear is designed to:
- Capture scenes using a compact camera (e.g., mounted on glasses)
- Extract readable content from the captured image using Tesseract OCR
- Optionally convert that extracted text into audio using TTS
- Display intermediate results (like grayscale image) for debugging or further processing

This repository contains a simplified prototype version implemented in Python, ideal for extension into a full hardware-integrated system using Raspberry Pi or other edge devices.

---

## Features

- Camera-based Capture – Takes an image from the webcam or camera module
- Grayscale Processing – Improves OCR accuracy with image preprocessing
- Text Extraction – Uses Tesseract OCR to identify and extract text
- Debug Display – Visualizes intermediate output for development
- (Optional) Text-to-Speech Support – Can be integrated for real-time audio output

---

## Requirements

Install Python dependencies using:

```bash
pip install -r requirements.txt
