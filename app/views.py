from app import app

from flask import render_template, request, redirect

import os

from werkzeug.utils import secure_filename

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract


def ocr_core(filename):
    """
    This function will handle the core OCR processing of images.
    """
    text = pytesseract.image_to_string(Image.open(filename))  # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
    return text  # Then we will print the text in the image
    
app.config["IMAGE_UPLOADS"] = r".\app\static\img\uploads"
app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["JPEG", "JPG", "PNG", "GIF"]
app.config["MAX_IMAGE_FILESIZE"] = 0.5 * 1024 * 1024

def allowed_image(filename):
    """
    allowed image format
    """

    if not "." in filename:
        return False

    ext = filename.rsplit(".", 1)[1]

    if ext.upper() in app.config["ALLOWED_IMAGE_EXTENSIONS"]:
        return True
    else:
        return False


def allowed_image_filesize(filesize):

    if int(filesize) <= app.config["MAX_IMAGE_FILESIZE"]:
        return True
    else:
        return False

@app.route("/", methods=["GET", "POST"])

def upload_image():
    """
    uploading the image
    """
    
    if request.method == "POST":

        if request.files:

            if "filesize" in request.cookies:

                if not allowed_image_filesize(request.cookies["filesize"]):
                    print("Filesize exceeded maximum limit")
                    return redirect(request.url)

                image = request.files["image"]

                if image.filename == "":
                    print("No filename")
                    return redirect(request.url)

                if allowed_image(image.filename):
                    filename = secure_filename(image.filename)

                    image.save(os.path.join(app.config["IMAGE_UPLOADS"], filename))

                    extracted_text=ocr_core(image)               
                    return render_template("public/upload_image.html", msg='Successfully processed', extracted_text=extracted_text, img_src=app.config["IMAGE_UPLOADS"] + filename)

                else:
                    print("That file extension is not allowed")
                    return redirect(request.url)

                
    elif request.method == 'GET':
        return render_template('public/upload_image.html')