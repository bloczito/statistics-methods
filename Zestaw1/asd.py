import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"/opt/homebrew/Cellar/tesseract/4.1.1/bin/tesseract"

print(pytesseract.image_to_string("a.png"))