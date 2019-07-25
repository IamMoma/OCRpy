# OCRpy - Optical Character Recognition App with Python

## > About

![Markdown Logo](https://www.scantopdf.com/images/default-source/desktop-assets/solutions_ocr.png?sfvrsn=e1482150_2) 

This is my first project with Python. Hope you find it useful!

OCR - what is it? - https://searchcontentmanagement.techtarget.com/definition/OCR-optical-character-recognition

Image restrictions:

- Allowed image extensions - JPEG, JPG, PNG, GIF
- Max image size = 0.5 * 1024 * 1024
<hr>

## > Prerequisites

Tesseract OCR:

- Download - https://github.com/tesseract-ocr/tesseract/wiki

- add Tesseract to your path.

Python 3.7:

- Download - https://www.python.org/downloads/

<hr>

## > Running the Application

Clone the repository:

```bash
$ git clone https://github.com/IamMoma/OCRpy.git
```

Check into the repository:

```bash
$ cd new
```

Set up environment and activate it. If you are using pipenv do as follows:

```bash
$ pipenv shell
```

Install requirements. If you are using pipenv do as follows:

```bash
$ pipenv install -r requirements.txt
```

Set up FLASK_APP:

```bash
$ export FLASK_APP=app.py
```

Run the app:

```bash
$ flask run
```
<hr>
