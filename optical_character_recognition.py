import re
import tesserocr
import pytesseract
from PIL import Image


def tesser_recog(file_name: str) -> str:
    img = Image.open(file_name)
    api = tesserocr.PyTessBaseAPI()
    api.SetImage(img)
    text_ = api.GetUTF8Text()
    return text_


def pytesseract_recog(file_name: str, input_lang: str) -> str:
    img = Image.open(file_name)
    text_ = pytesseract.image_to_string(img, lang=input_lang)
    return text_


def main():
    fname = input("Enter file name: ")
    ocr_method = input(
        "(1) using tesserocr or (2) using pytesseract (preferable if using non-English image text): "
    )
    if ocr_method == "1":
        ocr = tesser_recog(fname)
    elif ocr_method == "2:
        language = input("Specify language in image: ")
        ocr = pytesseract_recog(fname, language)
    else:
        print("bad response")
        quit()
    print(ocr)
    save_to_file_response = input("save to file (y or n)?: ")
    if save_to_file_response == "y":
        name = lambda inputname: re.split("\.+", inputname)
        with open(f"{name(fname)[0]}.txt", "w", encoding="utf-8") as file_:
            file_.write(ocr)
            print("output saved")
    else:
        exit()


if __name__ == "__main__":
    main()
