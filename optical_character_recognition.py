import tesserocr
from PIL import Image


def recog(file_name: str) -> str:
    img = Image.open(file_name)
    api = tesserocr.PyTessBaseAPI()
    api.SetImage(img)
    text_ = api.GetUTF8Text()
    return text_


def save_to_file(file_name: str) -> object:
    output_text = recog(file_name)
    with open(f"{file_name}.txt", "w", encoding="utf-8") as file_:
        file_.write(output_text)
    return file_


def main():
    fname = input("Enter file name: ")
    ocr = recog(fname)
    print(ocr)
    save_to_file_response = input("save to file (y or n)?: ")
    if save_to_file_response == "y":
        save_to_file(fname)
    else:
        exit()


if __name__ == "__main__":
    main()
