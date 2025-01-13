# Attempting to extract text using OCR with Tesseract OCR
from pytesseract import pytesseract
from pdf2image import convert_from_path

# Convert PDF pages to images
images = convert_from_path(pdf_path, dpi=300)

# Apply OCR on each image
ocr_text = ""
for image in images:
    ocr_text += pytesseract.image_to_string(image, lang="spa")

# Test searching for an example article in the OCR-extracted text
example_article_ocr = search_article_improved(25, ocr_text)
example_article_ocr[:500] if example_article_ocr else "No se encontró el artículo con OCR."
