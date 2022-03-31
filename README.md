Optical Character Recognition (OCR) script.

Able to convert images to text using either `tesserocr` or `pytesseract`. Therefore it requires either of the two modules.

> pip install tesserocr pytesseract

or

> conda install -c conda-forge tesserocr pytesseract

if: on Linux and pytesseract error message "no language found"

> git clone https://github.com/tesseract-ocr/tessdata

copy all traineddata to /usr/share/tesseract-ocr/4.00/tessdata
